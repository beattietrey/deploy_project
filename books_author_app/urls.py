from django.urls import path     
from . import views

urlpatterns = [

    # display
    path('', views.index),	   
    path('books/<int:id>', views.book_info),
    path('authors', views.authors),
    path('authors/<int:id>', views.author_info),

    # action
    path('add_book', views.add_book),
    path('add_author', views.add_author),
    path('book_to_author/<int:author_id>', views.book_to_author),
    path('author_to_book/<int:book_id>', views.author_to_book),

] 