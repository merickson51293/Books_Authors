from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('author', views.author),
    path('add_book', views.add_book),
    path('add_author', views.add_author),
    path('book_desc.html/<int:book_id>', views.book_desc),
    path('author_desc.html/<int:author_id>', views.author_desc),
]