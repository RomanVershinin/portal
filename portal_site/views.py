from django.shortcuts import render

# Create your views here.
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect

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

def login_view(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        password = request.POST['password']
        username = request.POST['login']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        return render(request, 'portal_site/login.html', {'info':'Вы ввели не правильный пароль, логин или такого пользователя нет!'})

    return render(request, 'portal_site/login.html', {'test': 'isdbvaijfvb aifijnbgna'})

def logout_view(request):
    logout(request)
    return redirect('/login')
