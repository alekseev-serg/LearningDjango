from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm


# Create your views here.
def todolist(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save()
            return redirect('todolist')
    else:
        form = TaskForm()
    tasks = Task.objects.order_by('-created').filter(completed=False)
    return render(request, 'todolist/todolist.html', {'tasks': tasks,
                                                      'form': form, })


def edit_task(request, pk):
    task = Task.objects.get(pk=pk)
    form = TaskForm(instance=task)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            task = form.save()
            return redirect('todolist')
    return render(request, 'todolist/edit_task.html', {'task': task,
                                                       'form': form})


def done_list(request):
    tasks = Task.objects.filter(completed=True).order_by('-created')
    return render(request, 'todolist/done_list.html', {'tasks': tasks})


def done_task(request, pk):
    task = Task.objects.get(pk=pk)
    task.completed = True
    task.save()
    return redirect('todolist')


def recover_task(request, pk):
    task = Task.objects.get(pk=pk)
    task.completed = False
    task.save()
    return redirect('todolist')


def delete_task(request, pk):
    task = Task.objects.get(pk=pk)
    task.delete()
    return redirect('done_list')
