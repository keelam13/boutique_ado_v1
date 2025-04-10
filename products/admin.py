from django.contrib import admin
from .models import Category, Product

class ProductAdmin(admin.ModelAdmin):
    """Admin interface for Product model."""
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'rating',
        'image',
    )

    ordering = ('sku',)

class CategoryAdmin(admin.ModelAdmin):
    """Admin interface for Category model."""
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
