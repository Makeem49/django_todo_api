from django.shortcuts import render
from django.http import JsonResponse

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
        data['name'] = model_instance.name
        data['created_at'] = model_instance.created_at
        data['target_time'] = model_instance.target_time
        data['duration'] = model_instance.duration
        data['start_at'] = model_instance.start_at
        data['completed_at'] = model_instance.completed_at
        data['is_suspended'] = model_instance.is_suspended
        data['is_completed'] = model_instance.is_completed

        
    return JsonResponse(data) # converting to json format and send o client 