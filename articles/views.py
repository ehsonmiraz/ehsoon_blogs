from django.shortcuts import render, redirect
from django.http import  HttpResponse
from django.contrib.auth.decorators import login_required

from .forms import CreatePost
from .models import Article
# Create your views here.
def articles_list(request):
    articles_list=Article.objects.all().order_by('date')
    print(len(articles_list))
    context={
        'articles_list': articles_list,
        'title': 'blogs list'
    }
    return render(request,'articles/index.html',context=context)

def articles_detail(request,slug):
    article=Article.objects.get(slug=slug)
    return render(request,'articles/post.html',{'article':article})

@login_required(login_url="accounts:login")
def create_post(request):
    if request.method == 'POST':
        form = CreatePost(request.POST,request.FILES)
        if form.is_valid():
            # article_instance = form.save(commit=False)
            # article_instance.author = request.user
            # article_instance.save()
            print("valid")
            return redirect("article:list")
        else:
            print("invalid")
    else:
         form=CreatePost()
    return render(request,'articles/createpost.html',{'form':form})