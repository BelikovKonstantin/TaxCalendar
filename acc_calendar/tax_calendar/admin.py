from django.contrib import admin

from .models import Event, Regulator

@admin.register(Event) 
class EventAdmin(admin.ModelAdmin): 
    list_display = ('name','regulator', 'type',)


@admin.register(Regulator) 
class RegulatorAdmin(admin.ModelAdmin): 
    list_display = ('name',)