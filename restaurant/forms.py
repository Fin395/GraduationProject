from django import forms

from .mixins import StyleFormMixin
from .models import Page
from django.core.exceptions import ValidationError


FORBIDDEN_WORDS = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']

class PageForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Page
        fields = ['name', 'description', 'image', 'page_category', 'title']

# class ProductModeratorForm(StyleFormMixin, forms.ModelForm):
#     class Meta:
#         model = Product
#         fields = ['is_published']

    # def __init__(self, *args, **kwargs):
    #     super(ProductForm, self).__init__(*args, **kwargs)
    #
    #     self.fields['name'].widget.attrs.update({
    #         'class': 'form-control',  # Добавление CSS-класса для стилизации поля
    #         'placeholder': 'Введите наименование'  # Текст подсказки внутри поля
    #     })
    #
    #     self.fields['description'].widget.attrs.update({
    #         'class': 'form-control',  # Добавление CSS-класса для стилизации поля
    #         'placeholder': 'Введите описание'  # Текст подсказки внутри поля
    #     })
    #
    #     self.fields['image'].widget.attrs.update({
    #         'class': 'form-control',  # Добавление CSS-класса для стилизации поля
    #         'placeholder': 'Загрузите изображение'  # Текст подсказки внутри поля
    #     })
    #
    #     self.fields['category'].widget.attrs.update({
    #         'class': 'form-control'
    #     })
    #
    #     self.fields['price'].widget.attrs.update({
    #         'class': 'form-control',  # Добавление CSS-класса для стилизации поля
    #         'placeholder': 'Укажите цену'  # Текст подсказки внутри поля
    #     })

    def clean_name(self):
        name = self.cleaned_data.get('name')
        for word in FORBIDDEN_WORDS:
            if word.lower() in name.lower():
                raise ValidationError(f"Слово {word} не может содержаться в наименовании страницы")
        return name

    def clean_description(self):
        description = self.cleaned_data.get('description')
        for word in FORBIDDEN_WORDS:
            if word.lower() in description.lower():
                raise ValidationError(f"Слово '{word}' не может содержаться в описании страницы")
        return description

    def clean_title(self):
        title = self.cleaned_data.get('title')
        for word in FORBIDDEN_WORDS:
            if word.lower() in title.lower():
                raise ValidationError(f"Слово '{word}' не может содержаться в заголовке на странице")
        return title
