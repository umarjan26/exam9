from django.urls import path

from webapp.views.photos import (PhotoIndex,
                                 PhotoView,
                                 PhotoCreateView,
                                 PhotoUpdateView,
                                 PhotoDeleteView,)
from webapp.views.albums import (AlbumView,
                                 AlbumCreateView,
                                 AlbumUpdateView,
                                 AlbumDeleteView)

app_name = "webapp"

urlpatterns = [
    path('', PhotoIndex.as_view(), name="photo_index"),
    path('photo/<int:pk>/', PhotoView.as_view(), name='photo_view'),
    path('photo/add/', PhotoCreateView.as_view(), name='photo_create'),
    path('photo/<int:pk>/update', PhotoUpdateView.as_view(), name='photo_update'),
    path('photo/<int:pk>/delete', PhotoDeleteView.as_view(), name='photo_delete'),
    path('album/<int:pk>/', AlbumView.as_view(), name='album_view'),
    path('album/add/', AlbumCreateView.as_view(), name='album_create'),
    path('album/<int:pk>/update', AlbumUpdateView.as_view(), name='album_update'),
    path('album/<int:pk>/delete', AlbumDeleteView.as_view(), name='album_delete')
]