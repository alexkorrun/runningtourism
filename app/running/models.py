from django.db import models

from mixins import StrMixin


class Foto(StrMixin, models.Model):
    title = models.CharField(max_length=255, verbose_name="Название изображения")
    image = models.ImageField(verbose_name="Изображения")

    class Meta:
        verbose_name = "Изображение"
        verbose_name_plural = "Изображения"


class Event(StrMixin, models.Model):
    EVENT_VIEW_CHOICES = [
        (0, "События"),
        (1, "Проекты"),
    ]
    EVENT_TYPE_CHOICES = [
        (0, "события"),
        (1, "проекты"),
    ]

    event_view = models.SmallIntegerField(
        choices=EVENT_VIEW_CHOICES,
        verbose_name="Видимость события"
    )
    event_type = models.SmallIntegerField(
        choices=EVENT_TYPE_CHOICES,
        verbose_name="Тип события"
    )

    event_year = models.IntegerField(verbose_name="Год события")
    event_date1 = models.DateField(verbose_name="Дата начала")
    event_date2 = models.DateField(verbose_name="Дата конца")
    event_name = models.CharField(max_length=255, verbose_name="Названия события")
    event_description = models.TextField(verbose_name="Описания события")
    event_video = models.URLField(blank=True, verbose_name="Ссылка на видео")
    event_album = models.URLField(blank=True, verbose_name="Ссылка на фотоальбом")
    event_route = models.URLField(blank=True, verbose_name="Ссылка на маршрут")
    event_report = models.TextField(blank=True, verbose_name="Отчет события")

    event_foto = models.ForeignKey(
        Foto,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        verbose_name="Изображения события"
    )

    class Meta:
        verbose_name = "Событие"
        verbose_name_plural = "События"


class Feedback(StrMixin, models.Model):
    name = models.CharField(
        max_length=100,
        blank=False,
        null=False,
        verbose_name="Имя"
    )
    phone = models.CharField(
        max_length=110,
        blank=True,
        null=True,
        verbose_name="Номер телефона"
    )

    class Meta:
        verbose_name = "Обратная связь"
        verbose_name_plural = "Обратная связь"