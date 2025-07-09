from django.urls import include, path
from rest_framework.routers import SimpleRouter

from .views import CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet

v1_route = SimpleRouter()
v1_route.register(
    'posts',
    PostViewSet,
    basename='posts',
)
v1_route.register(
    'groups',
    GroupViewSet,
    basename='groups',
)
v1_route.register(
    r'posts/(?P<post_id>\d+)/comments',
    CommentViewSet,
    basename='comments',
)
v1_route.register(
    'follow',
    FollowViewSet,
    basename='follow',
)

urlpatterns = [
    path('v1/', include(v1_route.urls)),
    path('v1/', include('djoser.urls.jwt')),
]
