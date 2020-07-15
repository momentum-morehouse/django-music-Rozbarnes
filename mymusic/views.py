from django.shortcuts import render
from .models import Album, Users

# Create your views here.

def index(request):
  albums = Album.objects.all()
  return render(request, 'albums/list_album.html', context={'albums':albums})