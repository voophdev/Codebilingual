from functools import wraps
from django.contrib.auth.decorators import user_passes_test, login_required
from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import InstructorCreationForm
from quizzes.models import PythonResult, CppResult, PythonQuiz


def instructor_required(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.role == 'instructor':
                return view_func(request, *args, **kwargs)
            elif request.user.role == 'student':
                return redirect('student:student_home') 
            elif request.user.role == 'admin':
                return redirect('/admin/authuser/userprofile/') 
            else:
                return HttpResponseForbidden("You don't have permission to access this page.")
        else:
            return redirect('users:signup')  
    return wrapper

def admin_required(view_func):
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated and request.user.is_superuser:
            # If the user is authenticated and is a superuser (admin), allow access to the view
            return view_func(request, *args, **kwargs)
        else:
            # If the user is not authenticated or is not an admin, redirect them to a suitable page
            messages.error(request, "You don't have permission to access this page.")
            return redirect('users:signin')  # Adjust to your actual sign-in URL name
    return wrapper

def is_admin(user):
    return user.is_superuser

@admin_required
def protected_create_instructor(request):
    if request.user.role == 'student':
        return redirect('student:student_home')  # Adjust the name to your actual student homepage URL name
    elif request.user.role == 'instructor':
        return redirect('instructors:instructors_home')  # Adjust the name to your actual instructor homepage URL name
    elif not request.user.is_authenticated:
        return redirect('user:signin')  # Adjust to your actual sign-in URL name

    return create_instructor(request)

@user_passes_test(is_admin)
def create_instructor(request):
    if request.method == 'POST':
        form = InstructorCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Instructor account created successfully.')
            return redirect('/admin/authuser/userprofile/')  # Change this to your admin dashboard URL
    else:
        form = InstructorCreationForm()

    return render(request, 'instructors/create_instructor.html', {'form': form})

@instructor_required
def instructors_home(request):
    return render(request, 'instructors/instructors_home.html')

@instructor_required
def py_dashboard(request):
    # Query all completed Python quiz results
    python_results = PythonResult.objects.all()      

    # Group Python results by user (student)
    python_students = {}
    for result in python_results:
        user_id = result.user.user_id
        if user_id not in python_students:
            python_students[user_id] = {
                'user_id': user_id,
                'full_name': f"{result.user.last_name}, {result.user.first_name}",
                'quiz_scores': {result.quiz.title: result.score},
            }
        else:
            python_students[user_id]['quiz_scores'][result.quiz.title] = result.score

    # Extract all Python quiz titles
    all_python_quiz_titles = sorted(set(PythonQuiz.objects.values_list('title', flat=True)), key=lambda x: int(x.split()[-1]))

    # Calculate total and average scores for Python students
    for student in python_students.values():
        quiz_scores = student['quiz_scores'].values()
        total_score = sum(quiz_score for quiz_score in quiz_scores if quiz_score is not None)
        average_score = total_score / len(quiz_scores) if quiz_scores else None
        student['total_score'] = total_score
        student['average_score'] = average_score

    # Sort Python students by user ID
    sorted_python_students = sorted(python_students.values(), key=lambda x: x['user_id'])

    # Pass the grouped students and sorted quiz titles to the template
    return render(request, 'instructors/python_dashboard.html', {
        'python_students': sorted_python_students,
        'all_python_quiz_titles': all_python_quiz_titles,
    })

@instructor_required
def cpp_dashboard(request):
    # Query all completed CPP quiz results
    cpp_results = CppResult.objects.all()

    # Group CPP results by user (student)
    cpp_students = {}
    for result in cpp_results:
        user_id = result.user.user_id
        if user_id not in cpp_students:
            cpp_students[user_id] = {
                'user_id': user_id,
                'full_name': f"{result.user.last_name}, {result.user.first_name}",
                'quiz_scores': {result.quiz.title: result.score},
            }
        else:
            cpp_students[user_id]['quiz_scores'][result.quiz.title] = result.score

    # Extract all CPP quiz titles (always 13 titles)
    all_cpp_quiz_titles = [f"Quiz {i}" for i in range(1, 14)]
    
    # Calculate total and average scores for CPP students
    for student in cpp_students.values():
        quiz_scores = student['quiz_scores'].values()
        total_score = sum(quiz_score for quiz_score in quiz_scores if quiz_score is not None)
        average_score = total_score / len(quiz_scores) if quiz_scores else None
        student['total_score'] = total_score
        student['average_score'] = average_score

    # Sort CPP students by user ID
    sorted_cpp_students = sorted(cpp_students.values(), key=lambda x: x['user_id'])

    return render(request, 'instructors/cpp_dashboard.html', {
        'cpp_students': sorted_cpp_students,
        'all_cpp_quiz_titles': all_cpp_quiz_titles,
    })