from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Task
#from .forms import TaskForm


# Create your views here.
def tasklist(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/list.html', {'tasks': tasks})   

def novatarefa(request):
    form = TaskForm()
    return render(request, 'tasks/addtask.html', {'form': form}) 

def taskview(request, id):
    task = get_object_or_404(Task, pk=id)
    return render(request, 'tasks/task.html', {'task': task})


def helloworld(request):
    return HttpResponse("<h1>Hello World</h1>")


def yourname(request, name):
    return render(request, 'tasks/yourname.html', {'name': name})
