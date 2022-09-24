from http import HTTPStatus

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import JsonResponse
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse
from django.views import View
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView

from webapp.forms import AlbumForm
from webapp.models import Album


class AlbumView(LoginRequiredMixin, DetailView):
    model = Album
    template_name = 'albums/view.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        photos = self.object.photos.filter(isPrivate=False)
        context['photos'] = photos
        return context


class AlbumCreateView(LoginRequiredMixin, CreateView):
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



class AlbumUpdateView(PermissionRequiredMixin, UpdateView):
    model = Album
    template_name = 'albums/update.html'
    form_class = AlbumForm
    permission_required = 'webapp.change_album'



    def get_success_url(self):
        return reverse('webapp:album_view', kwargs={'pk': self.object.pk})

    def has_permission(self):
        album = get_object_or_404(Album, pk=self.kwargs.get('pk'))
        return super().has_permission() or self.request.user == album.author



class AlbumDeleteView(PermissionRequiredMixin, DeleteView):
    model = Album
    template_name = "albums/delete.html"
    permission_required = 'webapp.delete_album'


    def get_success_url(self):
        return reverse('webapp:photo_index')


    def has_permission(self):
        album = get_object_or_404(Album, pk=self.kwargs.get('pk'))
        return super().has_permission() or self.request.user == album.author




class AlbumSelectedView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        album = get_object_or_404(Album, pk=kwargs.get('pk'))

        if request.user in album.selected.all():
            return JsonResponse(
                {"error": 'Уже в избранных'},
                status=HTTPStatus.FORBIDDEN,
            )

        album.selected.add(request.user)
        return JsonResponse(
            {"Status": 'Selected'}
        )


class AlbumUnSelectedView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        album = get_object_or_404(Album, pk=kwargs.get('pk'))

        if not request.user in album.selected.all():
            return JsonResponse(
                {"error": 'Надо сначало добавить'},
                status=HTTPStatus.FORBIDDEN,
            )

        album.selected.remove(request.user)
        return JsonResponse(
            {"Status": 'UnSelected'}
        )