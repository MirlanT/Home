from django.contrib import admin
from .models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'phone', 'description', 'category', 'count', 'price']
    list_filter = ['category']
    search_fields = ['phone', 'category']
    fields = ['phone', 'description', 'category', 'count', 'price']
    list_display_links = ['id', 'phone', 'category']


admin.site.register(Product, ProductAdmin)
