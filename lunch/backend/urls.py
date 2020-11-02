from django.urls import path
from rest_framework import routers

from .views import UserViewSet, TestViewSet


router = routers.DefaultRouter(trailing_slash=False)
# router = routers.SimpleRouter(trailing_slash=False)
router.register(r'users', UserViewSet)
router.register(r'tests', TestViewSet)
