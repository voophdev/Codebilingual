from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile
import datetime
from django.contrib.auth import logout
from django.http import HttpResponseForbidden
from Codebilingual.views import anonymous_required
from django.contrib import messages
import re

def logout_view(request):
    logout(request)
    return redirect('users:signin')

@anonymous_required
def signin(request):
    if request.method == 'POST':
        email = request.POST.get('email')  # Get email from POST data
        password = request.POST.get('password')  # Get password from POST data
        user = authenticate(request, email=email, password=password)  # Authenticate user
        if user is not None:
            login(request, user)  # Log in the user
            
            # Check user's role and redirect accordingly
            if user.role == 'student':
                return redirect('student:student_home')  # Redirect students to student home
            elif user.role == 'instructor':
                return redirect('instructors:instructors_home')  # Redirect instructors to instructor home
            elif user.role == 'admin':
                return redirect('/admin/authuser/userprofile/')
        else:
            return render(request, 'authuser/signin.html', {'error_message': 'Invalid email or password.'})
    else:
        return render(request, 'authuser/signin.html')

@anonymous_required
def signup(request):
    if request.method == 'POST':
        # Extract form data
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        role = request.POST.get('role', 'student')  # Default role to 'student' if not provided

        # Server-side password validation
        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return render(request, 'authuser/signup.html')

        if len(password) < 8 or not re.search(r"[A-Z]", password) or not re.search(r"[0-9]", password) or not re.search(r"[^A-Za-z0-9]", password):
            messages.error(request, "Password does not meet the requirements.")
            return render(request, 'authuser/signup.html')

        # Generate user ID based on role-specific format
        if role == 'instructor':
            year = datetime.date.today().year % 100
            count = UserProfile.objects.filter(role='instructor').count() + 1
            user_id = f"I-{year:02d}-{count:04d}"
        else:
            year = datetime.date.today().year % 100
            count = UserProfile.objects.exclude(role='instructor').count() + 1
            user_id = f"{year:02d}-{count:04d}"

        try:
            # Create a new user profile with the extracted form data
            user = UserProfile.objects.create_user(user_id=user_id, first_name=first_name, last_name=last_name, email=email, password=password, role=role)
            messages.success(request, "User created successfully.")
            #login(request, user)  # Optionally log the user in
            return redirect('users:signup') 
        except Exception as e:
            messages.error(request, f"Error creating user: {e}")
            return render(request, 'authuser/signup.html')
    else:
        return render(request, 'authuser/signup.html')