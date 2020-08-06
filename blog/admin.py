from django.contrib import admin
from .models import Blog,UserBlog

# Register your models here.
admin.site.register(Blog)
admin.site.register(UserBlog)