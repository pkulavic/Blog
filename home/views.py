from django.shortcuts import render
from articles.models import Article

def home(request):
    #grab the latest article from the DB
    l = Article.objects.latest('created')

    template = 'home/home.html'
    context = {'l': l}

    return render(request, template, context)
