from turtle import title
from django.views.generic import ListView
from .models import ToDoItem
from django.utils import timezone
from django.urls import reverse
from django.http import HttpResponseRedirect


class ItemListView(ListView):
    model = ToDoItem
    template_name = 'todo/index.html'

    def get_queryset(self):
        return ToDoItem.objects.all().order_by('-pub_date')


def createItem(request):
    title = request.POST.get("content")
    ToDoItem.objects.create(title=title)
    return HttpResponseRedirect(reverse("index"))

def deleteItem(request, pk):
    ToDoItem.objects.get(id=pk).delete()
    return HttpResponseRedirect(reverse("index"))
