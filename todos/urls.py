from django.urls import path

from . import views

urlpatterns = [
    path('', views.get_todo, name='get_todo'),
    path('create/', views.create_todo, name='create_todo'),
]