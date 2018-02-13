from rest_framework import serializers

from .models import Article, Version


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('active', 'created', 'updated')


class VersionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Version
        fields = ('article', 'title', 'text', 'created', 'updated', 'current')
