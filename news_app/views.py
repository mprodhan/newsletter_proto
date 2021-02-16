from django.shortcuts import render, reverse, HttpResponseRedirect

from news_app.models import Author, News
from news_app.forms import NewsAddForm, AuthorAddForm

def index(request):
    data = News.objects.all()
    context = {'data': data}
    return render(request, 'index.html', context)


def newsadd(request):
    html = "newsaddform.html"
    if request.method == "POST":
        form = NewsAddForm(request.POST)
        # form.is_valid, validates the form
        if form.is_valid():
            # form.cleaned_data only uses the data that is being requested
            data = form.cleaned_data
            # News from the model is used to then take the model fields and
            # render them.
            News.objects.create(
                title=data['title'],
                body=data['body'],
                author=data['author']
            )
            return HttpResponseRedirect(reverse('homepage'))
    form = NewsAddForm()
    context = {"form": form}
    return render(request, html, context)

# def authoradd(request):
#     html = "authoradd.html"
#     if request.method == "POST":
#         form = AuthorAddForm(request.POST)
#         if form.is_valid():
#             data = form.cleaned_data
#             Author.objects.create(
#                 name=data['name']
#             )
#             return HttpResponseRedirect(reverse('homepage'))
#     form = AuthorAddForm()
#     context = {"form": form}
#     return render(request, html, context)

def authoradd(request):
    html = "authoradd.html"
    if request.method == "POST":
        form = AuthorAddForm(request.POST)
        form.save()
        return HttpResponseRedirect(reverse('homepage'))

    form = AuthorAddForm()
    context = {'form': form}

    return render(request, html, context)


''' Anytime we are looking at detail for lookup, then we need 
an id in addition to request as parameters. '''
def author_detail(request, id):
    html = "author.html"
    author = Author.objects.get(id=id)
    # the author=author means that for author(left), is assigned
    # to author variable listed above.
    articles = News.objects.filter(author=author)
    # body = News.objects.filter(author=author)
    context = {'author': author, 'articles': articles}
    return render(request, html, context)
    # Needs an html page to add between request and context

