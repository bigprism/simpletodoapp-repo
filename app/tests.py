from django.test import TestCase

from .models import TodoItem

class AddTodoItemTestCase(TestCase):
    def test_add_todo_item(self):
        """Test that a todo item can be added."""
        todo_item = TodoItem.objects.create(title="Test todo item")
        self.assertEqual(todo_item.title, "Test todo item")

from django.test import TestCase

from .models import TodoItem

class DeleteTodoItemTestCase(TestCase):
    def test_delete_todo_item(self):
        """Test that a todo item can be deleted."""
        todo_item = TodoItem.objects.create(title="Test todo item")
        todo_item.delete()
        self.assertFalse(TodoItem.objects.filter(title="Test todo item").exists())

from django.test import TestCase

from .models import TodoItem

class UpdateTodoItemTestCase(TestCase):
    def test_update_todo_item(self):
        """Test that a todo item can be updated."""
        todo_item = TodoItem.objects.create(title="Test todo item")
        todo_item.title = "Updated test todo item"
        todo_item.save()
        self.assertEqual(todo_item.title, "Updated test todo item")

from django.test import TestCase

from .models import TodoItem

class ListTodoItemsTestCase(TestCase):
    def test_list_todo_items(self):
        """Test that a list of todo items can be retrieved."""
        todo_item1 = TodoItem.objects.create(title="Test todo item 1")
        todo_item2 = TodoItem.objects.create(title="Test todo item 2")
        todo_items = TodoItem.objects.all()
        self.assertEqual(list(todo_items), [todo_item1, todo_item2])