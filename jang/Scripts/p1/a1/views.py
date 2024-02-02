from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,logout
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def index(request):
    error_message =None
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            error_message='Invalid Login'
    return render(request, 'index.html',{'error_message':error_message})
def out(request):
    logout(request)
    return redirect('index')

@login_required(login_url='index')
def home(request):
    return render(request,'home.html')


def register(request):
    if request.method == 'POST':
        Name = request.POST['Name']
        username = request.POST['username']
        Email = request.POST['Email']
        password = request.POST['password']
        check_user =User.objects.filter(username=username)
        if check_user:
            messages.info(request,"Username already exists")
        else:
            user = User.objects.create_user(username=username,password=password,email=Email,first_name=Name)
            user.save()
            return redirect('/')
    return render(request,'register.html')

