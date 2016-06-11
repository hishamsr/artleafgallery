
from rest_framework import serializers
from gallery.models import Product, Category, Artist, Company, Frame, ArtImage
from authentication.serializers import UserSerializer

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ('id', 'name', 'description')


class ProductSerializer(serializers.ModelSerializer):

    categories= CategorySerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ('id', 'name', 'categories', 'description', 'homepage_list_icon', 'slider_image')



class FrameSerializer(serializers.ModelSerializer):

    class Meta:
        model = Frame

class ArtistSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Artist

class CompanySerializer(serializers.ModelSerializer):

    class Meta:
        model = Company

class ArtImageSerializer(serializers.ModelSerializer):

    frames = FrameSerializer(many=True, read_only=True)
    artist = ArtistSerializer(read_only=True)

    class Meta:
        model = ArtImage