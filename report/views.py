from django.shortcuts import render

from .models import *

def index(request):
    context = {
        'title':'Dashboard'
    }
    return render(request, 'dashboard.html', context)


def entry_data(request):
    context = {
        'title':'Entry Data'
    }
    return render(request, 'entry_data.html', context)


def list_machine(request):
    machine = Machine.objects.all()

    context = {
        'title':'Daftar Mesin',
        'machines': machine
    }
   
    return render(request, 'machine_list.html', context)

def paramater(request):
    context = {
        'title':'Parameter'
    }
    return render(request, 'parameter.html', context)