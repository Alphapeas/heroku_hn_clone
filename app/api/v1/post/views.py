from django.shortcuts import get_object_or_404
from django.db.models import Count

from rest_framework import permissions
from rest_framework.generics import ListAPIView, RetrieveAPIView, DestroyAPIView, CreateAPIView, RetrieveUpdateAPIView
from rest_framework.mixins import CreateModelMixin, ListModelMixin
from rest_framework.response import Response
from rest_framework.views import APIView

from post.models import Post
from .permissions import IsOwnerOrReadOnly
from .serializers import PostSerializers, PostUpdateCreateSerializers
from .paginations import PostApiPagination


class PostListAPIView(ListAPIView, CreateModelMixin):
    serializer_class = PostSerializers
    queryset = Post.objects.all()
    pagination_class = PostApiPagination
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get_queryset(self):
        posts = Post.objects.filter().annotate(
            rating=Count('votes')
        )
        return posts


class PostDetailAPIView(RetrieveAPIView):
    serializer_class = PostSerializers
    lookup_field = 'pk'
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        posts = Post.objects.filter().annotate(
            rating=Count('votes')
        )
        return posts


class PostCreateAPIView(CreateAPIView, ListModelMixin):
    queryset = Post.objects.all()
    serializer_class = PostUpdateCreateSerializers
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class PostUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostUpdateCreateSerializers
    permission_classes = [IsOwnerOrReadOnly]
    lookup_field = 'pk'

    def perform_update(self, serializer):
        serializer.save(modified_by=self.request.user)


class PostDeleteAPIView(DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializers
    permission_classes = [permissions.IsAdminUser]
    lookup_field = 'pk'


class AddOrDeleteVoteAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        post = get_object_or_404(Post, id=pk)
        if post.votes.filter(id=self.request.user.id).exists():
            post.votes.remove(request.user)
            return Response(status=204)
        post.votes.add(request.user)
        return Response(status=201)
