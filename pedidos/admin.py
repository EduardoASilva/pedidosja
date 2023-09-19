from django.contrib import admin
from pedidos.models import Esfirras


class AdminEsfirras(admin.ModelAdmin):
    list_display = ('nome',)
    list_per_page = 15


admin.site.register(Esfirras)
