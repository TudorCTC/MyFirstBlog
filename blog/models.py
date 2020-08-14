from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    title = models.CharField(max_length = 200)
    text = models.TextField()
    createdDate = models.DateTimeField(default = timezone.now)
    publishedDate = models.DateTimeField(blank = True, null = True)

    def publish(self):

        self.publishedDate = timezone.now()
        self.save()

    def approved_comments(self):

        return self.comments.filter(approved_comment = True)
        
    def __str__(self):

        return self.title

class GameReview(models.Model):

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    
    coverArt = models.ImageField(null = True, blank = True)
    title = models.CharField(max_length = 200)
    intro = models.TextField()
    graphics = models.TextField()
    story = models.TextField()
    gameplay = models.TextField()
    conclusion = models.TextField()

    createdDate = models.DateTimeField(default = timezone.now)
    publishedDate = models.DateTimeField(blank = True, null = True)

    def publish(self):

        self.publishedDate = timezone.now()
        self.save()
        
    def __str__(self):

        return self.title

class BookReview(models.Model):

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)

    title = models.CharField(max_length = 200)
    intro = models.TextField()
    plot = models.TextField()
    characters = models.TextField()
    worldBuilding = models.TextField()
    conclusion = models.TextField()

    createdDate = models.DateTimeField(default = timezone.now)
    publishedDate = models.DateTimeField(blank = True, null = True)

    def publish(self):

        self.publishedDate = timezone.now()
        self.save()
        
    def __str__(self):

        return self.title

class Comment(models.Model):

    post = models.ForeignKey('blog.Post', on_delete = models.CASCADE, related_name = "comments")
    author = models.CharField(max_length = 200)
    text = models.TextField()
    created_date = models.DateTimeField(default = timezone.now)
    approved_comment = models.BooleanField(default = False)

    def approve(self):

        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text