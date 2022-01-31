from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from account.forms import RegistrationForm, AccountAuthenticationForm, AccountUpdateForm
from account.models import Account
from blog.models import BlogPost, Comment


def AccountView(request, user_id):
	try:
		user = Account.objects.get(id=user_id)
		context = {}
	except Account.DoesNotExist:
		return redirect('index')
	comments = Comment.objects.filter(author=user).all()
	if request.user.is_superuser or request.user == user:
		posts = BlogPost.objects.filter(author=user).order_by('-pub_date')
		if request.POST:
			form = AccountUpdateForm(request.POST, instance=request.user)
			if form.is_valid():
				form.initial = {
					'first_name': request.POST['first_name'],
					'last_name': request.POST['last_name'],
					'username': request.POST['username'],
					'email': request.POST['email']
				}
				form.save()
				context['account_form'] = form
		else:
			form = AccountUpdateForm(
				initial = {
					'first_name': request.user.first_name,
					'last_name': request.user.last_name,
					'username': request.user.username,
					'email': request.user.email
				}
			)
			context['account_form'] = form
	else:
		posts = BlogPost.objects.filter(published=True, author=user).order_by('-pub_date')
	context['posts'] = posts
	context['currUser'] = user
	context['comments'] = comments
	return render(request, 'account/account.html', context)


def LoginView(request):
	context = {}
	user = request.user
	if user.is_authenticated:
		return redirect('index')
	if request.POST:
		form = AccountAuthenticationForm(request.POST)
		if form.is_valid():
			email = request.POST['email']
			password = request.POST['password']
			user = authenticate(email=email, password=password)
			if user:
				login(request, user)
				return redirect('index')
	else:
		form = AccountAuthenticationForm()
	context['login_form'] = form
	context['navbar'] = 'login'
	return render(request, 'account/login.html', context)


def LogoutView(request):
	logout(request)
	return redirect('index')


def MustAuthenticateView(request):
	if request.user.is_authenticated:
			return redirect('index')
	return render(request, 'account/must_authenticate.html', {})


def RegisterView(request):
	context = {}
	if request.user.is_authenticated:
		return redirect('index')
	if request.POST:
		form = RegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			email = form.cleaned_data.get('email')
			raw_password = form.cleaned_data.get('password2')
			account = authenticate(email=email, password=raw_password)
			login(request, account)
			return redirect('index')
		else:
			context = {
				'registration_form': form,
				'navbar': 'register'
			}
	else:
		form = RegistrationForm()
		context = {
			'registration_form': form,
			'navbar': 'register'
		}
	return render(request, 'account/register.html', context)