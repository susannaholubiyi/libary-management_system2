from django.urls import path

from libraryManagementApp import views

urlpatterns = [
    path('view_all', views.view_all_books),
    path('book_details/', views.book_details, name='book_details')
]