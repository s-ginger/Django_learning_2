from django.contrib import admin

from .models import Comment, Tovars, Review

admin.site.register(Comment)
admin.site.register(Tovars)
admin.site.register(Review)