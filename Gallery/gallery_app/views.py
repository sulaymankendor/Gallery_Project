from django.shortcuts import render, redirect
from .models import Gallery
from .form import GalleryForm
from .file import FileForm
from pathlib import Path
import os

# BASE_DIR = Path(__file__).resolve().parent.parent

def home(request):
    galleries = Gallery.objects.all()
    count_posts = galleries.count()
    if request.method == 'POST':
        if request.POST.get('delete_all') == '':
            Gallery.objects.all().delete()
            return redirect('home')
    context = {'galleries': galleries, 'count_posts': count_posts}
    return render(request, 'gallery_app/home.html', context)

def post(request):
    if request.method == 'POST':
        description = request.POST.get('description')
        uploaded_image = request.FILES.get('image')
        Gallery.objects.create(description=description, image=uploaded_image)
        return redirect('home')
    context = {'form': GalleryForm, 'fileform': FileForm}
    return render(request, 'gallery_app/post.html', context)


def update_post(request, id):
    post_to_update = Gallery.objects.get(id=id)
    if request.method == 'POST':
        updated_description = request.POST.get('description')
        updated_image = request.FILES.get('image')
        gallery = Gallery.objects.get(id=id)
        gallery.description = updated_description
        gallery.image = updated_image
        gallery.save()
        return redirect('home')

    context = {'form': GalleryForm, 'fileform': FileForm, 'post_to_update': post_to_update}
    return render(request, 'gallery_app/update-post.html', context)


def delete_post(request, id):
    post_to_delete = Gallery.objects.get(id=id)
    no = request.POST.get('no')
    yes = request.POST.get('yes')
    if request.method == 'POST':
        if no == '':
            return redirect('home')
        elif yes == '':
            Gallery.objects.get(id=id).delete()
            return redirect('home')

    context = {'post_to_delete': post_to_delete}
    return render(request, 'gallery_app/delete-post.html', context)
