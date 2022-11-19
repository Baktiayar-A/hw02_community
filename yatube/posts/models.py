from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Post(models.Model):
    text = models.TextField(
        verbose_name="Текст",
        help_text="В свободной форме"
    )
    pub_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата публикации"
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts',
        verbose_name="Автор",
        help_text="Выберите из списка"
    )
    group = models.ForeignKey(
        "Group",
        models.SET_NULL,
        blank=True, null=True,
        related_name='posts',
        verbose_name="Группа",
        help_text="Выберите из списка"
    )

    class Meta:
        ordering = ('-pub_date',)
        verbose_name_plural = "Посты пользователей"

    def __str__(self):
        return self.text


class Group(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name="Название",
        help_text="Название группы, не более 200 символов"
    )
    slug = models.SlugField(
        unique=True,
        verbose_name="URL",
        help_text="URL Адресc группы"
    )
    description = models.TextField(
        verbose_name="Описание",
        help_text="В свободной форме"
    )

    class Meta:
        verbose_name_plural = "Группы"

    def __str__(self):
        return self.title
