from django.contrib import admin

from webapp.models import Article


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'author']
    list_filter = ['author']
    search_fields = ['title', 'content']
    fields = ['title', 'author', 'content']
    readonly_fields = ['create_at', 'update_at']

admin.site.register(Article,ArticleAdmin)
