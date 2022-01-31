from django.urls import path
from blog.views import (
    CreateBlogView,
    DetailBlogView,
    EditBlogView,
    PublishPostView,
    delete_post_view,    
    PostLikesView,
    PostCommentView,
    delete_comment_view,
    BlogIndexView,
    comment_likes_view,
)

app_name = 'blog'

urlpatterns = [
    # ! Blog posts
    path('', BlogIndexView, name='blogindex'),
    path('create', CreateBlogView, name='create'),
    path('<slug>', DetailBlogView, name='detail'),
    path('<slug>/edit', EditBlogView, name='edit'),
    path('<slug>/publish', PublishPostView, name='publish'),
    path('<slug>/delete', delete_post_view, name='delete'),
    path('<int:post_id>/like', PostLikesView, name='postlike'),
    # ! Comments
    path('<slug>/comment', PostCommentView, name='comment'),
    path('deletecomment/', delete_comment_view, name="deletecomment"),
    path('likecomment/', comment_likes_view, name='commentlike'),
]