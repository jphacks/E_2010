from django.urls import path
from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r'', views.UserViewSet)

urlpatterns = [
    # path('login/', views.loginform),
    # path('logout/', views.loginform),
    path('signup/', views.RegisterProfile.as_view()),
    path('signup/<int:pk>/', views.RegisterProfile.as_view()),
    path('login/', views.LoginView.as_view()),
    path('login/<int:pk>/', views.LoginView.as_view()),
    url(r'^users/', include(router.urls)),
]
