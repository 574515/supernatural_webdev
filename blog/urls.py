from django.urls import path
from blog.views import (
    CreateBlogView,
    DetailBlogView,
    EditBlogView,
    PublishPostView,
    DeletePostView,    
    PostLikesView,
    PostCommentView,
    ApproveCommentView,
    DeleteCommentView,
    BlogIndexView,
    CommentLikesView
)

app_name = 'blog'

urlpatterns = [
    path('', BlogIndexView, name='blogindex'),
    path('create', CreateBlogView, name='create'),
    path('<slug>', DetailBlogView, name='detail'),
    path('<slug>/edit', EditBlogView, name='edit'),
    path('<slug>/publish', PublishPostView, name='publish'),
    path('<slug>/delete', DeletePostView, name='delete'),

    
    path('<int:post_id>/like', PostLikesView, name='postlike'),

    # Comments
    path('<slug>/comment', PostCommentView, name='comment'),


    path('approvecomment/', ApproveCommentView, name="approvecomment"),    
    path('deletecomment/', DeleteCommentView, name="deletecomment"),
    path('<int:post_id>/<int:comment_id>/likecomment', CommentLikesView, name='commentlike'),
]