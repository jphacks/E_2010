from django.urls import path, include
from . import views
urlpatterns = [
    # path('login/', views.loginform),
    # path('logout/', views.loginform),
    path('login/', views.RegisterProfile.as_view()),
    path('login/<int:pk>/', views.RegisterProfile.as_view())
]
