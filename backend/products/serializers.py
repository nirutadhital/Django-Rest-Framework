# handle the conversion between Python objects (e.g., querysets) and JSON/XML for API responses.
# it converts models into dict

from rest_framework import serializers

from products.models import Product

class ProductSerializer(serializers.ModelSerializer):  
    my_discount=serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Product
        fields = [
            'title',
            'content',
            'price',
            'sale_price',
            'my_discount',
        ]
        
        
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
            