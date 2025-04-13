from django.contrib import admin
from django.urls import path, include, re_path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.views.static import serve


urlpatterns = [
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root' : settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root' : settings.STATIC_ROOT}),
    path('admin/', admin.site.urls),
    path('', views.landingPage),
    path('', include('authuser.urls')),
    path('about/', views.about),
    path('student/', include('student.urls')),
    path('translate/', include('translator.urls')),
    path('quizzes/', include('quizzes.urls')),
    path('instructors/', include('instructors.urls')),
]