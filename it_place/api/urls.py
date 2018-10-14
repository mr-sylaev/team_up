from django.conf.urls import url, include
from rest_framework import routers
from api.user.views import ItUserViewSet


router = routers.DefaultRouter()
router.register(r'user', ItUserViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),
]