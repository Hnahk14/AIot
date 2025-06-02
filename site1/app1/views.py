from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request,'app1/home.html') 
def register (request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
        
    context={'form':form}
    return render(request,'app1/register.html',context)
def loginPage (request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username = username, password = password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else: messages.info(request,'user or password not correct!')
    context={}
    return render(request,'app1/login.html',context)