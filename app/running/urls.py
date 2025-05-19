from django.urls import path

from . import views

urlpatterns: list[str] = [
    path("", views.main, name="home"),

    path("events/", views.EventView.as_view(), name="events"),
    path("events/<int:pk>/", views.EventDetailView.as_view(), name="event_detail"),

    path('feedback/', views.feedback, name='feedback'),
    path("politics/", views.politics, name="politics"),
    path("contacts/", views.contacts, name="contacts"),
]
