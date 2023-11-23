from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth  import authenticate,login
 

# Create your views here.

def home(request):
    return render(request,"authentication/index.html")

def signup(request):

    if request.method == "POST":
        username = request.POST['username']
        FirstName = request.POST['First Name']
        LastName = request.POST['Last Name']
        Email = request.POST['Email']
        Password1 = request.POST['Password1']
        Password2 = request.POST['Password2']

        myuser = User.objects.create_user(username, Email, Password1)
        myuser.FirstName = FirstName
        myuser.LastName = LastName
        myuser.save()
        
        messages.success(request, "Your account has been successfully created!!")
        return redirect('signin')




    return render(request, "authentication/signup.html")

def signin(request):

    if request.method == 'POST':
        username = request.POST['username']
        Password1 = request.POST['Password1']

        user = authenticate(username=username, password=Password1)

        if user is not None:
            login(request, user)
            fname = user.username
            return render(request,"authentication/index.html",{
                'fname':fname
            })
        else:
            messages.error(request, "Username OR Password is incorrect")
            return redirect('home')



    return render(request, "authentication/signin.html")

def signout(request):
    pass