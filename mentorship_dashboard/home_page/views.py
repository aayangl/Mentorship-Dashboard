from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import StudentRegistrationForm, MentorRegistrationForm

def home(request):
    """Landing page view with registration options"""
    return render(request, 'home_page/index.html')

def student_registration(request):
    """Handle student registration"""
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Student registration successful!')
            return redirect('registration_success')
    else:
        form = StudentRegistrationForm()
    return render(request, 'home_page/student_registration.html', {'form': form})

def mentor_registration(request):
    """Handle mentor registration"""
    if request.method == 'POST':
        form = MentorRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Mentor registration successful!')
            return redirect('registration_success')
    else:
        form = MentorRegistrationForm()
    return render(request, 'home_page/mentor_registration.html', {'form': form})

def registration_success(request):
    """Display success message after registration"""
    return render(request, 'home_page/registration_success.html')
