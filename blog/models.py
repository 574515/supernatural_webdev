from django.db import models

from django.utils.text import slugify
from django.conf import settings
from django.db.models.signals import post_delete, pre_save
from django.dispatch import receiver
from django.utils.timezone import now
import datetime
from account.models import Account
from datetime import timezone, datetime, timedelta

import json


def json_default(value):
    if isinstance(value, datetime.datetime):
        return dict(year=value.year, month=value.month, day=value.day, hour=value.hour, minute=value.minute, second=value.second)
    if isinstance(value, models.ForeignKey):
        return dict(author_id=value.username)
    else:
        return value.__dict__


def upload_location(instance, filename):
    file_path = 'blog/{author_id}/{title}-{filename}'.format(
        author_id=str(instance.author_id),
        title=str(instance.title),
        filename=filename
    )
    return file_path


class BlogPost(models.Model):
    title                   = models.CharField(max_length=50, null=False, blank=False)
    body                    = models.TextField(max_length=5000, null=False, blank=False)
    description             = models.TextField(max_length=300, null=False, blank=False)
    image                   = models.ImageField(upload_to=upload_location, null=False, blank=False)
    pub_date                = models.DateTimeField(verbose_name='Date published', default=now)
    upd_date                = models.DateTimeField(auto_now=True, verbose_name='Date updated')
    author                  = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='posts_by_author')
    slug                    = models.SlugField(blank=True, unique=True)
    published               = models.BooleanField(default=False)
    likes                   = models.PositiveIntegerField(default=0)
    userlikes               = models.ManyToManyField(Account, related_name='postlikes', verbose_name="Users who liked")

    def __str__(self):
        return self.title

    def count_published(self):
        return self.published.filter(published=False).count()

    def count_all_comments(self):
        return self.comments.count()

    def toJSON(self):
        return json.dumps(self, default=json_default, sort_keys=True)

    def kakoGod(self):
        return {
            'title': self.title,
            'body': self.body,
            'description': self.description,
            'image': str(self.image),
            'pub_date': str(self.pub_date.strftime("%d.%m.%Y, %H:%M")),
            'author_id': self.author.id,
            'author': self.author.username,
            'slug': str(self.slug),
            'likes': self.likes,
            'comments': self.count_all_comments(),
        }


@receiver(post_delete, sender=BlogPost)
def submission_delete(sender, instance, **kwargs):
    instance.image.delete(False)

def pre_save_blog_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.author.username + '-' + instance.title)

pre_save.connect(pre_save_blog_post_receiver, sender=BlogPost)


class LikePost(models.Model):
    postlike_user           = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="users_postlike")
    post                    = models.ForeignKey(BlogPost, on_delete=models.CASCADE, related_name="posts")
    alreadyLikedPost        = models.BooleanField(default=False)

    def __str__(self):
        return "Liked"


class Comment(models.Model):
    post                    = models.ForeignKey(BlogPost, on_delete=models.CASCADE, related_name='comments')
    author                  = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='commAuthor')
    text                    = models.TextField(blank=False, max_length=300)
    likes                   = models.PositiveIntegerField(default=0)
    userlikes               = models.ManyToManyField(Account, related_name='commlikes')
    created_at              = models.DateTimeField(auto_now_add=True)
    updated_at              = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return self.text[:80]

    def count(self):
        return self.comments.count()


class LikeComment(models.Model):
    commlike_user           = models.ForeignKey(Account, on_delete=models.CASCADE, related_name="users_commlike")
    comment                 = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name="comment")
    alreadyLikedComment     = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.commlike_user} liked {self.comment}"