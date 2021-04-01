from django.urls import path

from rest_framework.authtoken.views import obtain_auth_token

from account.views import registeration_view

app_name = 'account'

urlpatterns = [
    path('register', registeration_view, name="register"),
    path('login', obtain_auth_token, name="login")
]
