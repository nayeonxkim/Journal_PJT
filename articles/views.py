from django.shortcuts import render, redirect
from .forms import ArticleForm
from .models import Article

# Create your views here.
def index(request):
    articles = Article.objects.all()
    context ={'articles':articles}
    return render(request, 'articles/index.html', context)



def create(request):
    if request.method == 'GET':
        form = ArticleForm()
        
    else:
        form = ArticleForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('articles:index')

    context = {'form':form}
    return render(request, 'articles/create.html', context)



def detail(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    context = {'article':article}
    return render(request, 'articles/detail.html', context)



def update(request, article_pk):

    article = Article.objects.get(pk=article_pk)

    if request.method == 'GET':
        form = ArticleForm(instance=article)
        
    else:
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles:detail', article_pk)
        
    context = {'form': form}
    return render(request, 'articles/update.html', context)
    

def delete(request, article_pk):

    article = Article.objects.get(pk=article_pk)
    article.delete()

    return redirect('articles:index')


