from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages

from .models import AccountDetails
from BankingSystem.models import BankingSystem
# Create your views here.
def registerPage(request):
    if request.method == "POST":
        Data = request.POST
        user = User.objects.create_user(username =Data['username'], email = Data['email'], password = Data['password1'],first_name = Data['FirstName'], last_name = Data['LastName'],)
        A = AccountDetails(aadhar_number = Data['Aadhar'],UserName =Data['username'],Address = Data['Address'],FirstName = Data['FirstName'], LastName = Data['LastName'], email = Data['email'], phone_number = Data['PhoneNumber'],pan_number = Data['PanCard'],Gender = Data['Gender'])
        A.save()
        instance = BankingSystem(Username = A, Balance = 0)
        instance.save()
        username = Data['username']
        password = Data['password1']
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('Home')

    elif request.method == "GET":
        return render(request, 'Register.html')


def logoutUser(request):
    logout(request)
    return redirect('Login')
def loginPage(request):
    context= {'User' : User}
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username = username, password = password)

        if user is not None:
            login(request,user)
            return redirect('Home') 
        else:
            messages.info(request, 'Username Or Password Is Incorrect :(')
            return render (request,'Login.html', context)
    
    return render (request,'Login.html', context)


def Home(request):
    return render(request, 'Home.html')

def Contact(request):
    return render(request, 'Contact.html')