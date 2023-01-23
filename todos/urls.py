from django.urls import path

from . import views

urlpatterns = [
    path('<int:pk>/', views.TodoMixinsViews.as_view(), name='get_todo'),
    path('<int:pk>/update/', views.TodoMixinsViews.as_view(), name='get_todo'),
    path('<int:pk>/delete/', views.TodoMixinsViews.as_view(), name='get_todo'),
    path('create/', views.TodoMixinsViews.as_view(), name='creat_todo'),
    path('', views.TodoMixinsViews.as_view(), name='todos'),
    path('create_or_get/', views.TodoListCreateAPIView().as_view(), name='both')
]