from django.contrib import admin

from petstagram.common.models import Comment, Like
from petstagram.pets.models import Pet


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    ...


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    ...
