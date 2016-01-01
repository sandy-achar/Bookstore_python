from django.conf.urls import url
from book.views import index_books, search_books, search_test, register_user, login_user, logout_user

urlpatterns = [
    url(r'^$', index_books, name="index_books"),
    url(r'^search/(?P<category>\w+)/(?P<name>[\w|\W]+)/$', search_books, name='search_book'),
    url(r'^search/$', search_test, name='search_test'),
    url(r'^register/$', register_user, name='register_user'),
    url(r'^login/$', login_user, name="login_user"),
    url(r'^logout/$', logout_user, name="logout_user"),
]
