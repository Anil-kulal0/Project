from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import UserForms
# Create your views here.
@login_required
def home(request):
    return render(request, 'home.html')

@login_required
def features(request):
    return render(request, 'features.html')

@login_required
def pricing(request):
    return render(request, 'pricing.html')
# def register(request):
#     return render(request, 'register.html')

def login(request):
    return render(request, 'login.html')

def logout(request):
    return render(request, 'logout.html')


def register(request):
    if request.method =='POST':
        form = UserForms(request.POST)
        if form.is_valid():
            user = form.save()
            user.set_password(user.password)
            user.save()
            return redirect('/accounts/login/')
    form = UserForms()
    return render(request, 'register.html', {'form':form})