from django.shortcuts import render
from django.contrib.auth.decorators import  login_required
# Create your views here.
@login_required(login_url="/users/login")
def BLD3home(request):
    return render(request, 'course/BLD3home.html')
def BLD4home(request):
    return render(request, 'course/BLD4home.html')
def BLD5home(request):
    return render(request, 'course/BLD5home.html')
def home(request):
    return render(request, 'course/coursehome.html')