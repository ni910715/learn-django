from django.db import models

# Create your models here.
class ToDoList(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
class Item(models.Model):
    todolist = models.ForeignKey(ToDoList, on_delete=models.CASCADE) # on_delete當ToDoList被刪除，在上面的Item也會被刪除
    text = models.CharField(max_length=300)
    complete = models.BooleanField()

    def __str__(self):
        return self.text