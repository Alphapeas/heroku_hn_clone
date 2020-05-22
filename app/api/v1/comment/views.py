from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView, RetrieveUpdateAPIView, DestroyAPIView
from rest_framework.mixins import DestroyModelMixin
from rest_framework import permissions

from comment.models import Comment

from .permissions import IsOwnerOrReadOnly
from .serializers import CommentCreateSerializer, CommentListSerializer, CommentDeleteUpdateSerializer


class CommentCreateAPIView(CreateAPIView):
    """Comment creation"""
    queryset = Comment.objects.all()
    serializer_class = CommentCreateSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CommentListAPIView(ListAPIView):
    """Comments list or comments of concrete post"""
    serializer_class = CommentListSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        queryset = Comment.objects.filter(parent=None)
        query = self.request.GET.get('post')
        if query:
            queryset = queryset.filter(post=query)
        return queryset


class CommentUpdateAPIView(RetrieveUpdateAPIView, UpdateAPIView):
    """Comments list or comments of concrete post"""
    queryset = Comment.objects.all()
    serializer_class = CommentDeleteUpdateSerializer
    lookup_field = 'pk'
    permission_classes = [IsOwnerOrReadOnly]


class CommentDeleteAPIView(DestroyAPIView):
    """Delete comment"""
    queryset = Comment.objects.all()
    serializer_class = CommentDeleteUpdateSerializer
    permission_classes = [permissions.IsAdminUser]
    lookup_field = 'pk'
