from django.urls import path

from . import views

app_name = 'todo_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('new', views.create_todo_item, name='create_todo_item'),
    path('update/<int:id>/', views.update_todo_item, name='update_todo_item'),
    path('delete/<int:id>/', views.delete_todo_item, name='delete_todo_item'),
]