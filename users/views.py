import secrets

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.views import LoginView
from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView

from config.settings import EMAIL_HOST_USER
from restaurant.models import Page
from .forms import UserRegistrationForm
from django.core.mail import send_mail
from django.contrib.auth import login

from .models import User


class UserRegisterView(CreateView):
    form_class = UserRegistrationForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pages'] = Page.objects.all()
        context['user'] = self.request.user

        return context

    def form_valid(self, form):
        user = form.save()
        user.is_active = False
        token = secrets.token_hex(16)
        user.token = token
        user.save()
        host = self.request.get_host()
        url = f'http://{host}/users/email-confirm/{token}/'
        send_mail(
            subject='Подтверждение почты',
            message=f'Привет! Перейди по ссылке {url} для подтверждения почты!',
            from_email=EMAIL_HOST_USER,
            recipient_list=[user.email]
        )
        return super().form_valid(form)


def email_verification(request, token):
    user = get_object_or_404(User, token=token)
    user.is_active = True
    user.save()
    send_mail(
        subject='Добро пожаловать в наш ресторан',
        message='Спасибо, что зарегистрировались в нашем сервисе!',
        from_email=EMAIL_HOST_USER,
        recipient_list=[user.email]
    )
    return redirect(reverse('users:login'))


class CustomLoginView(LoginView):
    template_name = 'users/login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pages'] = Page.objects.all()
        context['user'] = self.request.user

        return context

    def get_success_url(self, **kwargs):
        return reverse_lazy('users:user_detail', kwargs={'pk': self.request.user.pk})


class UserDetailView(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'users/user_detail.html'
    # login_url = reverse_lazy('users:login')

    def get_object(self, queryset=None):
        user_to_view = super().get_object(queryset)
        user = self.request.user
        if user_to_view != user:
            raise PermissionDenied
        return user_to_view

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pages'] = Page.objects.all()
        context['user'] = self.request.user
        context['image_path'] = '/static/images/профиль.jpg'

        return context


class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserRegistrationForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')


    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_queryset(self, **kwargs):
        pk = self.kwargs.get('pk')
        user = get_object_or_404(User, pk=pk)
        if self.request.user != user:
            raise PermissionDenied
        return User.objects.filter(pk=self.request.user.pk)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pages'] = Page.objects.all()
        context['user'] = self.request.user

        return context
