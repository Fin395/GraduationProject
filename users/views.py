import secrets

from django.contrib.auth.views import LoginView
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import DetailView, TemplateView
from django.views.generic.edit import CreateView

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
        context['pages'] = Page.objects.prefetch_related('page_sections').all()
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

    # def form_valid(self, form):
    #     user = form.save()
    #     login(self.request, user)
    #     send_mail(
    #         subject='Добро пожаловать в наш сервис',
    #         message='Спасибо, что зарегистрировались в нашем сервисе!',
    #         from_email=EMAIL_HOST_USER,
    #         recipient_list=[user.email]
    #     )
    #     return super().form_valid(form)


class CustomLoginView(LoginView):
    template_name = 'users/login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pages'] = Page.objects.prefetch_related('page_sections').all()
        context['user'] = self.request.user

        return context


class ProfileView(TemplateView):
    template_name = 'users/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pages'] = Page.objects.prefetch_related('page_sections').all()
        context['user'] = self.request.user

        return context



