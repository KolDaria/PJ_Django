from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name="Email")
    phone = models.CharField(max_length=15, blank=True, null=True, verbose_name="Телефон",
                             help_text="Введите номер телефона")
    country = models.CharField(max_length=50, blank=True, null=True, verbose_name="Страна",
                               help_text="Укажите страну")
    avatar = models.ImageField(upload_to='users/avatars/', verbose_name="Аватар", blank=True, null=True,
                               help_text="Загрузите свой аватар")

    token = models.CharField(max_length=100, verbose_name="Token", blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.email


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30, blank=True, verbose_name="Имя", help_text="Введите имя")
    last_name = models.CharField(max_length=30, blank=True, verbose_name="Фамилия", help_text="Введите фамилию")
    birth_date = models.DateField(null=True, blank=True, verbose_name="Дата рождения",
                                  help_text="Введите дату рождения")
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, verbose_name="Фото профиля",
                                        help_text="Добавьте фото профиля")


    def __str__(self):
        return str(self.user.username)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
