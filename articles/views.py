from django.views.generic import ListView
from django.shortcuts import render

from articles.models import Article, Scope


def articles_list(request):
    template = 'articles/news.html'
    ordering = '-published_at'
    object_list = Article.objects.all().order_by(ordering)

     
    context = {'object_list': object_list, }

  

    # используйте этот параметр для упорядочивания результатов
    # https://docs.djangoproject.com/en/2.2/ref/models/querysets/#django.db.models.query.QuerySet.order_by
    
    return render(request, template, context)
