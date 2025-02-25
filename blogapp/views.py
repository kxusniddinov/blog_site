from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView

from .models import Post


# Create your views here.
class PostListView(ListView):
    queryset = Post.published.all()
    content_object_name = "posts"
    paginate_by = 5
    template_name = "blog/post/list.html"


def post_detail(request, year, month, day, slug):
    post =  get_object_or_404(Post, slug=slug, status="published", publish__year=year, publish__month=month, publish__day=day)
    return render(request, "blog/post/detail.html", {"post": post})