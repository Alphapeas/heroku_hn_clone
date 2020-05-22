from django.urls import path, include
from django.views.decorators.cache import cache_page

from . import views


urlpatterns = [
    path('post/list/', cache_page(60 * 1)(views.PostListAPIView.as_view()), name='post`s list'),
    path('post/create/', views.PostCreateAPIView.as_view(), name='create post'),
    path('post/update/<pk>/', views.PostUpdateAPIView.as_view(), name='update post'),
    path('post/detail/<pk>/', views.PostDetailAPIView.as_view(), name='post detail info (with all comments)'),
    path('post/<int:pk>/vote/', views.AddOrDeleteVoteAPIView.as_view(), name='Adding or deleting vote if it exists'),
    path('post/delete/<pk>/', views.PostDeleteAPIView.as_view(), name='delete'),
]
