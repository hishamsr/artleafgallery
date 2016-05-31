
from rest_framework import serializers
from gallery.models import Product, Category

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ('id', 'name', 'description')


class ProductSerializer(serializers.ModelSerializer):

    categories= CategorySerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ('id', 'name', 'categories', 'description', 'homepage_list_icon', 'slider_image')
