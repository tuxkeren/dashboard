from django.shortcuts import render

from .models import *

def index(request):
    return render(request, 'dashboard.html')


def entry_data(request):
    return render(request, 'entry_data.html')


def list_machine(request):
    machines = Machine.objects.all()
    return render(request, 'machine_list.html', {'machines': machines})

