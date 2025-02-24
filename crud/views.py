from django.shortcuts import render, redirect

# Create your views here.
from crud.models import Videojuego, Tipo

def signin(request):

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username == "admin" and password == "puerta123":
            return redirect('posview')
    
    context = {
        'lista': "texto"
    }
    return render(request, 'authentication/signin.html', context)

def posview(request):
    print("POSSSSSSS")
    context = {
        'tipos' : "AAAAAA"
    }
    return render(request, 'pos/home.html', context)
