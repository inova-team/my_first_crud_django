# from django.contrib import admin
from django.urls import path, include

from crud import views

#
# from clientes import views, views_actores, institution_views

urlpatterns = [
    # path('ruta/', backend, identificador)
    path('home/', views.home, name='home'),
    path('contacto/', views.contacto, name='contacto')
]

# actorespatterns = [
#     path('register', views_actores.RegisterActorView.as_view(), name="register_actor"),
#     path('edit/<pk>', views_actores.EditActor.as_view(), name="edit_actor"),
#     path('list', views_actores.actores_list, name="list_actor"),
#     path('delete/<pk>', views_actores.delete_actor, name="delete_actor"),
#     path('detail/<pk>', views_actores.actors_detail, name="actor_detail"),
# ]
# institucionespatterns = [
#     path('list', institution_views.instituttion_list, name="instituttion_list"),
#     path('subdivision_list/<pk>', institution_views.instituttion_son_list, name="instituttion_son_list"),
#     path('register', institution_views.CreateInstitution.as_view(), name="institution_register"),
#     path('edit/<pk>', institution_views.EditInstitution.as_view(), name="institution_edit"),
#     path('detail/<pk>', institution_views.institution_detail, name="institution_detail"),
#     path('nuevo_cargo/<pk>', institution_views.AddCargo.as_view(), name="cargo_register"),
# ]
#
# clientspatterns = [
#     path('register', views.RegisterClientView.as_view(), name="register_client"),
#     path('edit/<pk>', views.EditClient.as_view(), name="edit_client"),
#     path('list', views.cliente_list, name="list_client"),
#     path('delete/<pk>', views.delete_cliente, name="delete_client"),
#     path('detail/<pk>',views.client_detail, name="client_detail"),
# ]
#

# urlpatterns = [
#     path('actores/', include(actorespatterns)),
#     path('instituciones/', include(institucionespatterns)),
#     path('clients/', include(clientspatterns)),
# ]


