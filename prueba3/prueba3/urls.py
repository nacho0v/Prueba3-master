from django.contrib import admin
from django.urls import path
from app_gestion import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('index/', views.index),
    path('ingresar_persona/', views.ingresar_persona ),
    path('eliminar_persona/', views.eliminar_persona ),
    path('buscar_persona/', views.busqueda_persona ),
    path('buscar/',views.buscar),
    path('ingreso_persona/', views.ingresoPersona ),
    path('listar_todo_persona/', views.listar_todo_persona ),
    path('listar_todo/', views.listar_todo),
    path('eliminacion_persona/',views.eliminacion_persona),
    path('ingresar_medico/', views.ingresar_medico),
    path('ingresoMedico/', views.ingresoMedico),
    path('busqueda_medico/', views.busqueda_medico),
    path('eliminar_medico/', views.eliminar_medico),
    path('listar_medico/', views.listar_medico),
    path('listar_todo_medico/', views.listar_todo_medico),
    path('buscar_medico/', views.buscar_medico),
    path('eliminacion_medico/', views.eliminacion_medico),
    path('ingresoMedico/', views.ingresoMedico),
]
