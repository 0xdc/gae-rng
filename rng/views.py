from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import TemplateView

import random
import functools

from .models import UsedNumber

_RINT = functools.partial(random.SystemRandom().randint, 0)
_PRIME = 2 ** 127 - 1

def random_number_generator(request):
    rand = str(_RINT(_PRIME))
    UsedNumber.objects.get_or_create(number=rand, defaults={'number': rand})
    return HttpResponse(rand)

class HomePageView(TemplateView):
    template_name = "rng/random.html"

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['random'] = _RINT(_PRIME)
        return context

hpv = HomePageView.as_view()
