#from django.conf.urls import url
from django.urls import re_path
from books import views

urlpatterns = [
    re_path(r'^$', views.BookList.as_view(), name='book_list'),
    re_path(r'^(?P<pk>\d+)/$', views.BookDetail.as_view(), name='book_detail'),
    re_path(r'^add/$', views.AuthorCreateView.as_view(), name='add_author_and_books'),
    re_path(r'^(?P<pk>\d+)/edit/$', views.AuthorUpdateView.as_view(), name='edit_author_and_books'),
    re_path(r'^authors/$', views.AuthorList.as_view(), name='author_list'),
    re_path(r'^authors/(?P<pk>\d+)/$', views.AuthorDetail.as_view(), name='author_detail'),
]
