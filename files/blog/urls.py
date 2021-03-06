from django.urls import path
from .views import (
    ArticleListView,
    ArticleDetailView,
)

app_name = 'articles'
urlpatterns = [
    path('',ArticleListView.as_view() ,name = 'article-list'),#a class based view
    path('<int:pk',ArticleDetailView.as_view(),name = 'article')

]