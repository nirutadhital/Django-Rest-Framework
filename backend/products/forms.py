from django import froms
from .models import Product

class productForm (forms.ModelForm):  
    class Meta:
        model = Product
        fields = [
            'title',
            'content',
            'price'
        ]
