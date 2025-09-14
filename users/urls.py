from django.urls import path
from users.apps import UsersConfig
from django.contrib.auth.views import LogoutView
from users.views import UserRegisterView, ProfileView, CustomLoginView, email_verification, UserDetailView, \
    UserUpdateView

app_name = UsersConfig.name

urlpatterns = [
    path('login/', CustomLoginView.as_view(template_name='users/login.html'), name='login'),
    path('register/', UserRegisterView.as_view(), name='register'),
    path('email-confirm/<str:token>/', email_verification, name='email_confirm'),
    path('logout/', LogoutView.as_view(next_page='users:login'), name='logout'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('<int:pk>/user/', UserDetailView.as_view(), name='user_detail'),
    path('<int:pk>/user/update/', UserUpdateView.as_view(), name='user_update'),
]