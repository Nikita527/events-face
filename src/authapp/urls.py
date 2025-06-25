from django.urls import path

from rest_framework_simplejwt.views import TokenRefreshView

from .views import RegisterView, LoginView, LogoutView

urlpatterns = [
    path("auth/register", RegisterView.as_view()),
    path("auth/login", LoginView.as_view()),
    path("auth/token/refresh", TokenRefreshView.as_view()),
    path("auth/logout", LogoutView.as_view()),
]
