# handle the conversion between Python objects (e.g., querysets) and JSON/XML for API responses.
# it converts models into dict

from rest_framework import serializers
from rest_framework.reverse import reverse

from products.models import Product

class ProductSerializer(serializers.ModelSerializer):  
    my_discount=serializers.SerializerMethodField(read_only=True)
    edit_url=serializers.SerializerMethodField(read_only=True)
    url=serializers.HyperlinkedIdentityField(
        view_name='product-detail',
        lookup_field='pk'
    )
    class Meta:
        model = Product
        fields = [
            'url',
            'edit_url',
            'pk',
            'title',
            'content',
            'price',
            'sale_price',
            'my_discount',
        ]
        
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
            