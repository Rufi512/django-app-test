from .models import Product
from clients.models import Customer
from clients.serializers import CustomerProductSerializer
from rest_framework import serializers


class ProductSerializer(serializers.ModelSerializer):
    seller = CustomerProductSerializer(read_only=True)
    
    class Meta:
        model = Product
        fields = ('id','title','description','seller','price','image','avalaible')