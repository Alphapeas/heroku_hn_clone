from django.urls import path
from rest_framework.routers import DefaultRouter

from . import views


urlpatterns = [
    path('post/<int:pk>/vote/', views.AddOrDeleteVoteAPIView.as_view(), name='Adding or deleting vote if it exists'),
]

router = DefaultRouter()
router.register(r'news', views.PostViewSet, basename='news')
urlpatterns += router.urls
