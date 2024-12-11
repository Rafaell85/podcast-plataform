from django.shortcuts import render
from .models import Podcast

def home(request):
    podcasts = Podcast.objects.all()  # Busca todos os podcasts
    return render(request, 'core/home.html', {'podcasts': podcasts})
