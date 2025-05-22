from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import ListView, DetailView

from .forms import FeedbackForm
from .models import Event


def main(request):
    context = {
        "title": "Главная",
        "page": "home"
    }
    return render(request, "running/main.html", context)


class EventView(ListView):
    model: Event = Event
    template_name: str = "running/events.html"
    context_object_name: str = "events"

    def get_queryset(self):
        queryset = Event.objects.filter(event_view=0)
        event_type = self.request.GET.get('type')
        event_year = self.request.GET.get('year')

        if event_type in ['0', '1']:
            queryset = queryset.filter(event_type=event_type)

        if event_year and event_year.isdigit():
            queryset = queryset.filter(event_date1__year=event_year)

        if event_type == '1':
            return queryset.order_by('event_date1')
        return queryset.order_by('-event_date1')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        event_type = self.request.GET.get('type')
        year_queryset = Event.objects.filter(event_view=0)

        if event_type in ['0', '1']:
            year_queryset = year_queryset.filter(event_type=event_type)
        years = year_queryset.dates('event_date1', 'year')

        if event_type == '1':
            context['years'] = sorted({d.year for d in years})
        else:
            context['years'] = sorted({d.year for d in years}, reverse=True)

        context['current_year'] = self.request.GET.get('year')
        context['current_type'] = event_type

        context['title'] = "События" if event_type == '0' else "Проекты"
        return context


class EventDetailView(DetailView):
    model = Event
    template_name = "running/event_detail.html"
    context_object_name = "event"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        event = self.get_object()

        context['type'] = self.request.GET.get('type', '')
        context['year'] = self.request.GET.get('year', '')
        context['title'] = event.event_name
        return context


def feedback(request):
    if request.method == "POST":
        form = FeedbackForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(
                request,
                "Форма успешно отправлена"
            )
            return redirect(request.META.get('HTTP_REFERER', '/'))
    else:
        form = FeedbackForm()


def politics(request):
    return render(request, "running/politics.html", {"title": "Политика конфиденциальности"})


def contacts(request):
    context = {
        "title": "Контакты",
        'page': "contacts"
    }
    return render(request, "running/contacts.html", context)


def feedback_page(request):
    context = {
        "title": "Обратная связь",
        "page": "feedback_page"
    }
    return render(request, "running/feedback_page.html", context)
