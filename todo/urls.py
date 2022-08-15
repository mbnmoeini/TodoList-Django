from django.urls import path
from . import views

urlpatterns = [
    path("", views.ItemListView.as_view(), name="index"),
    path("item/add/",views.createItem,name="add"),
    path("item/delete/<int:pk>/", views.deleteItem, name="delete"),
]
