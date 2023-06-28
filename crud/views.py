from django.shortcuts import render

# Create your views here.

def contacto(request):
    user = request.user
    print(user)
    context = {
    "mensaje": 'Contacto',
    "user": user
    }
    return render(request, 'contacto.html', context)

def home(request):
    context = {
    "mensaje": 'Home'
    }
    return render(request, 'home.html', context)
