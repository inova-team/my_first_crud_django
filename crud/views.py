from django.shortcuts import render, redirect

# Create your views here.
from crud.models import Videojuego, Tipo

def listar_videojuegos(request):

    videojuegos = Videojuego.objects.filter(estado=1)

    print(':::')
    for juego in videojuegos:
        print(juego.nombre)

    context = {
        'lista': videojuegos
    }
    return render(request, 'carlos/home.html', context)

def crear_videojuego(request):

    tipos = Tipo.objects.all()

    if request.POST:
        nombre = request.POST['nombre_name']
        fecha = request.POST['fecha_name']
        tipo = request.POST['tipo_name']


        Videojuego.objects.create(nombre=nombre, tipo_id=tipo, fecha_lanzamiento=fecha)
        return redirect('listar_vj')

    context = {
        'tipos' : tipos
    }
    return render(request, 'carlos/create.html', context)


def editar_videojuego(request,pk):

    videojuego_actual = Videojuego.objects.get(pk=pk)
    tipos = Tipo.objects.all()

    if request.POST:
        nombre = request.POST['nombre_name']
        fecha = request.POST['fecha_name']
        tipo = request.POST['tipo_name']

        videojuego_actual.nombre = nombre
        videojuego_actual.fecha_lanzamiento = fecha
        videojuego_actual.tipo = Tipo.objects.get(pk=tipo)
        videojuego_actual.save()
        return redirect('listar_vj')

    context = {
        'tipos' : tipos,
        'videojuego_actual' : videojuego_actual
    }
    return render(request, 'carlos/edit.html', context)


def eliminar_videojuego_logico(request,pk):

    videojuego_actual = Videojuego.objects.get(pk=pk)
    videojuego_actual.estado = 0
    videojuego_actual.save()

    return redirect('listar_vj')

def eliminar_videojuego_fisico(request,pk):

    videojuego_actual = Videojuego.objects.get(pk=pk)
    videojuego_actual.delete()

    return redirect('listar_vj')
