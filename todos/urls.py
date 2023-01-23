from django.urls import path

from . import views

urlpatterns = [
    path('<int:pk>/', views.TodoDetailAPIView.as_view(), name='get_todo'),
    path('<int:pk>/update/', views.TodoUpdateAPIView.as_view(), name='get_todo'),
    path('<int:pk>/delete/', views.TodoDeleteAPIView.as_view(), name='get_todo'),
    path('create/', views.TodoCreateAPIView.as_view(), name='creat_todo'),
    path('', views.TodoListAPIView.as_view(), name='todos'),
    path('create_or_get/', views.TodoListCreateAPIView().as_view(), name='both')
]