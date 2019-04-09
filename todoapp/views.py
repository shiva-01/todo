from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login, logout
from .models import TodoList
from .forms import SignUpForm, TodoListform
from django.contrib import messages
from django.core.mail import send_mail

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            #username = form.cleaned_data.get('username')
            #raw_password = form.cleaned_data.get('password1')
            #user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('todoList')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('todoList')

    else:
        form = AuthenticationForm()
    return render(request, 'login.html',{'form':form})

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login')
    return redirect('login')


def todoList(request):
    if request.POST:
        form = TodoListform(request.POST)
        if form.is_valid():
            form.save(commit = False)
            form.user = request.user
            form.save()
            tasks = TodoList.objects.all()
            messages.success(request, ("New Task to be done"))
            return render(request, 'todo.html', {'form':form,'tasks':tasks})
        else:
            return HttpResponse("form invalid")
    else:
        tasks = TodoList.objects.all()
        return render(request, 'todo.html', {'tasks':tasks})

    return render(request, 'todo.html')

def deleteTask(request, task_id):
    task = TodoList.objects.get(pk = task_id)
    task.delete()
    messages.success(request, ("Task has been deleted"))
    return redirect('todoList')

def task_compleated(request, task_id):
    task = TodoList.objects.get(pk = task_id)
    task.Accomplished = True
    task.save()
    return redirect('todoList')

def task_not_compleated(request, task_id):
    task = TodoList.objects.get(pk = task_id)
    task.Accomplished = False
    task.save()
    return redirect('todoList')

def editTask(request, task_id):
    if request.method =="POST":
        task = TodoList.objects.get(pk = task_id)
        form = TodoListform(request.POST or None, instance = task)
        if form.is_valid():
            form.save()
            messages.success(request, ("Task has been edited"))
            return redirect("todoList")
    else:
        task = TodoList.objects.get(pk = task_id)
        return render(request, 'edit_task.html', {'edit_task':task})
    pass
