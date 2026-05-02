#from django.shortcuts import render
# Create your views here.

from django.shortcuts import render, redirect
from .models import Photo

def gallery_view(request):
    if request.method == 'POST' and request.FILES.get('image_file'):
        img = request.FILES.get('image_file')
        title = request.POST.get('title')
        Photo.objects.create(title=title, image=img)
        return redirect('gallery')

    photos = Photo.objects.all().order_by('-uploaded_at')
    return render(request, 'gallery/gallery.html', {'photos': photos})
