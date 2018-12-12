from django.conf.urls import url

from . import views

app_name = "rng"
urlpatterns = [
    url('rng/$', views.random_number_generator, name="rng"),
    url('', views.hpv, name="hp"),
]
