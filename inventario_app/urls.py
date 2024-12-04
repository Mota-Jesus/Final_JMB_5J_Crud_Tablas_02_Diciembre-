from django.urls import path
from inventario_app import views

urlpatterns = [
    path("inventarios", views.inicio_vistaInventario, name="inventarios"),
    path("registrarInventario/", views.registrarInventario, name="registrarInventario"),
    path("seleccionarInventario/<id_inventario>", views.seleccionarInventario, name="seleccionarInventario"),
    path("editarInventario/", views.editarInventario, name="editarInventario"),
    path("borrarInventario/<id_inventario>", views.borrarInventario, name="borrarInventario")
]
