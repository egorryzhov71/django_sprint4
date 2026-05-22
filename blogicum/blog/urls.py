from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('profile/<str:username>/', views.ProfileView.as_view(), name='profile'),
    path('profile/<str:username>/edit/', views.ProfileEditView.as_view(), name='profile_edit'),
    path('posts/create/', views.PostCreateView.as_view(), name='post_create'),
    path('posts/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('posts/<int:pk>/edit/', views.PostUpdateView.as_view(), name='post_edit'),
    path('posts/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post_delete'),
    path('posts/<int:post_id>/comment/', views.CommentCreateView.as_view(), name='comment_create'),
    path('posts/<int:post_id>/edit_comment/<int:pk>/', 
         views.CommentUpdateView.as_view(), 
         name='comment_edit'),
    path('posts/<int:post_id>/delete_comment/<int:pk>/', 
         views.CommentDeleteView.as_view(), 
         name='comment_delete'),
    path('category/<slug:category_slug>/', 
         views.CategoryPostsView.as_view(), 
         name='category_posts'),
]
