from django.conf.urls.static import static
from django.urls import path
from django.urls.conf import re_path
from . import views
from django.conf import settings

urlpatterns = [
    re_path('^.*$', views.index),
]
