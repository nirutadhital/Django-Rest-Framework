from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics, mixins #, permissions, authentication
from .models import Product
from .serializers import ProductSerializer
from django.shortcuts import get_object_or_404
from .permissions import IsStaffEditorPermission
# from api.authentication import TokenAuthentication
from api.mixins import (StaffEditorPermissionMixin, UserQuerySetMixin)
# from django.http import Http404
from .custompagination import CustomLimitOffsetPagination




class ProductCreateAPIView(generics.CreateAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    
    def perform_create(self, serializer):
        title=serializer.validated_data.get('title')
        content=serializer.validated_data.get('content') or None
        if content is None:
            content=title
        serializer.save(content=content)
          
product_create_view=ProductCreateAPIView.as_view()
    


class ProductDetailAPIView(UserQuerySetMixin,StaffEditorPermissionMixin,generics.RetrieveAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    #lookuop_field='pk

product_detail_view=ProductDetailAPIView.as_view()


class ProductUpdateAPIView(UserQuerySetMixin,StaffEditorPermissionMixin,generics.UpdateAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    # permission_classes=[permissions.DjangoModelPermissions]
    # permission_classes=[permissions.IsAdminUser, IsStaffEditorPermission]
    #lookuop_field='pk
    lookup_field='pk'
    
    def perform_update(self, serializer):
        instance=serializer.save()
        if not instance.content:
            instance.content=instance.title

product_update_view=ProductUpdateAPIView.as_view()


class ProductDestroyAPIView(UserQuerySetMixin,StaffEditorPermissionMixin,generics.DestroyAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    # permission_classes=[permissions.IsAdminUser, IsStaffEditorPermission]
    #lookuop_field='pk
    lookup_field='pk'
    
    def perform_destroy(self, instance):
        #instance
        super().perform_destroy(instance)
        

product_destroy_view=ProductDestroyAPIView.as_view()


# Listing objects: It allows you to retrieve a list of all objects from a queryset.
# Creating objects: It allows you to create a new object in the database.
# It is a combination of ListAPIView and CreateAPIView.
class ProductListCreateAPIView(UserQuerySetMixin,StaffEditorPermissionMixin,generics.ListCreateAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    # authentication_classes=[authentication.SessionAuthentication, TokenAuthentication]
    # permission_classes=[permissions.IsAdminUser, IsStaffEditorPermission]
    pagination_class=CustomLimitOffsetPagination
    
    
    def perform_create(self, serializer):
        # email=serializer.validated_data.pop('email')
        # print(email)
        title=serializer.validated_data.get('title')
        content=serializer.validated_data.get('content') or None
        if content is None:
            content=title
        serializer.save(user=self.request.user,content=content)
        
        
    # def get_queryset(self, *args, **kwargs):
    #     qs = super().get_queryset(*args, **kwargs)
    #     request = self.request
    #     user = request.user
    #     if not user.is_authenticated:
    #         return Product.objects.none()
    #     # print(request.user)
    #     return qs.filter(user=request.user)
    
product_list_create_view=ProductListCreateAPIView.as_view()


# class ProductListAPIView(generics.ListAPIView):
#     '''
#     Not gonna use this method
#     '''
#     queryset=Product.objects.all()
#     serializer_class=ProductSerializer
    
# product_list_view=ProductListAPIView.as_view()

 
 
#class based view set in drf
class ProductMixinview(mixins.CreateModelMixin,mixins.ListModelMixin,mixins.RetrieveModelMixin, generics.GenericAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    lookup_field='pk'
    
    def get(self, request, *args, **kwargs):
        print(args, kwargs)
        pk=kwargs.get('pk')
        if pk is not None:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
    def perform_create(self, serializer):
        title=serializer.validated_data.get('title')
        content=serializer.validated_data.get('content') or None
        if content is None:
            content="This is the single view doing cool stuffs"
        serializer.save(content=content)
        
    
product_mixin_view=ProductMixinview.as_view()
 
 
    


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

   
    
    
