from rest_framework import routers

from django.urls import path, include

from .views import UserViewSet, GroupViewSet

router = routers.DefaultRouter()
router.register("users", UserViewSet)
router.register("groups", GroupViewSet)


urlpatterns = [
    path("", include(router.urls)),
    ]
