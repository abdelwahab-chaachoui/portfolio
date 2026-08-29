from django.contrib import admin
from .models import Post, Keyword

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date', 'status')
    list_filter = ('status', 'keywords')
    search_fields = ('title', 'status')


class KeywordAdmin(admin.ModelAdmin):
    list_display = ('title',)
    list_filter = ('title',)

admin.site.register(Post, PostAdmin)
admin.site.register(Keyword, KeywordAdmin)
