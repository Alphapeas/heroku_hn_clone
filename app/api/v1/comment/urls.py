from django.urls import path, include

from app.api.v1.comment.views import CommentCreateAPIView, CommentListAPIView, CommentUpdateAPIView, CommentDeleteAPIView


urlpatterns = [
    path('comment/create/', CommentCreateAPIView.as_view(), name='create comment'),
    path('comment/update/<pk>/', CommentUpdateAPIView.as_view(), name='update comment'),
    path('comment/delete/<pk>/', CommentDeleteAPIView.as_view(), name='delete comment'),
]
