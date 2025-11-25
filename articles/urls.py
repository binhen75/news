from django.contrib import admin
from django.urls import path, include

from .views import ArticleListView, ArticleDetailView, ArticleUpdateView, ArticleDeleteView, ArticleCreateView

urlpatterns = [
    path("", ArticleListView.as_view(), name="article_list"),
    path("<int:pk>/", ArticleDetailView.as_view(), name="article_detail"), # new
    path("<int:pk>/edit/", ArticleUpdateView.as_view(),name="article_edit"), # new
    path("<int:pk>/delete/", ArticleDeleteView.as_view(),name="article_delete"), 
    path("create/", ArticleCreateView.as_view(),name="article_create"), 
]
