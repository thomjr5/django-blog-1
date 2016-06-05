from django.contrib import admin
from .models import Post, Comment

class PostAdmin(admin.ModelAdmin):
    list_display = ['title','author','created_date','published_date']
    
admin.site.register(Post, PostAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display = ['author','post','created_date','approved_comment']


admin.site.register(Comment,CommentAdmin)
