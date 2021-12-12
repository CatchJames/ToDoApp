from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoForm

def index(request):

    tasks = Todo.objects.all()
    form = TodoForm()
    context = {'form': form, 'tasks': tasks}
    return render(request, 'Todo/index.html', context)


def update(request, id):
    task = Todo.objects.get(id=id)
    form = TodoForm(request.POST or None, instance=task)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {'form': form}
    return render(request, 'Todo/update.html', context)


def delete(request, id):
    task = Todo.objects.get(id=id)
    context = {'task': task}
    if request.method == 'POST':
        task.delete()
        return redirect('index')

    return render(request, 'Todo/delete.html', context)

def add(request):
    form = TodoForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('index')



    context = {'form': form}
    return render(request, 'todo/index.html', context)

def complete_task(request, id):
    task = Todo.objects.get(id=id)
    task.completed = True
    task.save()

    return redirect('index')