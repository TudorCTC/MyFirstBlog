from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    
    #Basic URLs.
    path('', views.home, name = "home"),
    path('new/', views.new, name = "new"),
    path('drafts', views.post_draft_list, name = "post_draft_list"), 

    #CS-related URLs.
    path('cs_post_list/', views.post_list, name = 'post_list'),
    path('post/<int:pk>', views.post_detail, name = 'post_detail'), 
    path('post/new/', views.post_new, name = 'post_new'), 
    path('post/<int:pk>/edit/', views.post_edit, name = "post_edit"), 
    path('post/<pk>/publish/', views.post_publish, name = "post_publish"), 
    path('post/<pk>/remove/', views.post_remove, name = "post_remove"),


    #GameReview-related URLs.
    path('game_review_list/', views.game_review_list, name = "game_review_list"),
    path('game_review/<int:pk>', views.game_review_detail, name = "game_review_detail"),
    path('game_review/new/', views.new_game_review, name = "new_game_review"), 
    path('game_review/<int:pk>/edit/', views.game_review_edit, name = "game_review_edit"),
    path('game_review/<pk>/publish/', views.game_review_publish, name = "game_review_publish"), 
    path('game_review/<pk>/remove/', views.game_review_remove, name = "game_review_remove"),

    #BookReview-related URLs.
    path('book_review_list/', views.book_review_list, name = "book_review_list"),
    path('book_review/<int:pk>', views.book_review_detail, name = "book_review_detail"),
    path('book_review/new/', views.new_book_review, name = "new_book_review"),
    path('book_review/<int:pk>/edit/', views.book_review_edit, name = "book_review_edit"),
    path('book_review/<pk>/publish/', views.book_review_publish, name = "book_review_publish"), 
    path('book_review/<pk>/remove/', views.book_review_remove, name = "book_review_remove"),
    
    
    #Comment-related URLs.
    path('post/<int:pk>/comment', views.add_comment_to_post, name = "add_comment_to_post"), 
    path('comment/<int:pk>/approve/', views.comment_approve, name = "comment_approve"), 
    path('comment/<int:pk>/remove/', views.comment_remove, name = "comment_remove"),

    #About-page URL.
    path('about', views.about, name = "about"),  
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)