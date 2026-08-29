from django.contrib import admin
from .models import Post

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date', 'status')
    list_filter = ('status',)
    search_fields = ('title', 'body')

admin.site.register(Post)

