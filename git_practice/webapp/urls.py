from django.urls import path

from webapp.views import index_view, article_view, article_add

urlpatterns = [
    path('', index_view),
    path('article/', article_view),
    path('article/add/', article_add)
]
