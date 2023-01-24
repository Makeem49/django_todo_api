from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from . import views

urlpatterns = [
    path('', views.hello_world, name='hello_wolrd'),
    path('auth/', obtain_auth_token),
]