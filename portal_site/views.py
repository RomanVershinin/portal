from django.shortcuts import render

# Create your views here.

from news.models import News

def index(request):
    news_vospit = News.objects.filter(section__id=1)[:5]
    news_slujeb = News.objects.filter(section__id=2)[:5]
    if request.user.is_authenticated:
        user_is_auth = True
    else:
        user_is_auth = False
    context = {'news_slujeb':news_slujeb, 'news_vospit':news_vospit, 'user_is_auth':user_is_auth}

    return render(request, 'portal_site/index.html', context)
