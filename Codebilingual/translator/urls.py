from django.urls import path
from . import views

app_name = 'translator'

urlpatterns = [
    path('', views.translate, name='translate'),
    path('download_windows/', views.download_windows, name='download_windows'),
    path('download_mac/', views.download_mac, name='download_mac'),
]