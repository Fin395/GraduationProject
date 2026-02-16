from django.db import models


class Page(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название страницы")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Страница"
        verbose_name_plural = "Страницы"


class Section(models.Model):
    name = models.CharField(max_length=50, verbose_name="Название раздела")
    title = models.CharField(
        max_length=50, verbose_name="Заголовок на странице", blank=True, null=True
    )
    image = models.ImageField(
        upload_to="photos/",
        verbose_name="Изображение на странице",
        blank=True,
        null=True,
    )
    page = models.ForeignKey(
        Page,
        verbose_name="Страница",
        on_delete=models.CASCADE,
        related_name="page_sections",
    )
    content = models.TextField(verbose_name="Текст на странице", blank=True, null=True)
    epigraph = models.TextField(
        verbose_name="Эпиграф",
        blank=True,
        null=True,
    )

    email = models.EmailField(
        unique=True,
        verbose_name="Email",
        blank=True,
        null=True,
    )
    phone_number = models.CharField(
        max_length=25,
        verbose_name="Телефон",
        blank=True,
        null=True,
    )
    country = models.CharField(
        max_length=35,
        verbose_name="Страна",
        blank=True,
        null=True,
    )
    address = models.CharField(
        max_length=50,
        verbose_name="Адрес",
        blank=True,
        null=True,
    )

    TEMPLATE_CHOICES = [
        ("description", "Описание ресторана"),
        ("services", "Перечень услуг"),
        ("contacts", "Контактная информация"),
        ("feedback", "Обратная связь"),
        ("history", "История"),
        ("mission", "Ценности и миссия"),
        ("team", "Наша команда"),
    ]

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Раздел"
        verbose_name_plural = "Разделы"
        # permissions = [('can_unpublish_product', 'Can unpublish product')]


class Table(models.Model):
    seats_amount = models.PositiveSmallIntegerField(verbose_name="Количество мест")
    is_reserved = models.BooleanField(verbose_name="Резерв", default=False)

    def __str__(self):
        return f"Столик № {self.pk}"

    class Meta:
        verbose_name = "Столик"
        verbose_name_plural = "Столики"
