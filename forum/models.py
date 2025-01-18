from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from unidecode import unidecode
# Create your models here.

class Thread(models.Model):
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='threads')
    slug = models.SlugField(unique=True, blank=True)

    def __str__(self):
        return self.title
    def create_slug(self):
        base_slug = slugify(unidecode(self.title))
        slug = base_slug
        counter = 1
        while Thread.objects.filter(slug=slug).exists():
            slug = f"{base_slug}-{counter}"
            counter += 1
        return slug

    def save(self, *args, **kwargs):
        self.slug = self.create_slug()
        super().save(*args, **kwargs)


class ThreadPost(models.Model):
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE, related_name='posts')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    quoted_posts = models.ManyToManyField('self', related_name='quoted_by', symmetrical=False, blank=True)

    def __str__(self):
        return f"Post by {self.author} in {self.thread.title}"