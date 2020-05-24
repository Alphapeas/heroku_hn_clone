from rest_framework import permissions, viewsets, mixins

from comment.models import Comment

from .permissions import IsOwnerOrReadOnly
from .serializers import CommentCreateSerializer, CommentUpdateDeleteSerializer


class CommentViewSet(viewsets.GenericViewSet,
                     mixins.CreateModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.DestroyModelMixin,
                     mixins.UpdateModelMixin):

    def get_serializer_class(self):
        if self.action == 'retrieve' or self.action == 'create':
            return CommentCreateSerializer
        elif self.action == 'destroy' or self.action == 'update' or self.action == 'partial_update':
            return CommentUpdateDeleteSerializer

    def get_queryset(self, pk=None):
        if self.action == 'list':
            query = self.request.GET.get('post')
            if query:
                queryset = Comment.objects.filter(post=query)
                return queryset

        return Comment.objects.all()

    def get_permissions(self):
        if self.action == "retrieve":
            self.permission_classes = [permissions.AllowAny]
        elif self.action == "create":
            self.permission_classes = [permissions.IsAuthenticated]
        elif self.action == "update" or self.action == "partial_update":
            self.permission_classes = [IsOwnerOrReadOnly]
        elif self.action == "destroy":
            self.permission_classes = [permissions.IsAdminUser]
        return super().get_permissions()
