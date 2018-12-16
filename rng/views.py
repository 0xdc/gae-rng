from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.views import generic

from .models import UsedNumber

def random_number_generator(request):
    rand = UsedNumber.new()
    return HttpResponse(rand.number, content_type="text/plain")

class HomePageView(TemplateView):
    template_name = "rng/random.html"

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['random'] = UsedNumber.new().number
        return context

hpv = HomePageView.as_view()

class UsedList(generic.ListView):
    model = UsedNumber
    template_name = "rng/list.html"

usedindex = UsedList.as_view()
