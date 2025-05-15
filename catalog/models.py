from django.db import models


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
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
        ordering = ["name", "category"]

    def __str__(self):
        return self.name
