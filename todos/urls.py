from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add', views.addTodo, name='add'),
    path('complete/<int:todo_id>', views.completeTodo, name='complete'),
    path('delete/<int:todo_id>', views.deleteTodo, name='delete'),
]
