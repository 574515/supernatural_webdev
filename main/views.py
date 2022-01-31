from itertools import count
import json
from django.http import Http404, JsonResponse
from django.shortcuts import render
from account.models import Account
from blog.models import BlogPost, Comment
from django.db.models import Count


def IndexView(request):
	comments = Comment.objects.all()
	users = Account.objects.all()
	posts = BlogPost.objects.filter(published=True).all()
	if request.user.is_authenticated:
		sort_by = request.POST.get('value')
		if sort_by:
			if request.method == "POST" and is_ajax(request):
				sort_strategy = defaultOrder
				if sort_by == '1':
					sort_strategy = defaultOrder
				if sort_by == '2':
					sort_strategy = orderByCommentsDesc
				if sort_by == '3':
					sort_strategy = orderByCommentsAsc
				if sort_by == '4':
					sort_strategy = orderByLikesDesc
				if sort_by == '5':
					sort_strategy = orderByLikesAsc
				posts = BlogPost.objects.filter(published=True).all()
				sortedPosts = sort_strategy(posts)
				seralized_posts = []
				for post in sortedPosts:
					seralized_posts.append(post.kakoGod())
				seralized_posts.append(seralized_posts.__len__())
				return JsonResponse(json.dumps(seralized_posts), status=200, safe=False)
		else:
			return render(request, 'main/index.html', {})
	else:		
		context = {
			'navbar': 'index',
			'comments': comments,
			'users': users,
			'posts': posts,
			}
		return render(request, 'main/index.html', context)


def defaultOrder(posts):
	posts = list(posts)
	posts.sort(key=lambda x: x.pub_date, reverse=True)
	return list(posts)


def orderByLikesAsc(posts):
	posts = list(posts)
	posts.sort(key=lambda x: x.likes)
	return posts


def orderByLikesDesc(posts):
	posts = list(posts)
	posts.sort(key=lambda x: x.likes, reverse=True)
	return posts


def orderByCommentsAsc(posts):
	posts = list(posts)
	posts.sort(key=lambda x: x.count_all_comments())
	return posts


def orderByCommentsDesc(posts):
	posts = list(posts)
	posts.sort(key=lambda x: x.count_all_comments(), reverse=True)
	return posts


def is_ajax(request):
	return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'