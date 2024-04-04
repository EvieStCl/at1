from django.urls import path
from . import views

urlpatterns = [
    path('', views.splash_page, name='splash_page'),
]