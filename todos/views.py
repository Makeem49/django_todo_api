from django.shortcuts import render
from django.http import JsonResponse
from django.forms.models import model_to_dict
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Todo
# Create your views here.

@api_view(['GET'])
def create_todo(request):
    """The process of converting a model instance 
    to a dictionary and later to json format is called serialization. 
    """
    model_instance = Todo.objects.all().order_by("?").first()

    data = {}
    if model_instance:
        # serializing to dictionary format 
        data = model_to_dict(model_instance, fields=['name', 'created_at'])

        
    return Response(data) # converting to json format and send o client 