from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from .models import Post, Comment, BookReview, GameReview
from .forms import PostForm, CommentForm, BookReviewForm, GameReviewForm

#Basic views.
def home(request):

    return render(request, 'blog/home.html', {})

def about(request):

    return render(request, 'blog/about.html', {})

@login_required
def new(request):

    return render(request, 'blog/new.html', {})

#CS-posts-related views.
def post_list(request):
    
    posts = Post.objects.filter(publishedDate__lte = timezone.now()).order_by("publishedDate")
    return render(request, 'blog/post_list.html', {"posts": posts})

def post_detail(request, pk):
    
    post = get_object_or_404(Post, pk = pk)
    return render(request, 'blog/post_detail.html', {'post': post})

@login_required
def post_new(request):

    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit = False)
            post.author = request.user
            post.save()
            return redirect('post_detail', pk = post.pk)
            
    else:
        form = PostForm()
    
    return render(request, 'blog/post_edit.html', {'form': form})

@login_required
def post_edit(request, pk):

    post = get_object_or_404(Post, pk = pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance = post)
        if form.is_valid():
            form = form.save(commit = False)
            post.author = request.user
            post.save()
            return redirect('post_detail', pk = post.pk)
    else:
        form = PostForm(instance = post)
        
    return render(request, "blog/post_edit.html", {"form": form})

@login_required
def post_draft_list(request):

    posts = Post.objects.filter(publishedDate__isnull = True).order_by("createdDate")
    gameReviews = GameReview.objects.filter(publishedDate__isnull = True).order_by("createdDate")
    bookReviews = BookReview.objects.filter(publishedDate__isnull = True).order_by("createdDate")
    return render(request, "blog/post_draft_list.html", {"posts" : posts, "gameReviews": gameReviews, "bookReviews": bookReviews})

@login_required
def post_publish(request, pk):

    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect("post_detail", pk=pk)

@login_required
def post_remove(request, pk):
    
    post = get_object_or_404(Post, pk = pk)
    post.delete()
    return redirect('post_list')


#Comment views.
def add_comment_to_post(request, pk):

    post = get_object_or_404(Post, pk = pk)

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit = False)
            comment.post = post
            comment.save()
            return redirect('post_detail', pk = post.pk)
    
    else:
        form = CommentForm()
    
    return render(request, 'blog/add_comment_to_post.html', {"form": form})

@login_required
def comment_approve(request, pk):

    comment = get_object_or_404(Comment, pk = pk)
    comment.approve()
    return redirect('post_detail', pk = comment.post.pk)

@login_required
def comment_remove(request, pk):

    comment = get_object_or_404(Comment, pk = pk)
    comment.delete()
    return redirect('post_detail', pk = comment.post.pk)

#GameReview-realted views.
@login_required
def new_game_review(request):

    if request.method == "POST":
        form = GameReviewForm(request.POST, request.FILES)
        if form.is_valid():
            review = form.save(commit=False)
            review.author = request.user
            review.save()
            return redirect('game_review_detail', pk=review.pk)
    else:
        form = GameReviewForm()
    return render(request, 'blog/game_review_edit.html', {'form': form})

def game_review_list(request):
    
    reviews = GameReview.objects.filter(publishedDate__lte = timezone.now()).order_by("publishedDate")
    return render(request, 'blog/game_review_list.html', {"reviews": reviews})

def game_review_detail(request, pk):
    
    review = get_object_or_404(GameReview, pk = pk)
    return render(request, 'blog/game_review_detail.html', {'review': review})

@login_required
def game_review_publish(request, pk):

    review = get_object_or_404(GameReview, pk=pk)
    review.publish()
    return redirect("game_review_detail", pk=pk)

@login_required
def game_review_edit(request, pk):

    review = get_object_or_404(GameReview, pk = pk)
    if request.method == "POST":
        form = GameReviewForm(request.POST, instance = review)
        if form.is_valid():
            form = form.save(commit = False)
            review.author = request.user
            review.save()
            return redirect('game_review_detail', pk = review.pk)
    else:
        form = GameReviewForm(instance = review)
        
    return render(request, "blog/game_review_edit.html", {"form": form})

@login_required
def game_review_remove(request, pk):
    
    review = get_object_or_404(GameReview, pk = pk)
    review.delete()
    return redirect('game_review_list')

#BookReview-related views.
def book_review_list(request):

    reviews = BookReview.objects.filter(publishedDate__lte = timezone.now()).order_by("publishedDate")
    return render(request, 'blog/book_review_list.html', {"reviews": reviews})

def book_review_detail(request, pk):

    review = get_object_or_404(BookReview, pk = pk)
    return render(request, 'blog/book_review_detail.html', {'review': review})

@login_required
def new_book_review(request):

    if request.method == "POST":
        form = BookReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.author = request.user
            review.save()
            return redirect('book_review_detail', pk=review.pk)
    else:
        form = BookReviewForm()
    return render(request, 'blog/book_review_edit.html', {'form': form})

@login_required
def book_review_edit(request, pk):

    review = get_object_or_404(BookReview, pk = pk)
    if request.method == "POST":
        form = BookReviewForm(request.POST, instance = review)
        if form.is_valid():
            form = form.save(commit = False)
            review.author = request.user
            review.save()
            return redirect('book_review_detail', pk = review.pk)
    else:
        form = BookReviewForm(instance = review)
        
    return render(request, "blog/book_review_edit.html", {"form": form})

@login_required
def book_review_publish(request, pk):

    review = get_object_or_404(BookReview, pk=pk)
    review.publish()
    return redirect("book_review_detail", pk=pk)

@login_required
def book_review_remove(request, pk):

    review = get_object_or_404(BookReview, pk = pk)
    review.delete()
    return redirect('book_review_list')
