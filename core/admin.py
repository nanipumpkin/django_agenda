from django.contrib import admin

from core.models import Evento

class EventoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'data', 'criacao')
    list_filter = ('usuario', 'data')

# Register your models here.
admin.site.register(Evento, EventoAdmin)