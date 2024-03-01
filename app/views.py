from django.shortcuts import render, redirect

from django.contrib import messages

from .forms import AddTodoItemForm

from .models import TodoItem

from django.shortcuts import redirect

from django.shortcuts import render



def add_todo_item(request):
    if request.method == 'POST':
        form = AddTodoItemForm(request.POST)
        if form.is_valid():
            new_todo_item = form.save()
            messages.success(request, "Todo item added successfully")
            return redirect('list_todo_items')
    else:
        form = AddTodoItemForm()

    context = {
        'form': form,
    }
    return render(request, 'add_todo_item.html', context)



def delete_todo_item(request, todo_item_id):
    todo_item = TodoItem.objects.get(id=todo_item_id)
    todo_item.delete()
    messages.success(request, "Todo item deleted successfully")
    return redirect('list_todo_items')



def update_todo_item(request, todo_item_id):
    todo_item = TodoItem.objects.get(id=todo_item_id)

    if request.method == 'POST':
        form = AddTodoItemForm(request.POST, instance=todo_item)
        if form.is_valid():
            form.save()
            messages.success(request, "Todo item updated successfully")
            return redirect('list_todo_items')
    else:
        form = AddTodoItemForm(instance=todo_item)

    context = {
        'form': form,
        'todo_item': todo_item,
    }
    return render(request, 'update_todo_item.html', context)



def list_todo_items(request):
    todo_items = TodoItem.objects.all().order_by('due_date')

    context = {
        'todo_items': todo_items,
    }
    return render(request, 'list_todo_items.html', context)