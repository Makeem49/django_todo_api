from django.urls import path

from . import views

urlpatterns = [
    path('', views.create_todo, name='create_todo')
]