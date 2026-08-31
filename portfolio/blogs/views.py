from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .forms import CommentForm
from .models import Post

def index(request):
    blogs = Post.objects.filter(status=2).order_by("-date")
    context = {"blogs": blogs}
    return render(request, "blogs/index.html", context)

def blog_content(request, id):
    blog = get_object_or_404(Post, id=id)
    comments = blog.comments.filter(active=True)
    new_comment = None

    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = blog
            new_comment.save()
    else: # GET
        comment_form = CommentForm()

    return render(request, "blogs/blog_content.html", {"blog": blog,
                                                                            "comment_form": comment_form,
                                                                            "new_comment": new_comment,
                                                                            "comments": comments,
                                                                            })

def _format_tags(tags_as_str):
    tags_list = tags_as_str.split(' ')
    return set(tags_list)