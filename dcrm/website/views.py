from django.shortcuts import render, redirect
from .forms import EditTaskForm
from django.shortcuts import HttpResponse
from django.contrib.auth import authenticate, login as loginUser, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from website.forms import TODOForm
from website.models import TODO
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
import logging

logger = logging.getLogger(__name__)


def home(request):
    if request.user.is_authenticated:
        user = request.user
        form = TODOForm()
        todos = TODO.objects.filter(user=user)
        return render(request, 'index.html', context={'form': form, 'todos':
                                                      todos})
    else:
        return redirect('login')


def login(request):
    if request.method == 'GET':
        form = AuthenticationForm()
        return render(request, 'login.html', context={
            "form": form
        })
    else:
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                loginUser(request, user)
                messages.success(request, 'You have logged in successfully')
                return redirect('home')
        else:

            return render(request, 'login.html', context={
                "form": form
            })


def signUp(request):
    if request.method == 'GET':
        form = UserCreationForm()
        return render(request, 'signUp.html', context={
            "form": form
        })
    else:
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            if user:
                return redirect('login')
        else:

            return render(request, 'signUp.html', context={
                "form": form
            })


def add_todo(request):

    if request.user.is_authenticated:
        user = request.user

        if request.method == 'POST':
            form = TODOForm(request.POST)
            if form.is_valid():
                todo = form.save(commit=False)
                todo.user = user
                todo.save()
                return redirect("home")
        else:
            form = TODOForm()

        return render(request, 'index.html', context={'form': form})
    else:
        return redirect("login")


def user_logout(request):
    logout(request)
    return redirect("home")


def delete_todo(request, id):
    try:
        todo = TODO.objects.get(pk=id)
        if todo.user == request.user:
            todo.delete()
            messages.success(request, 'Task has been deleted successfully.')
        else:
            messages.error(
                request, 'You do not have permission to delete this task.')
    except ObjectDoesNotExist:
        return HttpResponse('Task with ID {} does not exist.'.format(id))

    return redirect("home")


def change_todo(id, status):
    try:
        todo = TODO.objects.get(pk=id)
        print(f"Before update - Status: {todo.status}")
        todo.status = status
        todo.save()
        print(f"After update - Status: {todo.status}")
        return redirect("home")
    except ObjectDoesNotExist:
        return HttpResponse('Task with ID {} does not exist.'.format(id))


def edit_details(request, id, status):
    try:
        todo = TODO.objects.get(pk=id)

        if todo.user == request.user:
            if request.method == 'POST':
                form = EditTaskForm(request.POST, instance=todo)
                if form.is_valid():
                    form.save()
                    return redirect("home")
                else:
                    return render(request, 'edit_details.html',
                                  {'form': form, 'todo': todo})
            else:
                form = EditTaskForm(instance=todo)
            message = f"Editing TODO with ID {id} and status '{status}'"
            return render(request, 'edit_details.html',
                          {'form': form, 'todo': todo, 'message': message})
        else:
            return HttpResponse('You do not have permission to edit this task.'
                                )

    except ObjectDoesNotExist:
        return HttpResponse('Task with ID {} does not exist.'.format(id))
