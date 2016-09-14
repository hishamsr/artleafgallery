
from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets, generics
from gallery.serializers import ProductSerializer, CategorySerializer, CompanySerializer, ArtImageSerializer
from gallery.models import Product, Category, Company, Artist, Frame, ArtImage
from authentication.permissions import IsAuthenticatedOrCreate


from rest_framework import permissions, routers, serializers, viewsets, pagination


class ProductViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.AllowAny,)
    queryset = Product.objects.all().order_by('order')
    serializer_class = ProductSerializer
    pagination_class = None


class CompanyViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.AllowAny,)
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class ArtWorkList(generics.ListAPIView):
    serializer_class = ArtImageSerializer
    def get_queryset(self):
        
        product_id = self.kwargs['product_id']
        color = self.request.query_params.get('color', None)
        query = ""
        if color:
            color = "#"+color
            if 'category_id' in self.kwargs:
                category_id = self.kwargs['category_id']
                query = ArtImage.objects.filter(product__id=product_id, category__id=category_id, color=color)
            else:
                query = ArtImage.objects.filter(product__id=product_id, color=color)
        else:
            if 'category_id' in self.kwargs:
                category_id = self.kwargs['category_id']
                query = ArtImage.objects.filter(product__id=product_id, category__id=category_id)
            else:
                query = ArtImage.objects.filter(product__id=product_id)
        return query