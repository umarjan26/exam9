from django.urls import path

from webapp.views.photos import PhotoIndex, PhotoView, PhotoCreateView, PhotoUpdateView, PhotoDeleteView

app_name = "webapp"

urlpatterns = [
    path('', PhotoIndex.as_view(), name="photo_index"),
    path('photo/<int:pk>/', PhotoView.as_view(), name='photo_view'),
    path('photo/add/', PhotoCreateView.as_view(), name='photo_create'),
    path('photo/<int:pk>/update', PhotoUpdateView.as_view(), name='photo_update'),
    path('photo/<int:pk>/delete', PhotoDeleteView.as_view(), name='photo_delete'),
]
