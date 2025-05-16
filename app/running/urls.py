from django.urls import path

from . import views


urlpatterns: list[str] = [
    path("", views.index, name="main")
]