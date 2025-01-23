from django.shortcuts import render, redirect
from .models import Thread, ThreadPost
from . import forms
# Create your views here.
def home_view(request):
    threads = Thread.objects.all().order_by('title')
    if request.method == 'POST':
        form=forms.CreateThread(request.POST, request.FILES)
        if form.is_valid():
            newthread = form.save(commit=False)

            newthread.creator = request.user
            newthread.save()

            return redirect('forum')
    else:
        form = forms.CreateThread()
    return render(request, 'forum/forum_home.html', context={'threads' : threads, 'form' : form})
def thread_view(request, slug):
    thread = Thread.objects.get(slug=slug)
    posts = thread.posts.all().order_by('created_at')
    if request.method == 'POST':
        form=forms.CreateThreadPost(request.POST, request.FILES)
        if form.is_valid():
            newpost = form.save(commit=False)

            newpost.author = request.user
            newpost.thread=thread
            newpost.save()

            return redirect('thread', slug = slug)
    else:
        form = forms.CreateThreadPost()
    return render(request, 'forum/thread_view.html', context={'thread' : thread, 'posts' : posts, 'form' : form})
