from django.shortcuts import render
from .models import Post
from django.utils import timezone

def post_list(request):
    # request --> everthing we receive from the user 
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts':posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})