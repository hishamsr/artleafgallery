
from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets, generics
from gallery.serializers import ProductSerializer, CategorySerializer
from gallery.models import Product, Category
from authentication.permissions import IsAuthenticatedOrCreate


from rest_framework import permissions, routers, serializers, viewsets



class ProductViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.AllowAny,)
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


