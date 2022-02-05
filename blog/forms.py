from django import forms
from blog.models import BlogPost, Comment


class CreateBlogPostForm(forms.ModelForm):
	
	class Meta:
		model = BlogPost
		fields = ['title', 'description', 'body', 'image']

		
class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ('text',)
		widgets = {
			'text': forms.Textarea(attrs={'class': 'form-contorl py-1 px-3', 'rows': 5, 'placeholder': 'Your comment'})
		}


class UpdateBlogPostForm(forms.ModelForm):

	class Meta:
		model = BlogPost
		fields = ['title', 'description', 'body', 'image']

	def save(self, commit=True):
		blog_post = self.instance
		blog_post.title = self.cleaned_data['title']
		blog_post.description = self.cleaned_data['description']
		blog_post.body = self.cleaned_data['body']

		if self.cleaned_data['image']:
			blog_post.image = self.cleaned_data['image']

		if commit:
			blog_post.save()
		return blog_post
