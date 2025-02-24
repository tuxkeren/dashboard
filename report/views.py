from django.shortcuts import render

from .models import *

def index(request):
    return render(request, 'dashboard.html')


def list_machine(request):
    machines = Machine.objects.all()
    return render(request, 'machine_list.html', {'machines': machines})

