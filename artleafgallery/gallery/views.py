
from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets, generics
from gallery.serializers import ProductSerializer, CategorySerializer, CompanySerializer
from gallery.models import Product, Category, Company, Artist, Frame, ArtImage
from authentication.permissions import IsAuthenticatedOrCreate


from rest_framework import permissions, routers, serializers, viewsets



class ProductViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.AllowAny,)
    queryset = Product.objects.all().order_by('order')
    serializer_class = ProductSerializer


class CompanyViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.AllowAny,)
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
