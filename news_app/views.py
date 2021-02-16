from django.shortcuts import render

from news_app.models import Author, News

def index(request):
    data = News.objects.all()
    context = {'data': data}
    return render(request, 'index.html', context)
