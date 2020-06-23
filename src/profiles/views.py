from django.shortcuts import render
from django.http import HttpResponse
from .models import Profile

import datetime
# Create your views here.

def current_datetime(request):
    now = datetime.datetime.now()
    html =  "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

def test_view(request):
    template = 'profiles/test.html'

    if request.user.is_authenticated:
        user = request.user
        profile = Profile.objects.filter(user=user).first()
        
    else:
        profile = 'None'
    context = {'user':profile}
    return render(request,template,context)