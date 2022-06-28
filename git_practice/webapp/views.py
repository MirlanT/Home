from django.shortcuts import render
from webapp.models import Article


def index_view(request):
    articles = Article.objects.all()
    context = {
        'articles': articles
    }
    return render(request, 'index.html', context)


def article_view(request):
    article_id = request.GET.get('pk')
    article = Article.objects.get(pk=article_id)
    context = {
        'article': article
    }
    return render(request, 'article.html', context)


def article_add(request):
    if request.method == 'GET':
        return render(request, 'create.html')
    else:
        title = request.POST.get('title')
        content = request.POST.get('content')
        author = request.POST.get('author')
        article = Article.objects.create(title=title, content=content, author=author)
        # context = {
        #     'article': article
        # }
        return render(request, 'article.html', context={'article': article})
