from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView

from webapp.forms import AlbumForm
from webapp.models import Album


class AlbumView(DetailView):
    model = Album
    template_name = 'albums/view.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        photos = self.object.photos.filter(isPrivate=False)
        print(photos)
        context['photos'] = photos
        return context


class AlbumCreateView(CreateView):
    model = Album
    form_class = AlbumForm
    template_name = 'albums/create.html'

    def get_success_url(self):
        return reverse('webapp:album_view', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        album = form.save(commit=False)
        album.author = self.request.user
        album.save()
        return redirect('webapp:album_view', pk=album.pk)



class AlbumUpdateView(UpdateView):
    model = Album
    template_name = 'albums/update.html'
    form_class = AlbumForm

    def get_success_url(self):
        return reverse('webapp:album_view', kwargs={'pk': self.object.pk})

class AlbumDeleteView(DeleteView):
    model = Album
    template_name = "albums/delete.html"

    def get_success_url(self):
        return reverse('webapp:photo_index')
