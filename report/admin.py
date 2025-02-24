from django.contrib import admin
from .models  import *

class MachineAdmin(admin.ModelAdmin):
    list_display  = ('name', 'task')
    search_fields = ('name',)

admin.site.register(Machine, MachineAdmin)

