from django.contrib import admin
from .models import Post, Comment, GameReview, BookReview


admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(GameReview)
admin.site.register(BookReview)