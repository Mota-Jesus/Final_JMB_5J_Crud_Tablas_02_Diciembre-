from django.urls import path
from clientes_app import views

urlpatterns = [
    path("clientes", views.inicio_vistaClientes, name="clientes"),
    path("registrarClientes/", views.registrarClientes, name="registrarClientes"),
    path("seleccionarClientes/<id_clientes>", views.seleccionarClientes, name="seleccionarClientes"),
    path("editarClientes/", views.editarClientes, name="editarClientes"),
    path("borrarClientes/<id_clientes>", views.borrarClientes, name="borrarClientes"),
]
