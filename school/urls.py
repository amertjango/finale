from django.urls import path
from . import views

urlpatterns = [
    path('agenda', views.agenda_list, name='agenda_list'),
    path('', views.home, name='home'),
    path('tarieven', views.tarieven, name='tarieven'),
    path('overons', views.overons, name='overons'),
    path('contact', views.contact, name='contact'),
]
