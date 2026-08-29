from django.db import models

# Create your models here.

class Post(models.Model):

    title = models.CharField(max_length=200)
    content = models.TextField()
    date = models.DateField(auto_now_add=True)
    keywords = models.CharField(max_length=200)
    tags = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    status = models.BooleanField(default=True) # published or not

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'post'
        ordering = ['-date']

