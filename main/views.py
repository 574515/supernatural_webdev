from django.shortcuts import render
from django.http import HttpResponse
from account.models import Account
from blog.models import BlogPost, Comment


def IndexView(request):
    context = {}
    users = Account.objects.all()
    allposts = BlogPost.objects.all()
    published_posts = BlogPost.objects.filter(published=True).all()
    unpublished_posts = BlogPost.objects.filter(published=False).all()
    comments = Comment.objects.all()
    context = {
        'navbar': 'index',
        'users': users,
        'blog_posts': allposts,
        'pub_posts': published_posts,
        'unpub_posts': unpublished_posts,
        'comments': comments,
        }
    return render(request, 'main/index.html', context)


def QuizGameView(request):
    context = {}
    users = Account.objects.all()
    context = {
        'users': users,
        }
    return render(request, 'main/quiz_game.html', context)