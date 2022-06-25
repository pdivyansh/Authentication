from django.shortcuts import render
from .models import *
# Create your views here.
def register(request):
    return render(request,'register.html')

def UserRegister(request):
    if request.method == 'POST':
        fname=request.POST['firstname']
        lname=request.POST['lastname']
        email=request.POST['email']
        contact=request.POST['contact']
        password=request.POST['password']
        cpassword=request.POST['cpassword']
        # first we will validate that user already exist
        user=User.objects.filter(Email=email)
        if user:
            message = "user already exist"
            return render(request,'register.html',{'msg':message})
        else:
            if password==cpassword:
                newuser=User.objects.create(Firstname=fname,Lastname=lname,Email=email,Contact=contact,Password=password)
                message="user register successfully"
                return render(request,'login.html',{'msg':message})
            else:
                message="password and confirm password does not match"
                return render(request,'register.html',{'msg':message})

def login(request):
    return render(request,'login.html')

def LoginUser(request):
    if request.method=='POST':
        email=request.POST['email']
        password=request.POST['password']

        # checking the emailid with database
        user=User.objects.get(Email=email)

        if user:
            if user.Password==password:
                request.session['Firstname']=user.Firstname
                request.session['Lastname']=user.Lastname
                request.session['Email']=user.Email
                return render(request,'home.html')
            else:
                message="password does not match"
                return render(request,'login.html',{'msg':message})
        else:
            message="user does not exist"
            return render(request,'register.html',{'msg':message})


    