from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Task

# Create your views here.
def AddTask(request):
    task_field = request.POST.get('taskadd')
    Task.objects.create(task=task_field)
    return redirect('home')
