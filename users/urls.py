from django.contrib.auth.views import (
    LogoutView,
    PasswordResetCompleteView,
    PasswordResetConfirmView,
    PasswordResetDoneView,
    PasswordResetView,
)
from django.urls import path, reverse_lazy

from users.apps import UsersConfig
from users.views import (
    ConfirmationMessageView,
    CustomLoginView,
    UserDetailView,
    UserRegisterView,
    UserUpdateView,
    email_verification,
    UsersListView,
    UserBlockView,
)

app_name = UsersConfig.name

urlpatterns = [
    path(
        "login/",
        CustomLoginView.as_view(template_name="users/login.html"),
        name="login",
    ),
    path("register/", UserRegisterView.as_view(), name="register"),
    path("email-confirm/<str:token>/", email_verification, name="email_confirm"),
    path("logout/", LogoutView.as_view(next_page="users:login"), name="logout"),
    path("<int:pk>/user/", UserDetailView.as_view(), name="user_detail"),
    path("<int:pk>/user/update/", UserUpdateView.as_view(), name="user_update"),
    path("confirm/", ConfirmationMessageView.as_view(), name="confirm"),
    path("email-confirm/<str:token>/", email_verification, name="email_confirm"),
    path(
        "password_reset/",
        PasswordResetView.as_view(
            template_name="users/password_reset_form.html",
            email_template_name="users/password_reset_email.html",
            success_url=reverse_lazy("users:password_reset_done"),
        ),
        name="password_reset",
    ),
    path(
        "password_reset/done/",
        PasswordResetDoneView.as_view(template_name="users/password_reset_done.html"),
        name="password_reset_done",
    ),
    path(
        "password_reset/<uidb64>/<token>/",
        PasswordResetConfirmView.as_view(
            template_name="users/password_reset_confirm.html",
            success_url=reverse_lazy("users:password_reset_complete"),
        ),
        name="password_reset_confirm",
    ),
    path(
        "password_reset/complete/",
        PasswordResetCompleteView.as_view(
            template_name="users/password_reset_complete.html"
        ),
        name="password_reset_complete",
    ),
    path("users/", UsersListView.as_view(), name="users_list"),
    path("users/<int:pk>/user/block/", UserBlockView.as_view(), name="user_block"),
]
