from django.conf.urls import url
from book.views import index_books, search_books, search_test

urlpatterns = [
    url(r'^$', index_books, name="index_books"),
    url(r'^search/(?P<category>\w+)/(?P<name>[\w|\W]+)/$', search_books, name='search_book'),
    url(r'^search/$', search_test, name='search_test'),
]
