from django.db import models

from users.models import User


# Create your models here.
class Category(models.Model):
    name = models.CharField(
        max_length=150, verbose_name="Наименование категории", help_text="Введите наименование категории"
    )
    description = models.TextField(
        blank=True, null=True, verbose_name="Описание категории", help_text="Введите описание категории"
    )

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(
        max_length=150, verbose_name="Наименование товара", help_text="Введите наименование товара"
    )
    description = models.TextField(
        blank=True, null=True, verbose_name="Описание товара", help_text="Введите описание товара"
    )
    image = models.ImageField(
        upload_to="product/image",
        blank=True,
        null=True,
        verbose_name="Изображение",
        help_text="Загрузите изображение товара",
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        related_name="products",
        verbose_name="Категория",
        help_text="Введите категорию товара",
        null=True)
    purchase_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена за покупки", default=0.00)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='products', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
        ordering = ["name", "category"]

    def __str__(self):
        return self.name


class Contact(models.Model):
    name = models.CharField(
        max_length=150,
        verbose_name="Наименование контакта",
        help_text="Введите наименование контакта",
    )
    email = models.EmailField(
        max_length=254,
        verbose_name="Email",
        help_text="Введите email",
    )
    phone_number = models.CharField(
        max_length=20,
        blank=True,
        verbose_name="Номер телефона",
        help_text="Введите номер телефона",
    )
    address = models.TextField(
        blank=True,
        verbose_name="Адрес",
        help_text="Введите адрес",
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания",
    )

    class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = "Контакты"
        ordering = ["name"]

    def __str__(self):
        return self.name
