from django.urls import path

from .views import api_user_login, api_user_signup

urlpatterns = [
    path('users/signup/', api_user_signup),
    path('users/login/', api_user_login),

]
