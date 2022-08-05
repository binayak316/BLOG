# from django.shortcuts import render, redirect
# from django.http import HttpResponseRedirect
# from django.contrib.auth import authenticate, login, logout
# from django.contrib import messages
# from django.contrib.auth.forms import AuthenticationForm
# from .forms import RegisterForm
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegisterForm


# Create your views here.
def index(request):
    if request.user.is_authenticated:
        return render(request, 'blog/index.html', {})
    else:
        return HttpResponseRedirect('/login/')



def registerUser(request):
    if not request.user.is_authenticated:
        form = RegisterForm()
        if request.method =="POST":
            form = RegisterForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('login-user')
        else:
            form = RegisterForm()
        return render(request, 'blog/register.html', {'form':form})
    else:
        return HttpResponseRedirect('/')


    
def loginUser(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            username = request.POST['username']
            password = request.POST['password']

            if username and password:
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request,user)
                    return redirect('index')
                else:
                    messages.error(request, "Username and password are Incorrect")
            else:
                messages.error(request, "Fill the fields")

        return render(request, 'blog/login.html', {})
    else:
        return HttpResponseRedirect('/')



def logoutUser(request):
    logout (request)
    return redirect('login-user')



def detail(request):
    if request.user.is_authenticated:
        return render(request, 'blog/detail.html', {})
    else:
        return HttpResponseRedirect('/login/')

    