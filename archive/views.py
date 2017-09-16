from django.shortcuts import render
from articles.models import Article

def archive(request):
    #grab all articles
    articles = Article.objects.all()

    template = 'archive/archive.html'
    context = {'articles': articles}

    return render(request, template, context)
