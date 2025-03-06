from django.contrib import admin
from .models  import *

class MachineAdmin(admin.ModelAdmin):
    list_display  = ('name', 'task')
    search_fields = ('name',)

admin.site.register(Machine, MachineAdmin)

class ReportAdmin(admin.ModelAdmin):
    list_display  = ('date', 
                     'param_1', 
                     'param_2', 
                     'param_3', 
                     'param_4', 
                     'param_5', 
                     'param_6', 
                     'param_7', 
                     'param_8', 
                     'param_9', 
                     'param_0', 
                     'note', 
                     'machine'
    )
    search_fields = ('date',)

admin.site.register(Report, ReportAdmin)


class FixvarAdmin(admin.ModelAdmin):
    list_display  = ('rate_threading', 
                     'rate_welding', 
                     'param_3', 
                     'param_4', 
                     'param_5', 
    )

admin.site.register(Fixvar, FixvarAdmin)
