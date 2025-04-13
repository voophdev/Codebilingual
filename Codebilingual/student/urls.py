from django.urls import path
from . import views

app_name = 'student'

urlpatterns = [
    path('', views.student_home, name='student_home'),
    path('select-language/', views.select_language, name='select_language'),
    path('lesson/cpp/', views.cpp_lessonlist, name='cpp_lessonlist'),
    path('lesson/cpp/<slug:lesson_slug>/', views.cpp_lesson_detail, name='cpp_lesson_detail'),
    path('lesson/py/', views.py_lessonlist, name='py_lessonlist'),
    path('lesson/py/<slug:lesson_slug>/', views.py_lesson_detail, name='py_lesson_detail'),
]
