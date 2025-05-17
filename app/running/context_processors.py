from .forms import FeedbackForm


def feedback_form(request):
    return {'form': FeedbackForm()}


def global_filters(request):
    current_type = request.GET.get('type', '')
    current_year = request.GET.get('year', '')

    return {
        'form': FeedbackForm(),
        'current_type': current_type,
        'current_year': current_year,
    }