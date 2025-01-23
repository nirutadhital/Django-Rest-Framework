from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
import json
from products.models import Product
from django.forms.models import model_to_dict


# Create your views here.

def api_home(request, *args, **kwargs):
    model_data=Product.objects.all().order_by("?").first()
    data={}
    if model_data:
        # data['id']=model_data.id
        # data['title']=model_data.title
        # data['content']=model_data.content
        # data['price']=model_data.price
        data=model_to_dict(model_data, fields=['id','price'])
        return JsonResponse(data)
        # print(data)
        # data=dict(data)
        # json_data_str=json.dumps(data)
        
        
        # model instance (model_data)
        # turn a python dict
        # return json to my client
        
    #request-> httpRequest->django
    #print(dir(request))
    #request.body
    # print(request.GET)
    # print(request.POST)
    # body=request.body
    # data={}#dict
    # try:
    #     data=json.loads(body)# string of json data to python dict
    # except:
    #     pass
    # print(data.keys())
    # # data['headers']=request.headers  #request.META-->
    # data['params']=dict(request.GET)
    # print(request.headers)
    # data['headers']=dict(request.headers)
    # data['content_type']=request.content_type
    return HttpResponse(json_data_str, headers={"content-type":"application/json"})
    # return JsonResponse({"message":"hi, there this is Niruta"})
