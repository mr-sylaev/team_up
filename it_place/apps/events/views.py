from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse
from .models import Event
from .forms import EventCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin


class ListEventView(LoginRequiredMixin, ListView):
    model = Event

    def get_context_data(self, **kwargs):
        context = super(ListEventView, self).get_context_data(**kwargs)
        # context['now'] = timezone.now()
        return context


class DetailEventView(LoginRequiredMixin, DetailView):
    model = Event

    def get_context_data(self, **kwargs):
        context = super(DetailEventView, self).get_context_data(**kwargs)
        # context['now'] = timezone.now()
        return context


class CreateEventView(CreateView):
    template_name = 'events/create.html'
    form_class = EventCreationForm

    def get_success_url(self):
        return reverse('event:detail', args=(self.object.pk,))

    def form_valid(self, form):
        form.instance.create_by = self.request.user
        return super(CreateEventView, self).form_valid(form)
