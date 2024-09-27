from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import UserProfile 

def home(request):
    if request.user.is_authenticated:
        user_profile = UserProfile.objects.get(user=request.user)
        return render(request, 'home.html', {'user': user_profile})
    return redirect('login')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['loginUsername']
        password = request.POST['loginPassword']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to home after login
        else:
            error = "Invalid username or password"
            return render(request, 'register.html', {'error': error})
    return render(request, 'register.html')

# Decorator to check if the user is an admin
def is_admin(user):
    return user.is_staff  # Assuming 'is_staff' is used for admin users

@user_passes_test(is_admin)
def admin_view(request):
    users = User.objects.all()  # Fetch all users
    return render(request, 'admin.html', {'users': users})

from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import User  # Assume you have a User model defined

def register_view(request):
    if request.method == 'POST':
        username = request.POST['registerUsername']
        email = request.POST['registerEmail']
        password = request.POST['registerPassword']
        contact = request.POST['registerContact']
        dob = request.POST['registerDOB']
        gender = request.POST['gender']
        skills = request.POST['registerSkills']
        role = request.POST['userRole']
        # Handle file uploads if needed

        # Save user to the database
        user = User.objects.create(username=username, email=email, password=password, contact=contact, dob=dob, gender=gender, skills=skills, role=role)
        return redirect('login')  # Redirect to the login page after registration
    return render(request, 'register.html')  # Render the registration page
