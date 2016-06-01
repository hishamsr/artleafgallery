
from rest_framework import serializers
from gallery.models import Product, Category, Artist, Company, Frame, ArtImage

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ('id', 'name', 'description')


class ProductSerializer(serializers.ModelSerializer):

    categories= CategorySerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ('id', 'name', 'categories', 'description', 'homepage_list_icon', 'slider_image')

class ArtistSerializer(serializers.ModelSerializer):

    class Meta:
        model = Artist

class FrameSerializer(serializers.ModelSerializer):

    class Meta:
        model = Frame

class CompanySerializer(serializers.ModelSerializer):

    class Meta:
        model = Company

class ArtImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = ArtImage