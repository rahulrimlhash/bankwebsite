#from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from . models import *
from django.contrib import messages, auth

# create a views here

def home(request):
    return render(request,'home.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('myapp:form')
        else:
            #messages.info(request, "invalid credentials")
            context = {
                'error':True,
                'message':'Invalid Credentials'
            }
            return render(request,'login.html',context)
            #return redirect('myapp:login')
    return render(request,'login.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['confirm_password']
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                #messages.info(request, "username taken")
                context = {
                    'error': True,
                    'message': 'Username Already exists'
                }
                return render(request,'register.html',context)
                #return redirect('myapp:register')
            else:
                user = User.objects.create_user(username=username, password=password)
                user.save();
                return redirect('myapp:login')
        else:
            #messages.info(request, "password not matching")
            context = {
                'error': True,
                'message': 'Password Not Matching'
            }
            return render(request,'register.html',context)
            #return redirect('myapp:register')
        return redirect('/')
    return render(request, "register.html")

def form(request):
    return render(request,'new_form.html')

def application(request):
    return render(request,'application.html')

def logout(request):
    auth.logout(request)
    return redirect('myapp:home')

