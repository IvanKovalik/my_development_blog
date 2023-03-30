from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login-page'),
    path('register/', RegisterView.as_view(), name='register-page'),
]
