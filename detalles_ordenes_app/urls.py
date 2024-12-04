from django.urls import path
from detalles_ordenes_app import views

urlpatterns = [
    path("detalles_ordenes", views.inicio_vistaDetalles, name="detalles_ordenes"),
    path("registrarDetalles/", views.registrarDetalles, name="registrarDetalles"),
    path("seleccionarDetalles/<id_detalles>", views.seleccionarDetalles, name="seleccionarDetalles"),
    path("editarDetalles/", views.editarDetalles, name="editarDetalles"),
    path("borrarDetalles/<id_detalles>", views.borrarDetalles, name="borrarDetalles")
]
