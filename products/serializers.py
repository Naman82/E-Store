from rest_framework import serializers
from .models import Product,Category,Discount,Inventory

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields="__all__"

class ProductEditSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        exclude = ['discount_id','inventory_id','category_id']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields="__all__"

class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Inventory
        fields="__all__"

class DiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model=Discount
        fields="__all__"
