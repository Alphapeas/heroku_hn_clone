from django.shortcuts import get_object_or_404
from django.db.models import Count

from rest_framework import permissions, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from post.models import Post
from .permissions import IsOwnerOrReadOnly
from .serializers import (
    PostCUDSerializer,
    PostListSerializer,
    PostDetailSerializer
)
from .paginations import PostApiPagination


class PostViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    pagination_class = PostApiPagination

    def get_serializer_class(self):
        if self.action == "list":
            return PostListSerializer
        elif self.action == 'create' or self.action == 'delete' or self.action == 'update'\
                or self.action == "partial_update":
            return PostCUDSerializer
        else:
            return PostDetailSerializer

    def get_queryset(self, pk=None):
        return Post.objects.filter().annotate(rating=Count('votes'))

    def get_permissions(self):
        if self.action == "list" or self.action == "retrieve":
            self.permission_classes = [permissions.AllowAny]
        elif self.action == "create":
            self.permission_classes = [permissions.IsAuthenticated]
        elif self.action == "update" or self.action == "partial_update":
            self.permission_classes = [IsOwnerOrReadOnly]
        elif self.action == "destroy":
            self.permission_classes = [permissions.IsAdminUser]
        return super().get_permissions()


class AddOrDeleteVoteAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        post = get_object_or_404(Post, id=pk)
        if post.votes.filter(id=self.request.user.id).exists():
            post.votes.remove(request.user)
            return Response(status=204)
        post.votes.add(request.user)
        return Response(status=201)
