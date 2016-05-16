
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):              
        return self.name

    class Meta:
        ordering = ["name"]
        verbose_name_plural = "Products"
    
class Category(models.Model):
    name = models.CharField(max_length=200, unique=True)
    product = models.ForeignKey(Product, related_name='categories')

    def __str__(self):             
        return self.name

    class Meta:
        ordering = ["name"]
        verbose_name_plural = "Categories"