from django.contrib import admin

from blog.models import BlogPost, Comment

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date', 'upd_date', 'author', 'likes', 'published')
    search_fields = ('author', 'title')
    readonly_fields = ('likes', 'userlikes', 'pub_date', 'upd_date', 'slug')
    actions = [
        'publish_posts', 'unpublish_posts',
    ]

    def publish_posts(self, request, queryset):
        cnt = queryset.filter(published=False).update(published=True)
        self.message_user(request, 'Published {} posts.'.format(cnt))
    publish_posts.short_description = 'Publish Posts'

    def unpublish_posts(self, request, queryset):
        cnt = queryset.filter(published=True).update(published=False)
        self.message_user(request, 'Unapproved {} posts.'.format(cnt))
    unpublish_posts.short_description = 'Unpublish Posts'

    filter_horizontal = ()
    list_filter = ('pub_date', 'upd_date', 'published',)
    fieldsets = ()

class CommentAdmin(admin.ModelAdmin):
    list_display = ('text', 'created_at', 'likes', 'author') #, 'approved'
    search_fields = ('author', 'text')
    readonly_fields = ('likes', 'userlikes',)
    # actions = [
    #     'approve_comments', 'disapprove_comments',
    # ]

    # def approve_comments(self, request, queryset):
    #     cnt = queryset.filter(approved=False).update(approved=True)
    #     self.message_user(request, 'Approved {} comments.'.format(cnt))
    # approve_comments.short_description = 'Approve Comments'

    # def disapprove_comments(self, request, queryset):
    #     cnt = queryset.filter(approved=True).update(approved=False)
    #     self.message_user(request, 'Disapproved {} comments.'.format(cnt))
    # disapprove_comments.short_description = 'Disapprove Comments'

    filter_horizontal = ()
    list_filter = ('created_at', 'updated_at',) # 'approved',
    fieldsets = ()

admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(Comment, CommentAdmin)