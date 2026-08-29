from django.http import HttpResponse
from django.shortcuts import render

from .models import Post, Comment

# Create your views here.
def index(request):
    blogs = Post.objects.filter(status=True).order_by("-date")

    for blog in blogs:
        print(blog)
        comments_of_blog_post = Comment.objects.filter(post=blog)

    context = {
        "blogs": blogs
        #"comments": comments
    }

    return render(request, "blogs/index.html", context)


def blog_content(request, id):
    blog = Post.objects.get(id=id)
    context = {"blog": blog}
    return render(request, "blogs/blog_content.html", context)
