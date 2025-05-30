from django.db import models


class Blog(models.Model):
    title = models.CharField(
        max_length=250,
        verbose_name="Название заголовка",
        help_text="Введите название заголовка",
    )
    content = models.TextField(
        blank=True, null=True, verbose_name="Текст", help_text="Введите текстовое описание"
    )
    image = models.ImageField(
        upload_to="blog/image",
        blank=True,
        null=True,
        verbose_name="Изображение",
        help_text="Загрузите изображение",
    )
    publication_attribute = models.BooleanField(
        default=False,
        verbose_name="Опубликовано",
        help_text="Отметьте, чтобы опубликовать запись на сайте",
    )
    views_count = models.PositiveIntegerField(
        default=0,
        verbose_name="Количество просмотров",
        editable=False,
        help_text="Автоматически увеличивается при каждом просмотре страницы.",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Моя запись"
        verbose_name_plural = "Мои записи"
        ordering = ['-created_at']

    def __str__(self):
        return self.title
