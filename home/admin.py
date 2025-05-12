from django.contrib import admin
from .models import Post, Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['user', 'body', 'slug', 'created_at', 'updated_at']
    raw_id_fields = ['user']
    search_fields = ['user', 'body', 'slug']
    list_filter = ['user', 'created_at', 'updated_at']
    
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['user', 'post', 'body', 'is_reply', 'created_at']
    raw_id_fields = ['user', 'post', 'reply']
