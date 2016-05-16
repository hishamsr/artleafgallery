from django.contrib import admin

from .models import Product, Category


class CatogoryInline(admin.TabularInline):
        model = Category
        extra = 5

class ProductAdmin(admin.ModelAdmin):
    inlines = [CatogoryInline]

admin.site.register(Category)
admin.site.register(Product, ProductAdmin)