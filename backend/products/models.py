from django.db import models
from django.conf import settings
from django.db.models import Q

User=settings.AUTH_USER_MODEL#auth.User

class ProductQuerySet(models.QuerySet):
    def is_public(self):
        return self.filter(public=True)#used to filter only products that are marked as public=True and used django filter method to do this 

    def search(self,query, user=None):#this method perform the search on the produts based on the provided query and operationally filtered by user
        lookup=Q(title__icontains=query) | Q(content__icontains=query)#it creates the Q object that searches for the query in either the title or content, icontains lookup is used to perform case-insensitive search
        qs= self.is_public().filter(lookup)#filters the queryset to include only public products that matches the lookup
        if user is not None:
            qs2= self.filter(user=user).filter(lookup)
            qs=(qs | qs2).distinct()# |-OR operation to filter the distinct result
        return qs
    


class ProductManager(models.Manager):
    def get_queryset(self,*args, **kwargs):# ProductManager overrides the default get_queryset method of the Manager class
        return ProductQuerySet(self.model, using=self._db)#returns ProductQuerySet , which allow to use the custom methods (is_public and search) defined in ProductQuerySet
    
    
    def search(self, query, user=None):# this methos is a convenience method that calls the search method on the ProductQuerySet
        return self.get_queryset().search(query, user=user)# it allow you to perform search directly from the ProductManager


class Product(models.Model):
    # pk
    user = models.ForeignKey(User, default=1, null=True, on_delete=models.SET_NULL)
    title=models.CharField(max_length=120)
    content=models.TextField(blank=True, null=True)
    price=models.DecimalField(max_digits=15, decimal_places=2, default=99.99)
    public=models.BooleanField(default=True)
    
    objects= ProductManager()
    
    
    def is_public(self)->bool:
        return self.public #True or False
    
    @property
    def sale_price(self):
        return "%.2f" %(float(self.price)*0.8)
    
    def get_discount(self):
        return "122"
    
