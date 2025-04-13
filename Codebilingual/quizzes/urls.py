from django.urls import path
from . import views

app_name= "quizzes"

urlpatterns = [
    path('', views.select_quiz, name='select_quiz'),
    path('python/', views.python_quiz_list, name='python_quiz_list'),
    path('python/<int:quiz_id>/', views.take_python_quiz, name='take_python_quiz'),
    path('python/<int:quiz_id>/result/', views.python_quiz_result, name='python_quiz_result'),
    
    path('cpp/', views.cpp_quiz_list, name='cpp_quiz_list'),
    path('cpp/<int:quiz_id>/', views.take_cpp_quiz, name='take_cpp_quiz'),
    path('cpp/<int:quiz_id>/result/', views.cpp_quiz_result, name='cpp_quiz_result'),
]
