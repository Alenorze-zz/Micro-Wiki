from django.contrib import admin
from django.conf.urls import url

from rest_framework.routers import DefaultRouter

from pages.views import ArcticleViewSet, VersionViewSet


router = DefaultRouter()
router.register(r'api/article', ArcticleViewSet, base_name='article')
router.register(r'api/version', VersionViewSet, base_name='version')
urlpatterns = router.urls


urlpatterns += [
    url(r'^admin/', admin.site.urls),
]
