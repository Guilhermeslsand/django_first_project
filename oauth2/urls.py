from django.urls import path
from oauth2.views import oauth,members

urlpatterns = [
    path('oauth', oauth, name='oauth'),
    path('members', members, name='members')
]