from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from student.views import student_required
from django.http import FileResponse, HttpResponseNotFound
import os
from django.conf import settings
# Create your views here.

@login_required
@student_required
def translate(request):
  return render(request, 'translator/translate.html')

@login_required
@student_required
def download_windows(request):
    # Specify the path to the file relative to your project directory
    file_relative_path = 'static/translator/codebilingual-windows.exe'

    # Construct the absolute file path using Django's BASE_DIR setting
    file_path = os.path.join(settings.BASE_DIR, file_relative_path)

    # Check if the file exists
    if os.path.exists(file_path):
        # Serve the file using FileResponse
        response = FileResponse(open(file_path, 'rb'), as_attachment=True)
        return response
    else:
        return HttpResponseNotFound("File not found: " + file_path)
    
@login_required
@student_required
def download_mac(request):
    # Specify the path to the file relative to your project directory
    file_relative_path = 'static/translator/codebilingual-mac'

    # Construct the absolute file path using Django's BASE_DIR setting
    file_path = os.path.join(settings.BASE_DIR, file_relative_path)

    # Check if the file exists
    if os.path.exists(file_path):
        # Serve the file using FileResponse
        response = FileResponse(open(file_path, 'rb'), as_attachment=True)
        return response
    else:
        return HttpResponseNotFound("File not found: " + file_path)