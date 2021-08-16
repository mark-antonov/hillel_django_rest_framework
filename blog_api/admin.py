from django.contrib import admin

from .models import Comment, Post


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 3


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['user', 'title', 'short_description', 'created', 'posted']
    fields = ['user', 'title', 'short_description', 'full_description', 'posted']
    list_filter = ['user', 'posted']
    search_fields = ['title']
    date_hierarchy = "created"
    inlines = [CommentInline]
    list_per_page = 10


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['user', 'text', 'post', 'created', 'moderated']
    fields = ['user', 'text', 'post', 'moderated']
    list_filter = ['moderated', 'user']
    search_fields = ['text']
    ordering = ['moderated']
