from django.urls import path, include

from accounts.views import UserRegisterView


urlpatterns = [
    path("register/", UserRegisterView.as_view(), name="register")
]

app_name = "accounts"
