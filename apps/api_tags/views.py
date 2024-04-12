from django.shortcuts import render
from apps.db_train_alternative.models import Tag
from rest_framework.viewsets import ModelViewSet
from .serializers import TagModelSerializer
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters


class TagPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 1000


class TagViewSet(ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagModelSerializer
    http_method_names = ['get', 'post']
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'slug_name']
    search_fields = ['name']
    ordering_fields = ['name', 'slug_name']
