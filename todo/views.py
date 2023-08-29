from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from .models import Task

# Create your views here.
def AddTask(request):
    task_field = request.POST.get('taskadd')
    Task.objects.create(task=task_field)
    return redirect('home')
def MarkAsDone(request,nk):
    task_done = get_object_or_404(Task,pk=nk)
    task_done.is_completed = True
    task_done.save()
    return redirect('home')
def MarkAsUndo(request,pk):
    u_task = get_object_or_404(Task,pk=pk)
    u_task.is_completed = False
    u_task.save()
    return redirect('home')
def MarkEdit(request,pk):
    task_edit = get_object_or_404(Task,pk=pk)
    if request.method == 'POST':
        new_task = request.POST.get('taskedit')
        task_edit.task = new_task
        task_edit.save()
        return redirect('home')
    else:
        context = {
            'data' : task_edit
        }
    return render(request,'edit.html',context)
def Delete(request,pk):
    mark_delete = get_object_or_404(Task,pk=pk)
    mark_delete.delete()
    return redirect('home')