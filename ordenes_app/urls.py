from django.urls import path
from ordenes_app import views

urlpatterns = [
    path("ordenes", views.inicio_vistaOrdenes, name="ordenes"),
    path("registrarOrdenes/", views.registrarOrdenes, name="registrarOrdenes"),
    path("seleccionarOrdenes/<id_orden>", views.seleccionarOrdenes, name="seleccionarOrdenes"),
    path("editarOrdenes/", views.editarOrdenes, name="editarOrdenes"),
    path("borrarOrdenes/<id_orden>", views.borrarOrdenes, name="borrarOrdenes"),
]
