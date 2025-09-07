from django.db import models

from users.models import User


class Restaurant(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name="Название ресторана",
    )

    epigraph = models.TextField(
        verbose_name="Эпиграф",
    )
    description = models.TextField(
        verbose_name="Описание ресторана"
    )
    image = models.ImageField(upload_to="photos/", verbose_name="Изображение ресторана")
    services = models.TextField(verbose_name="Услуги ресторана")
    email = models.EmailField(unique=True, verbose_name='Email')
    phone_number = models.CharField(
        max_length=25,
        verbose_name='Телефон',
        blank=True,
        null=True,
    )
    country = models.CharField(
        max_length=35,
        verbose_name='Страна',
        blank=True,
        null=True,
    )
    address = models.CharField(
        max_length=50,
        verbose_name='Адрес',
        blank=True,
        null=True,
    )
    client_name = models.CharField(max_length=50, verbose_name='Имя')
    client_phone_number = models.CharField(max_length=25, verbose_name='Телефон')
    client_message = models.TextField(verbose_name='Сообщение')
    owner = models.ForeignKey(
        User,
        verbose_name='Владелец',
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='restaurants')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Ресторан'
        verbose_name_plural = 'Рестораны'
        # permissions = [('can_unpublish_product', 'Can unpublish product')]
