from django.shortcuts import render
from django.utils import timezone
from .models import Event

def agenda_list(request):
    agendaposts = Event.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'school/agenda_list.html', {'agendaposts': agendaposts})

def home(request):
    return render(request, 'school/index.html')

def overons(request):
    return render(request, 'school/overons.html')

def tarieven(request):
    return render(request, 'school/tarieven.html')

def contact(request):
    return render(request, 'school/contact.html')
