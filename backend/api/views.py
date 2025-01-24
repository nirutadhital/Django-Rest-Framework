from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
import json
from products.models import Product
from django.forms.models import model_to_dict
from rest_framework.response import Response
from rest_framework.decorators import api_view
from products.serializers import ProductSerializer


@api_view(["POST"])
def api_home(request, *args, **kwargs):
    """
    DRF API View
    """
    # if request.method!="POST":
    #     return Response ({"detail":"GET not allowed"}, status=400)
    serializer=ProductSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        instance=serializer.save()
        print(instance)
        return Response(serializer.data)
    return Response({"invalid":"not good data"},status=400)
