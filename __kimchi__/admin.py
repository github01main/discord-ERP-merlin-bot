from django.contrib import admin

# Register your models here.

from .models import Document
from .models import Post_item

admin.site.register(Document)
admin.site.register(Post_item)