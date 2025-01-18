from django.contrib import admin
from .models import Thread, ThreadPost
# Register your models here.

admin.site.register(Thread)
admin.site.register(ThreadPost)