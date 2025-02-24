from django.urls import path
from .views import list_machine

urlpatterns = [
    path('machines/', list_machine, name='daftar_mesin')
    
]
