from django.db import models

from mixins import StrMixin


class Foto(StrMixin, models.Model):
    title = models.CharField(max_length=255)
    image = models.BinaryField()


class Event(StrMixin, models.Model):
    EVENT_VIEW_CHOICES = [
        (0, "Видимое событие"),
        (1, "Скрытое событие"),
    ]
    EVENT_TYPE_CHOICES = [
        (0, "выполненное событие"),
        (1, "будущее событие"),
    ]

    event_view = models.SmallIntegerField(choices=EVENT_VIEW_CHOICES)
    event_type = models.SmallIntegerField(choices=EVENT_TYPE_CHOICES)

    event_year = models.IntegerField()
    event_date1 = models.DateField()
    event_date2 = models.DateField()
    event_name = models.CharField(max_length=255)
    event_description = models.TextField()
    event_video = models.URLField(blank=True)
    event_album = models.URLField(blank=True)
    event_route = models.URLField(blank=True)
    event_report = models.TextField(blank=True)
    event_foto = models.ForeignKey(Foto, null=True, blank=True, on_delete=models.SET_NULL)