from django.shortcuts import render, redirect
from .models import Todo
from django.views.decorators.http import require_POST

def index(request):
    todos = Todo.objects.order_by('id')
    return render(request, 'todos/index.html', {'todos': todos})

@require_POST
def addTodo(request):
    new_todo = Todo(text=request.POST['text'])
    new_todo.save()
    return redirect('index')

def completeTodo(request, todo_id):
    todo = Todo.objects.get(pk=todo_id)
    todo.completed = True
    todo.save()
    return redirect('index')

def deleteTodo(request, todo_id):
    todo = Todo.objects.get(pk=todo_id)
    todo.delete()
    return redirect('index')
