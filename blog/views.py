from django.http import Http404
from django.shortcuts import get_object_or_404, render

from .models import Post


def post_list(request):
    posts = Post.published.all()
    return render(request, "post/list.html", {"posts": posts})


def post_detail(request, id):
    try:
        post = get_object_or_404(Post, id=id)
    except Post.DoesNotExist:
        raise Http404("Post does not exist")
    return render(request, "post/detail.html", {"post": post})
