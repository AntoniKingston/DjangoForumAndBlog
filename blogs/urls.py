from django.urls import path
from . import views

urlpatterns = [
    path('', views.blogs_list, name="blogs"),
    path('<slug:slug>', views.blog_page, name="blog"),
    path('<slug:slug>/<slug:slug2>', views.post_page, name="post")
]