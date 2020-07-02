from django.urls import path, include

from . import views

urlpatterns = [
    # home
    path('', views.index, name='index'),
]
