from django.urls import path
from . import views

urlpatterns = [
    path('register', views.registration_view, name="registration"),
    path('login', views.login_view, name="login"),
    path('logout', views.logout_view, name="logout"),
    path('activate/<uidb64>/<token>', views.activate, name='activate'),
    path('reset_password', views.reset_password_view, name="reset_password"),

    path('reset/<uidb64>/<token>', views.reset_password_confirm, name="reset_password_confirm")
]