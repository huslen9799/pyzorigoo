from django.contrib import admin
from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name', 'slug')
    prepopulated_fields = {
        'slug': ('category_name',)
    }


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'product_name',
        'slug',
        'category',
        'price',
        'stock',
        'is_available'
    )

    prepopulated_fields = {
        'slug': ('product_name',)
    }