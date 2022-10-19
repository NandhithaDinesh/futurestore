from rest_framework.serializers import ModelSerializer
from owner.models import Carts, Categories,Orders, Products
from rest_framework import serializers

class CartSerializer(ModelSerializer):
    user=serializers.CharField(read_only=True)
    class Meta:
        model=Carts
        fields="__all__"
    def create(self, validated_data):
        user=self.context.get("user")
        return Carts.objects.create(**validated_data,user=user)

class OrderSerializer(ModelSerializer):
    user=serializers.CharField(read_only=True)
    class Meta:
        model=Orders
        fields="__all__"
    def create(self, validated_data):
        user=self.context.get("user")
        return Orders.objects.create(**validated_data,user=user)

class ProductSerializer(ModelSerializer):
    
    class Meta:
        model=Products
        fields="__all__"
    def create(self, validated_data):
        product_name=self.context.get("product_name")
        return Products.objects.create(**validated_data,product_name=product_name)

class CategorySerializer(ModelSerializer):
    
    class Meta:
        model=Categories
        fields="__all__"
    def create(self, validated_data):
        category_name=self.context.get("category_name")
        return Categories.objects.create(**validated_data,category_name=category_name)