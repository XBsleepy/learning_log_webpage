from django.urls import path

from . import views
app_name = 'dairy'
urlpatterns = [
    path("dairy_list/", views.dairy_list, name='dairy_list'),
    path("add_dairy/", views.add_dairy, name='add_dairy'),
]
