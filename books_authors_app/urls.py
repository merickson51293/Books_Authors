from django.urls import path

from . import views

urlpatterns = [
    path('', views.home),
    path('book', views.book),
    path('author', views.author),
    path('add_book', views.add_book),
    path('add_author', views.add_author),
    path('book_desc.html/<int:book_id>', views.book_desc),
    path('author_desc.html/<int:author_id>', views.author_desc),
    path('author/<int:author_id>/assign', views.assign_author),
    path('book/<int:book_id>/assign', views.assign_book),
]