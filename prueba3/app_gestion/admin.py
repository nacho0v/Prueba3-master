from django.contrib import admin

# Register your models here.
from app_gestion.models import Persona
admin.site.register(Persona)

from app_gestion.models import Medico
admin.site.register(Medico)