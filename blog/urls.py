from django.urls import path
from blog.views import (
	blog_index_view,
	comment_likes_view,
	create_blog_view,
	delete_comment_view,
	delete_post_view,  
	detail_blog_view,
	edit_blog_view,
	post_comment_view,
	post_likes_view,
	publish_post_view,  
)
from account.views import(
    edit_user_view,
    delete_user_view,
    #list_users_view,
    dashboard_view,
)


app_name = 'blog'

urlpatterns = [
    # Overall
    path('dashboard/', dashboard_view, name='dashboard'),
	# Blog posts
	path('', blog_index_view, name='blogindex'),
	path('create', create_blog_view, name='create'),
	path('<slug>', detail_blog_view, name='detail'),
	path('<slug>/edit', edit_blog_view, name='edit'),
	path('<slug>/publish', publish_post_view, name='publish'),
	path('<slug>/delete', delete_post_view, name='delete'),
	path('<int:post_id>/like', post_likes_view, name='postlike'),
	# Comments
	path('<slug>/comment', post_comment_view, name='comment'),
	path('deletecomment/', delete_comment_view, name="deletecomment"),
	path('likecomment/', comment_likes_view, name='commentlike'),
    # Users
    # path('user_list/', list_users_view, name="user_list"),
    path('edit_user/', edit_user_view, name="edit_user"),
    path('delete_user/', delete_user_view, name="delete_user"),
]
