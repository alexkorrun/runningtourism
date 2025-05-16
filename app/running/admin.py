from django.contrib import admin

from .models import Foto, Event, Feedback

admin.site.register(Foto)
admin.site.register(Event)

admin.site.register(Feedback)

admin.site.site_title = "Админ-панель сайта Беговой Туризм"
admin.site.site_header = "Админ-панель сайта Беговой Туризм"