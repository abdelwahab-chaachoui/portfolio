from django.db import models
from django.db.models.fields.related import ForeignKey

# Create your models here.

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


# Model for the different keywords in the system
# might change, that's why i went with a DB table instead of static
class Keyword(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title