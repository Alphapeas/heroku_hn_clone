from .comment.urls import urlpatterns as comment_urls
from .post.urls import urlpatterns as post_urls


urlpatterns = []
urlpatterns += comment_urls
urlpatterns += post_urls
