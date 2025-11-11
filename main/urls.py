from django.urls import path
from .views import AuthorListCreateView, AuthorDetailView, BookListCreateView, BookDetailView, ArticleListCreateView, ArticleDetailView

urlpatterns = [
    path("authors/", AuthorListCreateView.as_view()),
    path("authors/<int:pk>/", AuthorDetailView.as_view()),
    path("books/", BookListCreateView.as_view()),
    path("books/<int:pk>/", BookDetailView.as_view()),
    path("articles/", ArticleListCreateView.as_view()),
    path("articles/<int:pk>/", ArticleDetailView.as_view()),
]
