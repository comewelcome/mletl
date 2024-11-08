from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm, LoginForm

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = SignUpForm()
    return render(request, 'users/signup.html', {'form': form})

@login_required
def dashboard_view(request):
    return render(request, 'users/dashboard.html')

def logout_view(request):
    logout(request)
    return redirect('login') 
