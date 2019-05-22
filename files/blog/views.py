from django.shortcuts import render
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    ListView,
    DeleteView,
)


# Create your views here.
from .models import Article

class ArticleListView(ListView):
    template_name = 'article_list.html'
    queryset = Article.objects.all() #it looks for a specific template blog/modelname_list.html

