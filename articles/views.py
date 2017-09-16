from django.shortcuts import render
from .models import Article

def article(request, slug):
    #find the article that corresponds with the slug
    article = Article.objects.get(slug=slug)

    template = "articles/%s" % (article.template)
    context = {'article': article}

    return render(request, template, context)
