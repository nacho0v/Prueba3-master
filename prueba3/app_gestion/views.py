from django.shortcuts import redirect, render
from app_gestion.models import Persona
from app_gestion.models import Medico
from django.http import HttpResponse


def ingresar_persona(request):
    return render(request, "ingresar_persona.html")

def ingresar_medico(request):
    return render(request, "ingreso_medico.html")

def index(request):
    return render(request, "index.html")

def busqueda_persona(request):
    return render(request, "buscar_persona.html")

def busqueda_medico(request):
    return render(request, "busqueda_medico.html")

def eliminar_persona(request):
    return render(request, "eliminar_persona.html")

def eliminar_medico(request):
    return render(request, "eliminar_medico.html")

def listar_todo(request):
    return render(request,"listar_todo.html")

def listar_medico(request):
    return render(request,"listar_medico.html")


# Create your views here.
def listar_todo_persona(request):
    datos = Persona.objects.all()  
    return render(request,"listar_todo.html",{'personas':datos})

def listar_todo_medico(request):
    datos = Medico.objects.all()  
    return render(request,"listar_todo_medico.html",{'medicos':datos})
    
def ingresoPersona(request):
    rut=request.GET["txt_rut"]
    nombre=request.GET["txt_nombre"]
    appaterno=request.GET["txt_appaterno"]
    apmaterno=request.GET["txt_apmaterno"]
    edad=request.GET["num_edad"]
    vacuna=request.GET["txt_vacuna"]
    fecha=request.GET["txt_fecha"]
    if len(rut)>0 and len(nombre)>0 and len(appaterno)>0 and len(apmaterno)>0 and len(edad)>0 and len(vacuna)>0 and len(fecha)>0:
        per=Persona(rut=rut,nombre=nombre,appaterno=appaterno,apmaterno=apmaterno,edad=edad,vacuna=vacuna,fecha=fecha)  
        per.save()
        mensaje="<h1>Persona ingresada...</h1> <a href='/index/' >Volver al inicio</a>"
    else:
        mensaje="<h1>Persona no ingresada o datos faltantes...</h1>"
    return HttpResponse(mensaje)


def ingreso_medico(request):
    med_rut=request.GET["txt_med_rut"]
    med_nombre=request.GET["txt_med_nombre"]
    med_appaterno=request.GET["txt_med_appaterno"]
    med_apmaterno=request.GET["txt_med_apmaterno"]
    med_fecha=request.GET["txt_med_fecha"]
    if len(med_rut)>0 and len(med_nombre)>0 and len(med_appaterno)>0 and len(med_apmaterno)>0 and len(med_fecha)>0:
        med=Medico(med_rut=med_rut,med_nombre=med_nombre,med_appaterno=med_appaterno,med_apmaterno=med_apmaterno,med_fecha=med_fecha)  
        med.save()
        mensaje="<h1>Médico ingresado...</h1> <a href='/index/' >Volver al inicio</a>"
    else:
        mensaje="<h1>Médico no ingresado o datos faltantes...</h1>"
    return HttpResponse(mensaje)

def buscar(request):
    if request.GET["txt_rut"]:
        rut = request.GET["txt_rut"]
        personas = Persona.objects.filter(rut__icontains=rut)
        return render(request,"listar.html",{"personas":personas,"query":rut})
    else:
        mensaje = "Debe ingresar el RUT de la persona a buscar"
        return HttpResponse(mensaje)


def buscar_medico(request):
    if request.GET["txt_med_rut"]:
        med_rut = request.GET["txt_med_rut"]
        medicos = Medico.objects.filter(med_rut__icontains=med_rut)
        return render(request,"listar_medico.html",{"medicos":medicos,"query":med_rut})
    else:
        mensaje = "Debe ingresar el RUT del medico a buscar"
        return HttpResponse(mensaje)


def eliminacion_persona(request):
    if request.GET["txt_rut"]:
        rut_recibido = request.GET["txt_rut"]
        persona = Persona.objects.filter(rut=rut_recibido)
        if persona:
            per=Persona.objects.get(rut=rut_recibido)
            per.delete()
            mensaje = "Persona Eliminada...  <a href='/index/' >Volver al inicio</a>"
        else:
            mensaje = "<h1>Persona NO eliminada...  <a href='/index/' >Volver al inicio</a></h1>"
    else:
        mensaje = "<h1>Debe ingresar un RUT para eliminar...  <a href='/index/' >Volver al inicio</a>"
    return HttpResponse(mensaje)


def eliminacion_medico(request):
    if request.GET["txt_med_rut"]:
        rut_recibido = request.GET["txt_med_rut"]
        medico = Medico.objects.filter(med_rut=rut_recibido)
        if medico:
            med=Medico.objects.get(med_rut=rut_recibido)
            med.delete()
            mensaje = "Médico Eliminado...  <a href='/index/' >Volver al inicio</a>"
        else:
            mensaje = "<h1>Médico NO eliminado...</h1>  <a href='/index/' >Volver al inicio</a>"
    else:
        mensaje = "<h1>Debe ingresar un RUT para eliminar..."
    return HttpResponse(mensaje)


