from rest_framework import routers
from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register'),
    path("login/",TokenObtainPairView.as_view(),name="login"),
    path("token/refresh/",TokenRefreshView.as_view(), name="token_refresh"),
    path("profile/",views.ProfileView.as_view(), name="profile"),
    path("change-password/",views.PasswordChangeView.as_view(), name="change-password"),
]