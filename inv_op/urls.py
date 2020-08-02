from django.urls import path
from django.contrib import admin
from .views import index
from rutaMasCorta.views import instanciarNodos
from expansionMinima.views import instanciarNodos


urlpatterns = [
    path('', index, name="index"),
    path('RMC/', instanciarNodos),
    path('EM/', instanciarNodos)
]