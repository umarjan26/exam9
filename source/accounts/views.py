

from django.contrib.auth import get_user_model, login, update_session_auth_hash
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import CreateView, DetailView, UpdateView

from accounts.forms import MyUserCreationForm, UserUpdateForm, PasswordChangeForm

User = get_user_model()


class RegisterView(CreateView):
    model = get_user_model()
    template_name = 'accounts/create.html'
    form_class = MyUserCreationForm

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect(self.get_success_url())

    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if not next_url:
            next_url = self.request.POST.get('next')
        if not next_url:
            next_url = reverse('webapp:index_view')
        return next_url


class UserDetailView(LoginRequiredMixin, DetailView):
    model = get_user_model()
    template_name = 'accounts/user_detail.html'
    context_object_name = 'user_obj'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(UserDetailView, self).get_context_data(object_list=object_list, **kwargs)
        pvivate_photos = self.object.photos.filter(isPrivate=True)
        private_albums = self.object.albums.filter(isPrivate=True)
        photos = self.object.photos.filter(isPrivate=False)
        albums = self.object.albums.filter(isPrivate=False)
        context['photos'] = photos
        context['albums'] = albums
        context['private_photos'] = pvivate_photos
        context['private_albums'] = private_albums
        return context


class UpdateUserView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserUpdateForm
    template_name = "accounts/update_profile.html"
    context_object_name = "user_object"

    def get_success_url(self):
        return reverse("accounts:detail", kwargs={"pk": self.request.user.pk})

    def get_object(self, queryset=None):
        return self.request.user


class UserPasswordChangeView(LoginRequiredMixin, UpdateView):
    model = get_user_model()
    template_name = 'accounts/user_password_change.html'
    form_class = PasswordChangeForm
    context_object_name = 'user_object'

    def form_valid(self, form):
        response = super().form_valid(form)
        update_session_auth_hash(self.request, self.object)
        return response

    def get_object(self, queryset=None):
        return self.request.user

    def get_success_url(self):
        return reverse("accounts:detail", kwargs={"pk": self.request.user.pk})
