from django.db import models
from django.db.models.fields.related import ForeignKey
import uuid

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date = models.DateField(auto_now_add=True)
    tags = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    status = models.BooleanField(default=True) # published or not
    keywords = ForeignKey('Keyword', related_name='keywords', on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.title


""" 
Model for the different keywords in the system
might change, that's why i went with a DB table instead of static
"""
class Keyword(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title


"""
Model describing all the Comments of a Post
A Post can have 0..n Comments
When a Post is deleted all its Comments will be deleted as well
Do not to show any user data in the Console/Admin page
"""
class Comment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    author = models.CharField(max_length=200)
    content = models.TextField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.id)
