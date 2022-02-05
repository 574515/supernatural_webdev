from django.contrib import admin

from blog.models import BlogPost, Comment


class BlogPostAdmin(admin.ModelAdmin):
	list_display = ('title', 'pub_date', 'upd_date', 'author', 'likes', 'published', 'count_all_comments')
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
	list_display = ('text', 'created_at', 'likes', 'author')
	search_fields = ('author', 'text')
	readonly_fields = ('likes', 'userlikes',)

	filter_horizontal = ()
	list_filter = ('created_at', 'updated_at',)
	fieldsets = ()


admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(Comment, CommentAdmin)
