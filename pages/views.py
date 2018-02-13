from rest_framework import viewsets, views

from .serializers import ArticleSerializer, VersionSerializer
from .models import Article, Version


class ArcticleViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()

class VersionViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = VersionSerializer
    queryset = Version.objects.all()
