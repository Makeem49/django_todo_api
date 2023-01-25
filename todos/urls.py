from django.urls import path

from . import views

urlpatterns = [
    path('<int:pk>/', views.TodoDetailAPIView.as_view(), name='todo-detail'),
    path('<int:pk>/update/', views.TodoUpdateAPIView.as_view(), name='todo-edit'),
    path('<int:pk>/delete/', views.TodoDeleteAPIView.as_view(), name='todo-delete'),
    path('create/', views.TodoCreateAPIView.as_view(), name='todo-create'),
    path('', views.TodoListAPIView.as_view(), name='todo-list'),
    path('create_or_get/', views.TodoListCreateAPIView().as_view(), name='both')
]