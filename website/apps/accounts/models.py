from django.db import models
from django.contrib.auth.models import User


class UserInterest(models.Model):
    name = models.CharField(max_length=64, unique=True, verbose_name="Название хобби")
    normalized_name = models.CharField(max_length=64, unique=True, verbose_name="Нормализованное название хобби")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Хобби"
        verbose_name_plural = "Хобби"
        indexes = [
            models.Index(fields=['name'])
        ]


class UserPersona(models.Model):
    name = models.CharField(max_length=64, unique=True, verbose_name="Название роли")
    normalized_name = models.CharField(max_length=64, unique=True, verbose_name="Нормализованное название роли")
    description = models.CharField(max_length=200, verbose_name="Описание")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Роль"
        verbose_name_plural = "Роли"
        indexes = [
            models.Index(fields=['name'])
        ]


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    bio = models.CharField(max_length=500, blank=True, null=True, verbose_name="Биография")
    website = models.URLField(max_length=200, blank=True, null=True, verbose_name="Вебсайт пользователя")
    linkedin_url = models.URLField(max_length=200, blank=True, null=True, verbose_name="Ссылка на LinkedIn")
    twitter_url = models.URLField(max_length=200, blank=True, null=True, verbose_name="Ссылка на Twitter")
    youtube_url = models.URLField(max_length=200, blank=True, null=True, verbose_name="Ссылка на YouTube")
    is_full_name_displayed = models.BooleanField(default=True, verbose_name="Отображать ли полное имя пользователя")
    persona = models.ForeignKey(UserPersona, on_delete=models.SET_NULL, blank=True, null=True)
    interests = models.ManyToManyField(UserInterest, blank=True)

    class Meta:
        verbose_name = "Профиль"
        verbose_name_plural = "Профили"
        indexes = [
            models.Index(fields=['user'])
        ]
