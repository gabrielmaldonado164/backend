from django.contrib import admin

from schemas.models.nodos import Nodos

class NodosAdmin(admin.ModelAdmin):
    list_display = ['domain', 'username', 'nodo']

admin.site.register(Nodos, NodosAdmin)
