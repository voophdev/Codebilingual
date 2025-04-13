from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden

# Custom decorator to check if the user is not authenticated
def anonymous_required(view_func):
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return view_func(request, *args, **kwargs)
        else:
            # Check the user's role and redirect accordingly
            if request.user.role == 'admin':
                return redirect('/admin/authuser/userprofile/')  # Adjust to your actual admin homepage URL
            elif request.user.role == 'student':
                return redirect('student:student_home')  # Adjust to your actual student homepage URL name
            elif request.user.role == 'instructor':
                return redirect('instructors:instructors_home')  # Adjust to your actual instructor homepage URL name
            else:
                return HttpResponseForbidden("You are already signed in.")
    return wrapper

@anonymous_required
def landingPage(request):
  return render(request, 'landing_page.html')

@anonymous_required
def about(request):
  return render(request, 'about.html')