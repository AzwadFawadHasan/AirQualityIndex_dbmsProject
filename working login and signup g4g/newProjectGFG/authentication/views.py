import email
from turtle import setx
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout 

import authentication
# Create your views here.

def home (request):
    return render(request, "authentication/index.html")



def signup (request):
    if request.method == "POST":
        username= request.POST.get('username')
        first_name=request.POST.get('fname');
        last_name=request.POST.get('lname');
        
        email=request.POST.get('email');
        password1=request.POST.get('password');
        password2= request.POST.get('pass2')

        userType = request.POST.get('userType');


        myuser = User.objects.create_user(username, email, password2)
        myuser.lastname = last_name
        

        myuser.save();
        messages.success(request, "your acc has been created")
        return redirect('signin')

    return render(request, "authentication/signup.html")




def signin (request):
    if request.method == 'POST':
        username = request.POST['username']
        userType = request.POST['userType']
        pass1 = request.POST['pass1']

        user = authenticate(username=username,userType=userType, password=pass1)

        if user is not None:
            
            login(request, user)
            fname = user.first_name
            return render(request, "authentication/index.html", {'fname':fname})
        else:
            messages.error(request, "Bad Credentials");
            return redirect('home')    

    return render(request, "authentication/signin.html")



def signout (request):
    logout(request)
    messages.success(request, "Logged out successful")
    return redirect('home')