from django.urls import path

from contacto import views

urlpatterns = [
    path('contacto/', views.contacto, name='contact'),
    path('editar_informacion_personal/', views.editar_informacion_personal, name='edit_pi'),
    ]