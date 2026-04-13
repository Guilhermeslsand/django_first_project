from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def oauth(request):
    return render(request, 'oauth2/oauth2.html')

@login_required
def members(request):
    return render(request,'oauth2/members.html')