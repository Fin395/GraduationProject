from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = None
    name = models.CharField(
        max_length=35,
        verbose_name='Имя',
        blank=True,
        null=True,
        help_text='Укажите имя',
    )
    surname = models.CharField(
        max_length=35,
        verbose_name='Фамилия',
        blank=True,
        null=True,
        help_text='Укажите фамилию',
    )
    email = models.EmailField(unique=True, verbose_name='Email')

    avatar = models.ImageField(
        upload_to='users/avatars/',
        verbose_name='Аватар',
        blank=True,
        null=True,
        help_text='Загрузите свой аватар (необязательно)'
    )
    phone_number = models.CharField(
        max_length=25,
        verbose_name='Телефон',
        blank=True,
        null=True,
        help_text='Введите номер телефона (необязательно)'
    )
    country = models.CharField(
        max_length=35,
        verbose_name='Страна',
        blank=True,
        null=True,
        help_text='Введите страну (необязательно)'
    )
    token = models.CharField(max_length=100, verbose_name='Token', blank=True, null=True)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.email