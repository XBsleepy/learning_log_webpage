from django.urls import path
from . import views
from .views import toggle_complete
app_name = 'todolist'
urlpatterns = [
    path('', views.list_todo, name='list_todo'),
    path('add_todo/', views.add_todo, name='add_todo'),
    path('toggle_complete/<int:task_id>/', toggle_complete, name='toggle_complete'),
   
]
