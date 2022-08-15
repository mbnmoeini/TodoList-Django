from turtle import title
from django.db import models
from django.utils import timezone
from django.urls import reverse


class ToDoItem(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ["pub_date"]