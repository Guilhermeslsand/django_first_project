from django.urls import path
from oauth2.views import oauth

urlpatterns = [
    path('oauth', oauth, name='oauth'),
]