from django.db import models


class Topic(models.Model):
    name = models.CharField(max_length=50, verbose_name="Тема новостей")
    description = models.CharField(max_length=250, verbose_name="О чем пишем в этой теме")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Тема новостей"
        verbose_name_plural = "Темы новостей"


class News(models.Model):
    title = models.CharField(max_length=150, verbose_name="Заголовок")
    content = models.TextField(verbose_name="Содержание")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    update_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")
    is_published = models.BooleanField(default=False, verbose_name="Опубликовано")
    topic = models.ForeignKey(Topic, on_delete=models.PROTECT, verbose_name="Категория")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"
        ordering = ['-created_at']

