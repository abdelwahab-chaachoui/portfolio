from django.db import models
from django.db.models.fields.related import ForeignKey
import uuid

from django.utils import choices

STATUS = (
    (0,"Created"),
    (1, "Draft"),
    (2, "Published")
)

""" 
Model for the different keywords in the system
might change, that's why i went with a DB table instead of static
"""
class Keyword(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date = models.DateField(auto_now_add=True)
    tags = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    status = models.IntegerField(choices=STATUS, default=0) # published or not
    keywords = ForeignKey(Keyword, related_name='keywords', on_delete=models.DO_NOTHING)

    class Meta:
        """
        when retrieving Posts - order the results by descending order
        this way we can print the latest ones at first
        """
        ordering = ['-date']

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
    active = models.BooleanField(default=False)
    email = models.EmailField(max_length=200, default='test@test.com')

    class Meta:
        """
        when retrieving Comments - order the results by descending order
        this way we can print the latest ones at first
        """
        ordering = ['-date']

    def __str__(self):
        return str(self.id)
