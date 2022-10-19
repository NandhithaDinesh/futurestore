from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from api.serializers import CartSerializer,OrderSerializer,ProductSerializer, CategorySerializer
from rest_framework.response import Response
from owner.models import Carts, Categories,Orders, Products
from rest_framework import authentication,permissions
class CartView(ModelViewSet):
    queryset = Carts.objects.all()
    serializer_class = CartSerializer
    authentication_classes = [authentication.BasicAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    def get_queryset(self):
        return Carts.objects.filter(user=self.request.user)

    def create(self, request, *args, **kwargs):
        serializer=CartSerializer(data=request.data,context={"user":request.user})
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)

class OrderView(ModelViewSet):
    queryset = Orders.objects.all()
    serializer_class = OrderSerializer
    authentication_classes = [authentication.BasicAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    def get_queryset(self):
        return Orders.objects.filter(user=self.request.user)

    def create(self, request, *args, **kwargs):
        serializer=CartSerializer(data=request.data,context={"user":request.user})
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)

class ProductView(ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer
    authentication_classes = [authentication.BasicAuthentication]
    permission_classes = [permissions.IsAuthenticated]

class CategoryView(ModelViewSet):
    queryset = Categories.objects.all()
    serializer_class = CategorySerializer
    authentication_classes = [authentication.BasicAuthentication]
    permission_classes = [permissions.IsAuthenticated]