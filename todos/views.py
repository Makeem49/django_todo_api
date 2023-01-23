from django.shortcuts import render
from django.http import JsonResponse
from django.forms.models import model_to_dict
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import TodoSerializer

from .models import Todo
# Create your views here.

@api_view(['GET'])
def get_todo(request):
    """
    DRF views
    """
    instance = Todo.objects.all().order_by("?").first()

    data = {}
    if instance:
        # serializing to dictionary format 
        data = TodoSerializer(instance).data

        
    return Response(data) # converting to json format and send o client 


@api_view(['POST'])
def create_todo(request):
    """DRF view"""
    serializer = TodoSerializer(data=request.data)

    if serializer.is_valid():
        instance = serializer.save()
        # data = request.data
        print(serializer)
        return Response(serializer.data)
    return Response({"message" : "invalid data"})