from django.urls import path
from .views import *

urlpatterns = [
    path('login',login_user),
    path("regester",regesete_user),
    path("log_out",user_log_out),
    path("user_panel",user_panel)
]
