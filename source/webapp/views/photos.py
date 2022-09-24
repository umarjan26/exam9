from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from webapp.forms import PhotoForm
from webapp.models import Photo


class PhotoIndex(LoginRequiredMixin, ListView):
    model = Photo
    template_name = 'photos/index.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        photos = Photo.objects.filter(isPrivate=False).filter(album__isPrivate=False).order_by('-created_at')
        context['photos'] = photos
        return context


class PhotoView(LoginRequiredMixin, DetailView):
    model = Photo
    template_name = 'photos/view.html'


class PhotoCreateView(LoginRequiredMixin, CreateView):
    model = Photo
    form_class = PhotoForm
    template_name = 'photos/create.html'

    def get_success_url(self):
        return reverse('webapp:photo_view', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        photo = form.save(commit=False)
        photo.author = self.request.user
        photo.save()
        return redirect('webapp:photo_view', pk=photo.pk)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class PhotoUpdateView(PermissionRequiredMixin, UpdateView):
    model = Photo
    template_name = 'photos/update.html'
    form_class = PhotoForm
    permission_required = 'webapp.change_photo'


    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def get_success_url(self):
        return reverse('webapp:photo_view', kwargs={'pk': self.object.pk})

    def has_permission(self):
        photo = get_object_or_404(Photo, pk=self.kwargs.get('pk'))
        return super().has_permission() or self.request.user == photo.author



class PhotoDeleteView(PermissionRequiredMixin, DeleteView):
    model = Photo
    template_name = "photos/delete.html"
    permission_required = 'webapp.delete_photo'


    def get_success_url(self):
        return reverse('webapp:photo_index')



    def has_permission(self):
        photo = get_object_or_404(Photo, pk=self.kwargs.get('pk'))
        return super().has_permission() or self.request.user == photo.author
