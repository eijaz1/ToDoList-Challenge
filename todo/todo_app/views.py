from django.shortcuts import render, redirect
from .models import ToDoItem
from .forms import ToDoItemForm

#get ToDoItems and display them

def index(request):
    todo_list = ToDoItem.objects.order_by('-due_date')
    context = {'todo_list': todo_list}
    return render(request, 'todo_app/index.html', context)

def create_todo_item(request):
    form = ToDoItemForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('todo_app:index')
    return render(request, 'todo_item_form.html', {'form': form})

def update_todo_item(request, id):
    todo_item = ToDoItem.objects.get(id=id)
    form = ToDoItemForm(request.POST or None, instance=todo_item)
    if form.is_valid():
        form.save()
        return redirect('todo_app:index')
    return render(request, 'todo_item_form.html', {'form': form, 'todo_item': todo_item})

def delete_todo_item(request, id):
    todo_item = ToDoItem.objects.get(id=id)
    todo_item.delete()
    return redirect('todo_app:index')
