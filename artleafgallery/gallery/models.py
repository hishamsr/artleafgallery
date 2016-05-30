
from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    name = models.CharField(max_length=200, unique=True)
    description = models.TextField()
    slider_image = models.ImageField(upload_to="slider")
    homepage_list_icon = models.ImageField(upload_to="homepage_list")

    def __str__(self):              
        return self.name

    class Meta:
        ordering = ["name"]
        verbose_name_plural = "Products"
    
class Category(models.Model):
    name = models.CharField(max_length=200, unique=True)
    product = models.ForeignKey(Product, related_name='categories')
    description = models.TextField()
    
    def __str__(self):             
        return self.name

    class Meta:
        ordering = ["name"]
        verbose_name_plural = "Categories"

class Artist(models.Model):
    user = models.ForeignKey(User)

    def __str__(self):             
        return self.user.first_name

class Frame(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="frames")

    def __str__(self):             
        return self.name

def content_file_name(instance, filename):
    return '/'.join(['media', instance.product.name,filename])

class ArtImage(models.Model):
    artist = models.ForeignKey(Artist)
    product = models.ForeignKey(Product)
    category = models.ForeignKey(Category)
    image = models.ImageField(upload_to=content_file_name)
    frames = models.ManyToManyField(Frame, related_name="frames")

    def __str__(self):             
        return self.product.name + "-" + self.artist.user.first_name + self.image.path

    class Meta:
        
        verbose_name_plural = "Art Works"
