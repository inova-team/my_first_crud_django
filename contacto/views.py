from datetime import datetime
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from crud.models import InformacionPersonal
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login


@login_required
def contacto(request):
    user = request.user
    user_pi = InformacionPersonal.objects.get(usuario=user)
    edad = datetime.now().year - user_pi.fecha_nacimiento.year
    context = {
        "user": user,
        "user_pi": user_pi,
        "edad":edad
    }
    return render(request, 'contacto/contacto.html', context)


def iniciar_sesion(request):
    if request.method == 'POST':
        username = request.POST['input_username']
        password = request.POST['input_password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('contact')

    return render(request, 'contacto/iniciar_sesion.html')


def registrarse(request):
    if request.method == 'POST':
        email = request.POST['input_email']
        first_name = request.POST['input_first_name']
        last_name = request.POST['input_last_name']
        username = request.POST['input_username']
        password = request.POST['input_password']
        birthday = request.POST['input_birthday']
        profesion = request.POST['input_profesion']
        pais = request.POST['input_country']

        if User.objects.filter(username=username).exists():
            return redirect('signup')

        user_create = User(email=email, username=username, password=make_password(password), first_name=first_name,
                           last_name=last_name)
        user_create.save()
        user = User.objects.get(username=username)
        InformacionPersonal.objects.create(fecha_nacimiento=birthday, edad=None, profesion=profesion, pais=pais,
                                           usuario=user)
        return redirect('login')


    return render(request, 'contacto/registro.html')


@login_required
def editar_informacion_personal(request):
    user = request.user
    user_pi = InformacionPersonal.objects.get(usuario=user)
    if request.method == 'POST':
        first_name = request.POST['input_first_name']
        last_name = request.POST['input_last_name']
        birthday = request.POST['input_birthday']
        profesion = request.POST['input_profesion']
        pais = request.POST['input_country']

        user.first_name=first_name
        user.last_name=last_name
        user.save()


        user_pi.fecha_nacimiento = birthday
        user_pi.profesion=profesion
        user_pi.pais=pais
        user_pi.save()
        return redirect('contact')

    context ={
        "user":user,
        "user_pi":user_pi
    }
    return render(request, 'contacto/editar_informacion_personal.html', context)

