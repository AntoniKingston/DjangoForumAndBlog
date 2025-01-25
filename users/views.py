from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib import messages

from .forms import UserRegistrationForm, UserLoginForm

def activateEmail(request, user, email):
    messages.success(request, f'A message with activation link has been sent to {email}')

def registration_view(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            activateEmail(request, user, form.cleaned_data.get('email'))
            return redirect("/")
    else:
        form = UserCreationForm()
    return render(request, 'users/registration.html', {"form" : form})
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user(), )
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            return redirect("/")

    else:
        form = AuthenticationForm()
    return render(request, 'users/login.html', {"form" : form})
def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect("/")