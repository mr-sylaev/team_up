from django.http import HttpResponseRedirect,HttpResponse
from django.views.generic import TemplateView,DetailView,CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Reit
from apps.events.forms import ReitForm
from django.urls import reverse
from django.shortcuts import render


class HomePageView(LoginRequiredMixin, TemplateView):
    template_name = 'main/home.html'
    redirect_field_name = 'redirect_to'


def index(request):
    form = ReitForm()
    data = {'form':form}
    return render(request,'main/home.html',data)


# class CreateReitView(CreateView):
#     template_name = 'main/home.html'
#     form_class = ReitForm
#
#     def get_success_url(self):
#         return reverse('reit:details', args=(self.object.pk,))
#
#     def form_valid(self, form):
#         form.instance.create_by = self.request.user
#         return super(CreateReitView, self).form_valid(form)


    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['it_user'] = self.request.user
        return context