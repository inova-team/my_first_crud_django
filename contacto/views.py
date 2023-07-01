from datetime import datetime

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from crud.models import InformacionPersonal

@login_required
def contacto(request):
    user = request.user
    context = {
    "user": user
    }
    return render(request, 'contacto/contacto.html', context)

@login_required
def editar_informacion_personal(request):
    usuario = request.user
    print(":::")
    print(usuario)
    informacion_personal, creado = InformacionPersonal.objects.get_or_create(usuario=usuario)
    #TODO:: Debo implementar las vistas de Signup
    #Alex Juep

    #devuelve false si hay informacion personal de ese usuario
    #creado es true cuando no hay informacion personal para ese usuario
    # Verificar si se ha creado una nueva instancia de InformacionPersonal
    if creado:
        request.method = 'POST'
        request.POST = {
            'fecha_nacimiento': None,
            'edad': None,
            'profesion': None,
            'pais': None
        }
        return crear_informacion_personal(request)
    else:
        fecha_nacimiento = informacion_personal.fecha_nacimiento
        edad = informacion_personal.edad
        profesion = informacion_personal.profesion
        pais = informacion_personal.pais
        context={
            'fecha_nacimiento': fecha_nacimiento,
            'edad': edad,
            'profesion': profesion,
            'pais': pais
        }
    return render(request,'contacto/editar_informacion_personal.html',context)

@login_required
def crear_informacion_personal(request):
    if request.method == 'POST':
        fecha_nacimiento = request.POST['fecha_nacimiento']
        edad = request.POST['edad']
        profesion = request.POST['profesion']
        pais = request.POST['pais']

        # Crear nueva instancia de InformacionPersonal
        informacion_personal = InformacionPersonal.objects.create(
            usuario=request.user,
            fecha_nacimiento=fecha_nacimiento,
            edad=edad,
            profesion=profesion,
            pais=pais
        )
        informacion_personal.save()

    return redirect('edit_pi')

    #return render(request, 'contacto/contacto.html')