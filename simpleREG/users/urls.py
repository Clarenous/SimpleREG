from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('register/', views.doNothing, name='register'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('check_login_time/', views.check_login_time, name='check_login_time'),
    path('password_change/', views.PasswordChangeView.as_view(), name='password_change'),
]