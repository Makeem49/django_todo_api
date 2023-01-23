import json 

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.

def hello_world(request):
    body = request.body
    data = {}

    try:
        data = json.loads(body) # -> converting string of json to python dictionary 
    except:
        pass 

    print(request.GET.get('abc'))
    # print(type(request.headers))
    # print(f"query {dict(request.GET)} ")
    # print(json.dumps(request.headers)) # can't be serialize to json because it's not a proper dictionary 

    data['hearders'] = dict(request.headers) # able to convert it to proper dict using dict
    data['query_params'] = dict(request.GET)
    print(data)
    # print(type(data))
    return JsonResponse({"x":"hello wolrd"})