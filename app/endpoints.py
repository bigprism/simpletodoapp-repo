from django.urls import path

from . import views

urlpatterns = [
    # REST API endpoints
    path('api/add_todo_item/', views.add_todo_item_api, name='add_todo_item_api'),
    path('api/delete_todo_item/<int:todo_item_id>/', views.delete_todo_item_api, name='delete_todo_item_api'),
    path('api/update_todo_item/<int:todo_item_id>/', views.update_todo_item_api, name='update_todo_item_api'),
    path('api/list_todo_items/', views.list_todo_items_api, name='list_todo_items_api'),
]