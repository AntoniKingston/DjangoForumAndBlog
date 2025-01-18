from django.shortcuts import render
from .models import Thread, ThreadPost
# Create your views here.
def home_view(request):
    threads = Thread.objects.all().order_by('title')
    return render(request, 'forum/forum_home.html', context={'threads' : threads})
def thread_view(request, slug):
    thread = Thread.objects.get(slug=slug)
    posts = thread.posts.all().order_by('created_at')
    return render(request, 'forum/thread_view.html', context={'thread' : thread, 'posts' : posts})
