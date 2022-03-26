from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('solicitud', views.enviar_solicitud, name='index'),
]
