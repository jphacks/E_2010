from django.urls import path, include
from . import views
urlpatterns = [
    # path('login/', views.loginform),
    # path('logout/', views.loginform),
    path('signup/', views.RegisterProfile.as_view()),
    path('signup/<int:pk>/', views.RegisterProfile.as_view()),
    path('login/', views.LoginView.as_view()),
    path('login/<int:pk>/', views.LoginView.as_view())
]
