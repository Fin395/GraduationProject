from django.db import models

from users.models import User


class Page(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name='Название страницы'
    )
    owner = models.ForeignKey(
        User,
        verbose_name='Владелец',
        on_delete=models.SET_NULL,
        related_name='pages',
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Страница'
        verbose_name_plural = 'Страницы'


class Section(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name='Название раздела'
    )
    title = models.CharField(
        max_length=50,
        verbose_name='Заголовок на странице'
    )
    image = models.ImageField(
        upload_to='photos/',
        verbose_name="Изображение на странице"
    )
    page = models.ForeignKey(Page, verbose_name='Страница', on_delete=models.CASCADE, related_name='page_sections')
    content = models.TextField(
        verbose_name="Текст на странице"
    )
    epigraph = models.TextField(
        verbose_name="Эпиграф",
        blank=True,
        null=True,
    )
    email = models.EmailField(
        unique=True,
        verbose_name='Email',
        blank=True,
        null=True,
    )
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

    owner = models.ForeignKey(
        User,
        verbose_name='Владелец',
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='sections')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Раздел'
        verbose_name_plural = 'Разделы'
        # permissions = [('can_unpublish_product', 'Can unpublish product')]
