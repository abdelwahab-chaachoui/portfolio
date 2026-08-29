from django.contrib import admin
from .models import Post, Keyword, Comment

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date', 'status')
    list_filter = ('status', 'keywords')
    search_fields = ('title', 'status')

class KeywordAdmin(admin.ModelAdmin):
    list_display = ('title',)
    list_filter = ('title',)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'date', 'post')
    list_filter = ('post',)
    search_fields = ('id', 'post')

admin.site.register(Post, PostAdmin)
admin.site.register(Keyword, KeywordAdmin)
admin.site.register(Comment, CommentAdmin)
