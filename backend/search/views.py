from rest_framework import generics
from products.models import Product
from products.serializers import ProductSerializer


class SearchListView(generics.ListAPIView):
    queryset = Product.objects.all()#default QuerySet is all products
    serializer_class = ProductSerializer# serializer is used to convert queryset to json
    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)
        q = self.request.GET.get('q')#It retrieves the search query (q) from the request's GET parameters.
        results = Product.objects.none()#initializes empty
        if q is not None:
            user = None
            if self.request.user.is_authenticated:
                user = self.request.user
            results = qs.search(q, user=user)
        return results