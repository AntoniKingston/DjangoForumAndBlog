from django.shortcuts import render, redirect
from .models import Blog
from . import forms
from django.http import HttpResponse
# Create your views here.
def blogs_list(request):
    blogs = Blog.objects.all().order_by('title')
    if request.method == 'POST':
        form=forms.CreateBlog(request.POST, request.FILES)
        if form.is_valid():
            newblog = form.save(commit=False)
            newblog.save()
            newblog.authors.add(request.user)

            return redirect('blogs')
    else:
        form = forms.CreateBlog()

    return render(request, 'blogs/blogs_list.html', context = {'blogs' : blogs, 'form' : form})
def blog_page(request, slug):
    blog = Blog.objects.get(slug=slug)
    posts = blog.posts.all()
    in_authors = user_in_authors = request.user.is_authenticated and blog.authors.filter(username=request.user.username).exists()
    if request.method == 'POST':
        form=forms.CreatePost(request.POST, request.FILES)
        if form.is_valid():
            newpost = form.save(commit=False)
            newpost.blog = blog
            newpost.save()
            return redirect('blog', slug=blog.slug)
    else:
        form = forms.CreatePost()
    return render(request, 'blogs/blog_page.html', context = {'blog' : blog, 'posts' : posts, 'form' : form, 'in_authors': in_authors})
def post_page(request, slug, slug2):
    blog = Blog.objects.get(slug=slug)
    post = blog.posts.get(slug=slug2)
    comments = post.comments.all()
    if request.method == 'POST':
        form=forms.CreateComment(request.POST, request.FILES)
        if form.is_valid():
            newcomment = form.save(commit=False)
            newcomment.post = post
            newcomment.author = request.user
            newcomment.save()
            return redirect('post', slug=blog.slug, slug2=post.slug)
    else:
        form = forms.CreateComment()
    return render(request, 'blogs/post_page.html', context = {'post' : post, 'comments' : comments, 'form' : form
        })
