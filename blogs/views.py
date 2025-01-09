from django.shortcuts import render
from .models import Blog
from django.http import HttpResponse
# Create your views here.
def blogs_list(request):
    blogs = Blog.objects.all().order_by('title')

    return render(request, 'blogs/blogs_list.html', context = {'blogs' : blogs})
def blog_page(request, slug):
    blog = Blog.objects.get(slug=slug)
    posts = blog.posts.all()
    return render(request, 'blogs/blog_page.html', context = {'blog' : blog, 'posts' : posts})
def post_page(request, slug, slug2):
    blog = Blog.objects.get(slug=slug)
    post = blog.posts.get(slug=slug2)
    comments = post.comments.all()
    return render(request, 'blogs/post_page.html', context = {'post' : post, 'comments' : comments})
