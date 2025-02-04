# handle the conversion between Python objects (e.g., querysets) and JSON/XML for API responses.
# it converts models into dict

from rest_framework import serializers
from rest_framework.reverse import reverse
from products.models import Product
from .import validators

class ProductSerializer(serializers.ModelSerializer):  
    my_discount=serializers.SerializerMethodField(read_only=True)
    edit_url=serializers.SerializerMethodField(read_only=True)
    url=serializers.HyperlinkedIdentityField(
        view_name='product-detail',
        lookup_field='pk'
    )
    title=serializers.CharField(validators=[validators.validate_title_no_hello, validators.unique_product_title])
    # name=serializers.CharField(source='title',read_only=True)
    # email=serializers.EmailField(write_only=True)
    class Meta:
        model = Product
        fields = [
            'user',
            'url',
            'edit_url',
            # 'email',
            'pk',
            'title',
            # 'name',
            'content',
            'price',
            'sale_price',
            'my_discount',
        ]
    
    # def validate_title(self, value):
    #     request=self.context.get('request')
    #     user=request.user
    #     qs=Product.objects.filter(user=user, title__iexact=value)
    #     if qs.exists():
    #         raise serializers.ValidationError(f"{value} is already a product name")
    #     return value
    
    # def create(self, validated_data):
    #     email=validated_data.pop('email')
    #     obj=super().create(validated_data)
    #     print(email, obj)
    #     return obj
    
    # def update(self, instance, validated_data):
    #     email=validated_data.pop('email')
    #     print(email)
    #     return super().create(validated_data)
        
    def get_edit_url(self, obj):
        request = self.context.get('request') # self.request
        if request is None:
            return None
        return reverse("product-edit", kwargs={"pk": obj.pk}, request=request)     
        
        
    def get_my_discount(self, obj):
        if not hasattr(obj,'id'):
            return None
        if not isinstance(obj,Product):
            return None
        # try:
        #     return obj.get_discount()
        # except:
        #     return None
        return obj.get_discount()
            