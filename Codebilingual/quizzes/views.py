from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import PythonQuiz, PythonResult, CppQuiz, CppResult, PythonQuizCompletion, CppQuizCompletion
from .forms import PythonQuizForm, CppQuizForm
from django.conf import settings  # Import settings module
from student.views import student_required

@login_required
@student_required
def select_quiz(request):
    return render(request, 'quizzes/select_language.html')

from django.conf import settings

@login_required
@student_required
def python_quiz_list(request):
    quizzes = PythonQuiz.objects.all()
    user = request.user

    # Fetch completed quizzes for the current user
    completed_quizzes = PythonQuizCompletion.objects.filter(user=user, completed=True).values_list('quiz__id', flat=True)

    # Determine if the previous quiz is completed
    previous_completed = True
    quiz_status = []
    for quiz in quizzes:
        result = PythonResult.objects.filter(user=user, quiz=quiz).first()
        if previous_completed:
            quiz_status.append({
                'quiz': quiz,
                'completed': quiz.id in completed_quizzes,
                'result': result,
                'locked': False
            })
            previous_completed = quiz.id in completed_quizzes
        else:
            if result and result.attempts < settings.MAX_ATTEMPTS:  # Check if attempts < MAX_ATTEMPTS
                quiz_status.append({
                    'quiz': quiz,
                    'completed': False,
                    'result': result,
                    'locked': False  # Quiz is not locked if attempts < MAX_ATTEMPTS
                })
            else:
                quiz_status.append({
                    'quiz': quiz,
                    'completed': False,
                    'result': result,
                    'locked': True  # Quiz is locked if attempts >= MAX_ATTEMPTS
                })
        previous_completed = quiz.id in completed_quizzes  # Move this line inside the loop

    return render(request, 'quizzes/py/python_quiz_list.html', {'quiz_status': quiz_status})


@login_required
@student_required
def take_python_quiz(request, quiz_id):
    quiz = get_object_or_404(PythonQuiz, pk=quiz_id)
    user = request.user
    
    # Check if the user has already completed this quiz
    if PythonQuizCompletion.objects.filter(user=user, quiz=quiz, completed=True).exists():
        return redirect('quizzes:python_quiz_list')

    result, created = PythonResult.objects.get_or_create(user=user, quiz=quiz)

    if request.method == 'POST':
        form = PythonQuizForm(request.POST, quiz=quiz)
        if form.is_valid():
            score = 0
            total_questions = quiz.questions.count()
            for question in quiz.questions.all():
                selected_choice_id = form.cleaned_data.get(f'question_{question.id}')
                if selected_choice_id:
                    selected_choice = question.choices.get(pk=selected_choice_id)
                    if selected_choice.is_correct:
                        score += 1
            score_percentage = (score / total_questions) * 100
            
            result.attempts += 1
            result.score = score_percentage
            result.save()
            
            # Save the quiz completion status
            PythonQuizCompletion.objects.create(user=user, quiz=quiz, completed=True)
            
            request.session['quiz_answers'] = form.cleaned_data
            
            return redirect('quizzes:python_quiz_list')
    else:
        previous_answers = request.session.get('quiz_answers')
        if previous_answers:
            form = PythonQuizForm(quiz=quiz, initial=previous_answers)
        else:
            form = PythonQuizForm(quiz=quiz)
        
    return render(request, 'quizzes/py/take_python_quiz.html', {'quiz': quiz, 'form': form, 'quiz_type': 'py'})


@login_required
@student_required
def python_quiz_result(request, quiz_id):
    quiz = get_object_or_404(PythonQuiz, pk=quiz_id)
    result = get_object_or_404(PythonResult, user=request.user, quiz=quiz)
    return render(request, 'quizzes/py/python_quiz_result.html', {'quiz': quiz, 'result': result})

@login_required
@student_required
def cpp_quiz_list(request):
    quizzes = CppQuiz.objects.all()
    user = request.user

    # Fetch completed quizzes for the current user
    completed_quizzes = CppQuizCompletion.objects.filter(user=user, completed=True).values_list('quiz__id', flat=True)

    # Determine if the previous quiz is completed
    previous_completed = True
    quiz_status = []
    for quiz in quizzes:
        result = CppResult.objects.filter(user=user, quiz=quiz).first()
        if result and result.attempts >= settings.MAX_ATTEMPTS:
            locked = True
        else:
            locked = not previous_completed
        if previous_completed:
            quiz_status.append({
                'quiz': quiz,
                'completed': quiz.id in completed_quizzes,
                'result': result,
                'locked': False
            })
            previous_completed = quiz.id in completed_quizzes
        else:
            quiz_status.append({
                'quiz': quiz,
                'completed': False,
                'result': result,
                'locked': locked
            })

    return render(request, 'quizzes/cpp/cpp_quiz_list.html', {'quiz_status': quiz_status})

@login_required
@student_required
def take_cpp_quiz(request, quiz_id):
    quiz = get_object_or_404(CppQuiz, pk=quiz_id)
    user = request.user
    
    if CppQuizCompletion.objects.filter(user=user, quiz=quiz, completed=True).exists():
        return redirect('quizzes:cpp_quiz_list')

    result, created = CppResult.objects.get_or_create(user=user, quiz=quiz)

    if request.method == 'POST':
        form = CppQuizForm(request.POST, quiz=quiz)
        if form.is_valid():
            score = 0
            total_questions = quiz.questions.count()
            for question in quiz.questions.all():
                selected_choice_id = form.cleaned_data.get(f'question_{question.id}')
                if selected_choice_id:
                    selected_choice = question.choices.get(pk=selected_choice_id)
                    if selected_choice.is_correct:
                        score += 1
            score_percentage = (score / total_questions) * 100
            
            result.attempts += 1
            result.score = score_percentage
            result.save()
            
            CppQuizCompletion.objects.create(user=user, quiz=quiz, completed=True)
            
            request.session['quiz_answers'] = form.cleaned_data
            
            return redirect('quizzes:cpp_quiz_list')
    else:
        previous_answers = request.session.get('quiz_answers')
        if previous_answers:
            form = CppQuizForm(quiz=quiz, initial=previous_answers)
        else:
            form = CppQuizForm(quiz=quiz)
        
    return render(request, 'quizzes/cpp/take_cpp_quiz.html', {'quiz': quiz, 'form': form, 'quiz_type': 'cpp'})

@login_required
@student_required
def cpp_quiz_result(request, quiz_id):
    quiz = get_object_or_404(CppQuiz, pk=quiz_id)
    result = get_object_or_404(CppResult, user=request.user, quiz=quiz)
    return render(request, 'quizzes/cpp/cpp_quiz_result.html', {'quiz': quiz, 'result': result})