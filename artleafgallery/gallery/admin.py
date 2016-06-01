from django.contrib import admin

from .models import Product, Category, ArtImage, Artist, Frame, Company

class ArtImageInline(admin.TabularInline):
        model = ArtImage
        extra = 1

class CatogoryInline(admin.TabularInline):
        model = Category
        extra = 0

class CategoryAdmin(admin.ModelAdmin):
    inlines = [ArtImageInline]

class ProductAdmin(admin.ModelAdmin):
    inlines = [CatogoryInline, ArtImageInline]

admin.site.register(Category, CategoryAdmin)
admin.site.register(ArtImage)
admin.site.register(Artist)
admin.site.register(Frame)
admin.site.register(Company)
admin.site.register(Product, ProductAdmin)