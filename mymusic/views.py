from django.shortcuts import render
from .models import Album, Users

# Create your views here.

def index(request):
  albums = Album.objects.all()
  return render(request, 'albums/list_album.html', context={'albums':albums})

def add_album(request):
    if request.method == 'GET':
        form = albumForm()
    else:
        form = albumForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='list_album')

    return render(request, "album/add_album.html", {"form": form})

def albums(request):
    if request.method == 'GET':
        form = albumForm()
    else:
        form = albumForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='list_album')

    return render(request, "albums/add_album.html", {"form": form})

def delete_albums(request, pk):
    album = get_object_or_404(Album, pk=pk)
    if request.method == 'POST':
        album.delete()
        return redirect(to='list_album')
    return render(request, "albums/delete_album.html", {"albums": album})