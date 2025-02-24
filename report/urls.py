from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='dashbord'),
    path('machines/', list_machine, name='daftar_mesin')
    
]
