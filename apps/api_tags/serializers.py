from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from apps.db_train_alternative.models import Tag


class TagModelSerializer(ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name', 'slug_name']
