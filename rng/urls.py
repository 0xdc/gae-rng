from django.conf.urls import url

from . import views

app_name = "rng"
urlpatterns = [
    url(r'rng/?$', views.random_number_generator, name="rng"),
    url(r'used/?$', views.usedindex, name="index"),
    url(r'^$', views.hpv, name="hp"),
]
