import json
from django.http import HttpResponseRedirect, HttpResponse
from django.http.response import Http404
from django.shortcuts import render, get_object_or_404, redirect
from blog.models import BlogPost, Comment, LikeComment
from account.models import Account
from blog.forms import CommentForm, CreateBlogPostForm, UpdateBlogPostForm
from django.urls import reverse
from django.http import JsonResponse


def blog_index_view(request):
	context = {}
	user = request.user
	all_posts = BlogPost.objects.all()
	pub_posts = BlogPost.objects.filter(published=True).order_by('-pub_date').all()
	unpub_posts = BlogPost.objects.filter(published=False).all()
	comments = Comment.objects.all()

	if all_posts:
		last_post = BlogPost.objects.order_by('-pub_date')[0]
		context['last_post'] = last_post
	if comments:
		last_comment = Comment.objects.order_by('-created_at')[0]
		context['last_comment'] = last_comment

	user_has_posts = False
	for post in all_posts:
		if post.author == user:
			not user_has_posts
	
	users = Account.objects.all()
	admins = Account.objects.filter(is_admin=True).all()

	if users:
		last_joined = Account.objects.order_by('-date_joined')[0]
		context['last_joined'] = last_joined

	if user_has_posts:
		unpub_withauth = BlogPost.objects.filter(author=user).all()

	if user.is_superuser:
		context['posts'] = all_posts
	elif user.is_authenticated and user_has_posts:
		context['posts'] = unpub_withauth
	else:
		context['posts'] = pub_posts
	#context['posts'] = all_posts
	context['unpub_posts'] = unpub_posts
	context['pub_posts'] = pub_posts
	context['comments'] = comments
	context['navbar'] = 'blogindex'
	context['users'] = users
	context['admins'] = admins
	return render(request, 'blog/blog_index.html', context)
	

def create_blog_view(request):
	context = {}
	
	user = request.user
	if not user.is_authenticated:
		return redirect('account:must_authenticate')
		
	form = CreateBlogPostForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		obj = form.save(commit=False)
		author = Account.objects.filter(email=request.user.email).first()
		obj.author = author
		obj.save()
		form = CreateBlogPostForm()
		return HttpResponseRedirect(reverse('index'))
		
	context = {
		'form': form,
		'navbar': 'blogindex',
	}
	
	return render(request, 'blog/create_blog.html', context)


def detail_blog_view(request, slug):
	user = request.user
	if not user.is_authenticated:
		return redirect('account:must_authenticate')
	context = {}    
	try:
		blog_post = get_object_or_404(BlogPost, slug=slug)
	except Http404:
		return redirect('index')

	if not blog_post.published:
		if not user.is_superuser and not blog_post.author == user:
			return redirect('index')

	comments = blog_post.comments.all()
	new_comment = None
	if request.method == 'POST':
		comment_form = CommentForm(data=request.POST)
		if comment_form.is_valid():
			new_comment = comment_form.save(commit=False)
			new_comment.post = blog_post
			new_comment.author = user
			new_comment.save()
	else:
		comment_form = CommentForm()


	context = {
		'post': blog_post,
		'comments': comments,
		'new_comment': new_comment,
		'comment_form': comment_form,
		'navbar': 'blogindex',
	}

	return render(request, 'blog/detail_blog.html', context)


def edit_blog_view(request, slug):
	context = {}

	user = request.user
	blog_post = get_object_or_404(BlogPost, slug=slug)

	if not user.is_authenticated:
		return redirect('account:must_authenticate')
	if not user == blog_post.author:
		return redirect('index')

	if request.POST:
		form = UpdateBlogPostForm(request.POST or None, request.FILES or None, instance=blog_post)
		if form.is_valid():
			obj = form.save(commit=False)
			obj.save()
			context['success_message'] = 'Updated!'
			blog_post = obj

	form = UpdateBlogPostForm(
		initial = {
			'title': blog_post.title,
			'description': blog_post.description,
			'body': blog_post.body,
			'image': blog_post.image,
		}
	)
	context = {
		'form': form,
		'post': blog_post,
		'navbar': 'blogindex',
	}
	return render(request, 'blog/edit_blog.html', context)


