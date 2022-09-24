from django import forms

from webapp.models import Photo, Album


class PhotoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        print(user)
        super(PhotoForm, self).__init__(*args, **kwargs)
        self.fields['album'].queryset = Album.objects.filter(author=user)

    class Meta:
        model = Photo
        fields = ('photo', 'description', 'isPrivate', 'album')
