from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from unidecode import unidecode
# Create your models here.

class Blog(models.Model):
    authors = models.ManyToManyField(User, related_name="authored_blogs")
    title = models.CharField(max_length=100, default="New Blog")
    slug = models.SlugField(unique=True, blank=True)
    def __str__(self):
        authors_list=self.authors_list()
        return self.title+"\n"+authors_list
    def authors_list(self):
        authors_set = self.authors.all()
        length = len(authors_set)
        authors_list = ""
        if length == 1:
            authors_list = authors_set.first().username
        else:
            i = 0
            for author in authors_set:
                authors_list += author.username
                if i < length - 2:
                    authors_list += ", "
                elif i == length - 2:
                    authors_list += " and "
                i += 1
        return "by: "+authors_list
    def create_slug(self):
        base_slug = slugify(unidecode(self.title))
        slug = base_slug
        counter = 1
        while Blog.objects.filter(slug=slug).exists():
            slug = f"{base_slug}-{counter}"
            counter += 1
        return slug

    def save(self, *args, **kwargs):
        self.slug = self.create_slug()
        super().save(*args, **kwargs)

class Post(models.Model):
    blog = models.ForeignKey(Blog, related_name="posts", on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    slug = models.SlugField()
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title
    def create_slug(self):
        base_slug = slugify(unidecode(self.title))
        slug = base_slug
        counter = 1
        while Blog.objects.filter(slug=slug).exists():
            slug = f"{base_slug}-{counter}"
            counter += 1
        return slug

    def save(self, *args, **kwargs):
        self.slug = self.create_slug()
        super().save(*args, **kwargs)

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    author = models.ForeignKey(User, related_name="comments", on_delete=models.CASCADE)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    parent_comment = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        related_name="replies",
        on_delete=models.CASCADE
    )
    def __str__(self):
        return self.date.strftime("%Y-%m-%d %H:%M:%S") + " " + self.author.username