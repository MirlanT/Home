from django.contrib import admin
from .models import Article


class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'phone', 'description', 'category', 'count', 'price']
    list_filter = ['phone']
    search_fields = ['phone', 'category']
    fields = ['phone', 'description', 'category', 'count', 'price']
    list_display_links = ['id', 'phone', 'category']


admin.site.register(Article, ProductAdmin)
