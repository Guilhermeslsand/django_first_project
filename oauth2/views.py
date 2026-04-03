from django.shortcuts import render

def oauth(request):
    return render(request, 'oauth2/oauth2.html')