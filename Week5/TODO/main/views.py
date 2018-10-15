from django.shortcuts import render
from datetime import datetime, timedelta
from .models import Task, Task_list
from .forms import TaskForm
from django.views.decorators.csrf import csrf_exempt


def main(request):
    return render(request, 'main/main.html')



def subject(request):
    task_lists= Task_list.objects.all()

    context = {
    'task_lists': task_lists
    }
    return render(request, 'main/subjects.html', context)

def todos(request):
    
    tasks = Task.objects.all() 
    
    context = {
    'task': tasks
    }	
    return render(request, 'main/todo_list.html' ,context)


def completed_todos(request, index):
	
    tasks = Task.objects.all()
    context = {
    'task': tasks
    }
    return render(request, "main/completed_todo_list.html",context)

def add(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todos')

    form = TaskForm()
    context = {
    'form': form
    }


    return render(request, 'main/addingPage.html'  , context)


def delete(request, id):
    Task.objects.get(pk=id).delete()
    tasks = Task.objects.all()
    context= {
     'task': tasks
    }

    return render(request,'main/todo_list.html', context)