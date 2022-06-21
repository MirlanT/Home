from django.urls import path
from webapp.views import index_view, create_article, index_view10


urlpatterns = [
    path('', index_view),
    path('articles/', create_article),
    path('articles/start/', index_view10),
]