def publish_post_view(request, slug):
	if not request.user.is_superuser:
		return redirect('account:must_authenticate')

	try:
		post = get_object_or_404(BlogPost, slug=slug)
	except BlogPost.DoesNotExist:
		return HttpResponse('Product not found', status=404)
	except Exception:
		return HttpResponse('Internal Error', status=500)

	if request.method == 'GET':
		if not post.published:
			post.published = True
			post.save()
		else:           
			post.published = False
			post.save()
			
	return HttpResponse(json.dumps({"good": True, "slug": slug}), content_type="application/json")


def delete_post_view(request, slug):
	if not request.user.is_authenticated:
		return redirect('account:must_authenticate')

	try:
		post = get_object_or_404(BlogPost, slug=slug)
		if not request.user.is_superuser or not request.user == post.author:
			return redirect('index')
	except BlogPost.DoesNotExist:
		return HttpResponse('Product not found', status=404)
	except Exception:
		return HttpResponse('Internal Error', status=500)

	if request.method == 'GET':
		post.delete()
		return HttpResponse(json.dumps({"good": True, "slug": slug, "user": request.user.username, "author": post.author.username}), content_type="application/json")
	else:
		post.delete()
		return HttpResponseRedirect(reverse('index'))


def post_comment_view(request, slug):
	user = request.user
	if not user.is_authenticated:
		return redirect('account:must_authenticate')

	post = get_object_or_404(BlogPost, slug=slug)
	if post and is_ajax(request):
		text = request.POST.get('text', None)
		if text:
			comment = post.comments.create(
								post=post.id,
								author=user,
								text=text,
						)
			comment.save()
			if not comment.likes:
				likes = 0
			response = {#'posted_comment': comment
				'text': comment.text,
				'post': post.slug,
				'comm_id': comment.id,
				'author': comment.author.username,
				'likes': likes,
				'success_msg': "Comment posted successfully!",
			}
			return JsonResponse(response)
	else:
		return redirect('index')


def is_ajax(request):
	return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'


def post_likes_view(request, post_id):
	if request.user.is_anonymous:
		return redirect('account:must_authenticate')
	if request.method == "GET" and is_ajax(request):
		user = Account.objects.get(id=request.user.id)
		post = BlogPost.objects.get(id=post_id)
		if user in post.userlikes.all():
			post.likes -= 1
			post.userlikes.remove(user)
		else:
			post.likes += 1
			post.userlikes.add(user)
		post.save()
		return HttpResponse(json.dumps({"good": True}), content_type="application/json")
	else:
		return redirect('index')


def delete_comment_view(request):
	if request.user.is_anonymous:
		return redirect('account:must_authenticate')
	if request.method == "POST" and is_ajax(request):
		id = request.POST.get('id', None)
		Comment.objects.get(pk=id).delete()
		data = {
			'deleted': True
		}
		return JsonResponse(data)
	else:
		return redirect('index')


def comment_likes_view(request):
	if request.user.is_anonymous:
		return redirect('account:must_authenticate')
	if request.method == "POST" and is_ajax(request):
		id = request.POST.get('id', None)
		user = Account.objects.get(id=request.user.id)
		comment = Comment.objects.get(id=id)
		new_like = LikeComment(commlike_user=user, comment=comment)
		if user in comment.userlikes.all():
			new_like.alreadyLiked = False
			comment.likes -= 1
			comment.userlikes.remove(user)
		else:
			new_like.alreadyLiked = True
			comment.likes += 1
			comment.userlikes.add(user)
		new_like.save()
		comment.save()
		return HttpResponse(json.dumps({"good": True}), content_type="application/json")
	else:
		return redirect('account:must_authenticate')
