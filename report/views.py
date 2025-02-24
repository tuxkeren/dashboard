from django.shortcuts import render

from .models import *

def index():
    pass


def list_machine(request):
    machines = Machine.objects.all()
    return render(request, 'machine_list.html', {'machines': machines})

