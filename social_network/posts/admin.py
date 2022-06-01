from django.contrib import admin

from .models import Post, PostInLiked


admin.site.register(Post)
admin.site.register(PostInLiked)
