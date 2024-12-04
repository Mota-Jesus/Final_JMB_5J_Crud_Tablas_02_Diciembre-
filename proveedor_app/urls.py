from django.urls import path
from proveedor_app import views

urlpatterns = [
    path("proveedores", views.inicio_vistaProveedores, name="proveedores"),
    path("registrarProveedores/", views.registrarProveedores, name="registrarProveedores"),
    path("seleccionarProveedores/<id_proveedor>", views.seleccionarProveedores, name="seleccionarProveedores"),
    path("editarProveedores/", views.editarProveedores, name="editarProveedores"),
    path("borrarProveedores/<id_proveedor>", views.borrarProveedores, name="borrarProveedores")
]
