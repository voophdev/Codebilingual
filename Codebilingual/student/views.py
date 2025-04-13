from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from student.models import LessonCPP, LessonPY, LessonCompletion
from authuser.models import UserProfile

# Custom decorator to check if the user is a student
def student_required(view_func):
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.role == 'student':
                return view_func(request, *args, **kwargs)
            elif request.user.role == 'instructor':
                return redirect('instructors:instructor_home')  # Adjust the name to your actual instructor homepage URL name
            elif request.user.role == 'admin':
                return redirect('/admin/authuser/userprofile/')  # Adjust the name to your actual admin homepage URL name
            else:
                return HttpResponseForbidden("You don't have permission to access this page.")
        else:
            return redirect('users:signin')
    return wrapper

# Create your views here.

@student_required
def student_home(request):
    return render(request, 'student/student_home.html')

@login_required
@student_required
def select_language(request):
    return render(request, 'student/select_language.html')

# Helper function to check if the previous lesson is completed
def is_previous_lesson_completed(user, lesson):
    if lesson.previous_lesson:
        if isinstance(lesson, LessonCPP):
            return LessonCompletion.objects.filter(user=user, lesson_cpp=lesson.previous_lesson, completed=True).exists()
        elif isinstance(lesson, LessonPY):
            return LessonCompletion.objects.filter(user=user, lesson_py=lesson.previous_lesson, completed=True).exists()
    return True  # If there's no previous lesson, allow access

@login_required
@student_required
def cpp_lessonlist(request):
    lessons_cpp = LessonCPP.objects.all()
    completed_lessons = LessonCompletion.objects.filter(user=request.user, completed=True).values_list('lesson_cpp', flat=True)
    return render(request, 'student/lesson/cpp/cpp_lessonlist.html', {
        'lessons_cpp': lessons_cpp,
        'completed_lessons': completed_lessons,
        'lesson_type': 'cpp'
    })

@login_required
@student_required
def cpp_lesson_detail(request, lesson_slug):
    lesson = get_object_or_404(LessonCPP, slug=lesson_slug)
    
    if lesson.previous_lesson is None or is_previous_lesson_completed(request.user, lesson):
        if request.method == "POST":
            LessonCompletion.objects.get_or_create(user=request.user, lesson_cpp=lesson, completed=True)
            return redirect('student:cpp_lessonlist')

        return render(request, f'student/lesson/cpp/{lesson_slug}.html', {'lesson': lesson, 'lesson_type': 'cpp'})
    else:
        return HttpResponseForbidden("You must complete the previous lesson first.")

@login_required
@student_required
def py_lessonlist(request):
    lessons_py = LessonPY.objects.all()
    completed_lessons = LessonCompletion.objects.filter(user=request.user, completed=True).values_list('lesson_py', flat=True)
    return render(request, 'student/lesson/python/py_lessonlist.html', {
        'lessons_py': lessons_py,
        'completed_lessons': completed_lessons,
        'lesson_type': 'py'
    })

@login_required
@student_required
def py_lesson_detail(request, lesson_slug):
    lesson = get_object_or_404(LessonPY, slug=lesson_slug)
    
    if lesson.previous_lesson is None or is_previous_lesson_completed(request.user, lesson):
        if request.method == "POST":
            LessonCompletion.objects.get_or_create(user=request.user, lesson_py=lesson, completed=True)
            return redirect('student:py_lessonlist')

        return render(request, f'student/lesson/python/{lesson_slug}.html', {'lesson': lesson, 'lesson_type': 'py'})
    else:
        return HttpResponseForbidden("You must complete the previous lesson first.")
