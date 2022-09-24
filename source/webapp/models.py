from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Album(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    description = models.CharField(max_length=500, verbose_name='Описание', null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор', related_name='albums')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    isPrivate = models.BooleanField(default=False, verbose_name='Приватность')
    selected = models.ManyToManyField(User, related_name='selected_albums')
    def __str__(self):
        return f'{self.pk}.{self.title}'

    class Meta:
        db_table = 'Albums'
        verbose_name = 'Альбом'
        verbose_name_plural = 'Альбомы'


class Photo(models.Model):
    photo = models.ImageField(upload_to='pictures', verbose_name='Фотография')
    description = models.CharField(max_length=500, verbose_name='Описание')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор', related_name='photos')
    album = models.ForeignKey('webapp.Album', on_delete=models.CASCADE, verbose_name='Альбом', related_name='photos', null=True, blank=True)
    isPrivate = models.BooleanField(default=False, verbose_name='Приватность')
    token = models.CharField(max_length=100, null=True, blank=True, unique=True)
    selected = models.ManyToManyField( User,related_name='selected_photos'
    )


    class Meta:
        db_table = 'Photos'
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'
