from django.urls import path

from authentication.views import get_csrf, get_current_user, login_view, logout_view

urlpatterns = [
    path("csrf", get_csrf, name="get-csrf"),
    path("login", login_view, name="login"),
    path("logout", logout_view, name="logout"),
    path("me", get_current_user, name="current-user"),
]
