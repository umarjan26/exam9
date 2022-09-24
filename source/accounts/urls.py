from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from accounts.views import RegisterView, UserDetailView, UpdateUserView, UserPasswordChangeView

app_name = 'accounts'

urlpatterns = [
    path('login/', LoginView.as_view(template_name="accounts/login.html"), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('create/', RegisterView.as_view(), name='create'),
    path('<int:pk>/', UserDetailView.as_view(), name='detail'),
    path('update/', UpdateUserView.as_view(), name='update'),
    path("change_psw/", UserPasswordChangeView.as_view(), name="change_password")
]
