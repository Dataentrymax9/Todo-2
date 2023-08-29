from django.http import HttpResponse
from django.shortcuts import render
from todo.models import Task


def Home(request):
    Todo_data = Task.objects.filter(is_completed = False).order_by('-update')
    context = {
        'data1' : Todo_data
    }
    return render(request,'index.html',context)