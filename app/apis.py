from django.http import JsonResponse

from django.views.decorators.http import require_http_methods

from .models import TodoItem



@require_http_methods(['POST'])
def add_todo_item(request):
    data = request.POST.copy()
    todo_item = TodoItem.objects.create(**data)
    return JsonResponse({'status': 'success', 'todo_item': todo_item.to_dict()})



@require_http_methods(['DELETE'])
def delete_todo_item(request, todo_item_id):
    try:
        todo_item = TodoItem.objects.get(id=todo_item_id)
        todo_item.delete()
        return JsonResponse({'status': 'success'})
    except TodoItem.DoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'Todo item not found'}, status=404)



@require_http_methods(['PUT'])
def update_todo_item(request, todo_item_id):
    try:
        todo_item = TodoItem.objects.get(id=todo_item_id)
        data = request.PUT.copy()
        for key, value in data.items():
            setattr(todo_item, key, value)
        todo_item.save()
        return JsonResponse({'status': 'success', 'todo_item': todo_item.to_dict()})
    except TodoItem.DoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'Todo item not found'}, status=404)



@require_http_methods(['GET'])
def list_todo_items(request):
    todo_items = TodoItem.objects.all()
    todo_items_list = [todo_item.to_dict() for todo_item in todo_items]
    return JsonResponse({'status': 'success', 'todo_items': todo_items_list})