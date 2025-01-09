from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('BLD3', views.BLD3home),
    path('BLD4', views.BLD4home),
    path('BLD5', views.BLD5home)
]