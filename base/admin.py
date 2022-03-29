from django.contrib import admin

# Register your models here.

from .models import Category, Post, Topic, Message

admin.site.register(Category)
admin.site.register(Topic)
admin.site.register(Post)
admin.site.register(Message)