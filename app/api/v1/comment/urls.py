from rest_framework.routers import DefaultRouter

from app.api.v1.comment.views import CommentViewSet

router = DefaultRouter()
router.register(r'comments', CommentViewSet, basename='comments')
urlpatterns = router.urls
