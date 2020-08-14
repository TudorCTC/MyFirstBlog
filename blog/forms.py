from django import forms
from .models import Post, GameReview, Comment, BookReview

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ("title", "text", )

class GameReviewForm(forms.ModelForm):

    class Meta:
        model = GameReview
        fields = ("title", "coverArt", "intro", "graphics", "story", "gameplay", "conclusion", )

class BookReviewForm(forms.ModelForm):

    class Meta:
        model = BookReview
        fields = ("title", "intro", "plot", "characters", "worldBuilding", "conclusion", )

class CommentForm(forms.ModelForm):

    class Meta:

        model = Comment
        fields = ("author", "text", )