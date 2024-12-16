from django.urls import path
from . import views

urlpatterns = [
    path('', views.author_list, name='home'), 
    path('authors/', views.author_list, name='author-list'),
    path('books/', views.book_list, name='book-list'),
    path('reviews/', views.review_list, name='review-list'),
]
