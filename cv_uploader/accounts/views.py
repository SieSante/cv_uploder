from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from .forms import SignUpForm, CVUploadForm
from .models import CV
import pandas as pd

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile')
    else:
        form = SignUpForm()
    return render(request, 'accounts/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('profile')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

def upload_cv_view(request):
    if request.method == 'POST':
        form = CVUploadForm(request.POST, request.FILES)
        if form.is_valid():
            cv = form.save(commit=False)
            cv.user = request.user
            cv.save()

            # Read the Excel file and save the content to the database
            df = pd.read_excel(cv.upload.path)
            # Process and store the dataframe as needed

            return redirect('profile')
    else:
        form = CVUploadForm()
    return render(request, 'accounts/upload_cv.html', {'form': form})

def profile_view(request):
    cv = CV.objects.filter(user=request.user).first()
    return render(request, 'accounts/profile.html', {'cv': cv})

def admin_view(request):
    cvs = CV.objects.all()
    return render(request, 'accounts/admin.html', {'cvs': cvs})
