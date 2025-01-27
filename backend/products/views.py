from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer



class ProductCreateAPIView(generics.CreateAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    
    
    def perform_create(self, serializer):
        # serializer.save(user=self.request.user)
        # print(serializer.validated_data)
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


class ProductListAPIView(generics.ListAPIView):
    '''
    Not gonna use this method
    '''
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    
product_list_view=ProductListAPIView.as_view()

    




    
