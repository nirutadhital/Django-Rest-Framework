from django.shortcuts import render
from django.http import JsonResponse
import json


# Create your views here.

def api_home(request, *args, **kwargs):
    #request-> httpRequest->django
    #print(dir(request))
    #request.body
    print(request.GET)
    print(request.POST)
    body=request.body
    data={}#dict
    try:
        data=json.loads(body)# string of json data to python dict
    except:
        pass
    print(data.keys())
    # data['headers']=request.headers  #request.META-->
    data['params']=dict(request.GET)
    print(request.headers)
    data['headers']=dict(request.headers)
    data['content_type']=request.content_type
    return JsonResponse(data)
    # return JsonResponse({"message":"hi, there this is Niruta"})
