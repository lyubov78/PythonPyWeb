from django.urls import path, include
from .views import TagViewSet
from rest_framework.routers import DefaultRouter

app_name = 'api_tags'

router = DefaultRouter()
router.register(r'tags_viewset', TagViewSet, basename='tags_viewset')

urlpatterns = [
    path('', include(router.urls)),
]
