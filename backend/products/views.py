from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer
from django.shortcuts import get_object_or_404
# from django.http import Http404



class ProductCreateAPIView(generics.CreateAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    
    def perform_create(self, serializer):
        title=serializer.validated_data.get('title')
        content=serializer.validated_data.get('content') or None
        if content is None:
            content=title
        serializer.save(content=content)
        # send a Django signal
          
product_create_view=ProductCreateAPIView.as_view()
    


class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    #lookuop_field='pk

product_detail_view=ProductDetailAPIView.as_view()



# Listing objects: It allows you to retrieve a list of all objects from a queryset.
# Creating objects: It allows you to create a new object in the database.
# It is a combination of ListAPIView and CreateAPIView.
class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    
    def perform_create(self, serializer):
        title=serializer.validated_data.get('title')
        content=serializer.validated_data.get('content') or None
        if content is None:
            content=title
        serializer.save(content=content)
        
    
product_list_create_view=ProductListCreateAPIView.as_view()


# class ProductListAPIView(generics.ListAPIView):
#     '''
#     Not gonna use this method
#     '''
#     queryset=Product.objects.all()
#     serializer_class=ProductSerializer
    
# product_list_view=ProductListAPIView.as_view()

    


@api_view(['GET','POST'])
def product_alt_view(request, pk=None, *args, **kwargs):
    method=request.method
    
    if method=="GET":
        if pk is not None:
            # detail view
            obj=get_object_or_404(Product, pk=pk)#
            data=ProductSerializer(obj, many=False).data        
            return Response(data)
        #url_args??
        # get request ->detail view
        # list view
        queryset=Product.objects.all()
        data=ProductSerializer(queryset, many=True).data
        return Response(data)
    
    if method=="POST":
        serializer=ProductSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            title=serializer.validated_data.get('title')
            content=serializer.validated_data.get('content') or None
            if content is None:
                content=title
            serializer.save(content=content)
        return Response(serializer.data)
    return Response({"invalid":"not good data"},status=400)

   
    
    
