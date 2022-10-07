from multiprocessing import context
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegisterForm, BlogModelForm, ProfileModelForm,PostUpdateForm, CommentForm
from .models import BlogModel, ProfileModel
from django.contrib.auth.decorators import login_required




# Create your views here.
@login_required
def index(request):
    if request.user.is_authenticated:
        posts = BlogModel.objects.all()
        return render(request, 'blog/index.html', {'posts': posts})
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


@login_required
def detail(request, pk):
    if request.user.is_authenticated:
        post = BlogModel.objects.get(id=pk)
        if request.method == 'POST':
            comment_form = CommentForm(request.POST)
            if comment_form.is_valid():
                instance = comment_form.save(commit=False)
                instance.user = request.user #user vaneko logged in user
                instance.post = post
                instance.save()
                return redirect('detail-view', post.id)
         
        else:
            comment_form = CommentForm()
        context = {
            'post': post,
            'comment_form':comment_form,
        }
        return render(request, 'blog/detail.html', context)
    else:
        return HttpResponseRedirect('/login/')

@login_required(login_url = 'blog-post-edit')
def post_edit(request, pk):
    post = BlogModel.objects.get(id=pk)
    if request.method == "POST":
        form = PostUpdateForm(request.POST or None, request.FILES or None, instance=post)#instance=post gare error auxa but yesle form lai retrive garxa vaneko edit thichepaxi tyo title (input field ma tehi aunxa_)
        if form.is_valid():
            form.save()
            return redirect('detail-view', pk=post.id)
    else:
        form = PostUpdateForm(instance=post)
    context ={
        'post':post,  
        'form':form,
    }
    return render(request, 'blog/post_edit.html', context)
@login_required(login_url = 'blog-post-delete')
def post_delete(request, pk):
    post = BlogModel.objects.get(id=pk)
    if request.method =='POST':
        post.delete()
        return redirect('index')
    context={
        'post':post
    }
    return render(request, 'blog/post_delete.html',context)
@login_required
def addblog(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = BlogModelForm(request.POST or None, request.FILES or None)
            if form.is_valid():
                instance = form.save(commit=False)#reload garda submission vanera na aauna ko lagi(auto save huntheo hatako)
                instance.author = request.user
                instance.save()
                return redirect('index')
        else:
            form = BlogModelForm()
        return render(request, 'blog/addblog.html', {'form':form})
    else:
        return HttpResponseRedirect('/login/')

@login_required(login_url = 'login-user')
def profile(request):
    myblogs = BlogModel.objects.filter(author=request.user)
    if request.method == "POST":
        form = ProfileModelForm( request.POST or None, request.FILES or None, instance=request.user.profilemodel )
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileModelForm(instance=request.user.profilemodel)
    context = {
        'myblogs':myblogs,
        'form':form,
    }
    return render(request, 'blog/profile.html',context)

