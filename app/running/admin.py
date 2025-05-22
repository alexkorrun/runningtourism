from django.contrib import admin
from .models import Foto, Event, Feedback


@admin.register(Foto)
class FotoAdmin(admin.ModelAdmin):
    list_display = ("title",)
    search_fields = ("title",)


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ("event_name", "event_year", "event_type", "event_view")
    list_filter = ("event_view", "event_type", "event_year")
    search_fields = ("event_name", "event_description")
    date_hierarchy = "event_date1"
    ordering = ("-event_year",)


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ("name", "phone")
    search_fields = ("name", "phone")


admin.site.site_title = "Админ-панель сайта Беговой Туризм"
admin.site.site_header = "Админ-панель сайта Беговой Туризм"
