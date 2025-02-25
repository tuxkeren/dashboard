from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='dashbord'),
    path('machines/', list_machine, name='daftar-mesin'),
    path('entry_data/', entry_data, name='entri-data')
    
]
