from django.urls import path

from todoapp import views

urlpatterns = [
    path('', views.Dashboard.as_view(), name='index'),
    path('get_todo_list', views.gettodolist, name='get_todo_list')
]