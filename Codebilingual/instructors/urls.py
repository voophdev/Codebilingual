from django.urls import path
from . import views

app_name = 'instructors'

urlpatterns = [
    path('', views.instructors_home, name='instructors_home'),
    path('create-instructor/', views.protected_create_instructor, name='create_instructor'), # Assuming you have a dashboard view for instructors
    path('cpp_dashboard',views.cpp_dashboard, name='cpp_dashboard'),
    path('py_dashboard/', views.py_dashboard, name='py_dashboard'), 
]
