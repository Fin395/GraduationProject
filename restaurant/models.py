from django.db import models

from users.models import User


class PageCategory(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name="Название раздела",
        help_text="Введите название раздела",
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Название раздела"
        verbose_name_plural = "Названия разделов"


class Page(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Название страницы",
    )

    title = models.CharField(
        max_length=100,
        verbose_name="Заголовок на странице",
    )
    epigraph = models.TextField(
        verbose_name="Эпиграф",
        blank=True,
        null=True,
    )

    description = models.TextField(
        verbose_name="Описание на странице",
        blank=True,
        null=True,
    )
    image = models.ImageField(
        upload_to="photos/",
        blank=True,
        null=True,
        verbose_name="Изображение на странице",
    )
    page_category = models.ForeignKey(PageCategory, on_delete=models.CASCADE, related_name='pages')

    owner = models.ForeignKey(User, verbose_name='Владелец', blank=True, null=True, on_delete=models.SET_NULL, related_name='owner_pages')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Страница"
        verbose_name_plural = "Страницы"
        # permissions = [('can_unpublish_product', 'Can unpublish product')]