from django.shortcuts import render
from django.http import JsonResponse
from django.forms.models import model_to_dict

from .models import Todo
# Create your views here.


def create_todo(request):
    """The process of converting a model instance 
    to a dictionary and later to json format is called serialization. 
    """
    model_instance = Todo.objects.all().order_by("?").first()

    data = {}
    if model_instance:
        # serializing to dictionary format 
        data = model_to_dict(model_instance, fields=['name', 'created_at'])

        
    return JsonResponse(data) # converting to json format and send o client 