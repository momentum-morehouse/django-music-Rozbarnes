from django.shortcuts import render, redirect, get_object_or_404
from django.shortcuts import render
from .models import Album, Users
from .forms import albumForm, DetailForm

 
#from .models import Album, Details
#from .forms import albumForm, DetailForm

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
            return redirect(to='home')

    return render(request, "albums/add_album.html", {"form": form})

def albums(request):
    if request.method == 'GET':
        form = albumForm()
    else:
        form = albumForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='list_album')

    return render(request, "albums/add_album.html", {"form": form})
def edit_album(request, pk):
    albums = get_object_or_404(Album, pk=pk)
    if request.method == 'GET':
        form = albumForm(instance=albums)
    else:
        form = albumForm(data=request.POST, instance=albums)
    
    if form.is_valid():
        form.save()
        return redirect(to='list_album')

    return render(request, "contacts/edit_album.html", {
        "form": form,
        "albums": albums
    })

def delete_album(request, pk):
    album = get_object_or_404(Album, pk=pk)
    if request.method == 'POST':
        album.delete()
        return redirect(to='list_album')
    return render(request, "albums/delete_album.html", {"albums": album})