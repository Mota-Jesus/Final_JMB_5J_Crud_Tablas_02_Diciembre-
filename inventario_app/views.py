# inventario_app/views.py
from django.shortcuts import render, redirect
from .models import Inventario

# Vista principal: listar registros del inventario
def inicio_vistaInventario(request):
    losinventarios = Inventario.objects.all()
    return render(request, "gestionarInventario.html", {"misinventarios": losinventarios})

# Registrar un nuevo inventario
def registrarInventario(request):
    id_inventario = request.POST["txtcodigo"]
    id_producto = request.POST["numproducto"]
    cantidad = request.POST["numcantidad"]
    fecha_ingreso = request.POST["dateingreso"]
    fecha_vencimiento = request.POST["datevencimiento"]
    id_proveedor = request.POST["numproveedor"]
    notas = request.POST["txtnotas"]

    guardarinventario = Inventario.objects.create(
        id_inventario=id_inventario,
        id_producto=id_producto,
        cantidad=cantidad,
        fecha_ingreso=fecha_ingreso,
        fecha_vencimiento=fecha_vencimiento,
        id_proveedor=id_proveedor,
        Notas=notas,
    )

    return redirect("inventario")

# Seleccionar un registro de inventario para editarlo
def seleccionarInventario(request, id_inventario):
    inventario = Inventario.objects.get(id_inventario=id_inventario)
    return render(request, "editarInventario.html", {"misinventarios": inventario})

# Editar un registro del inventario
def editarInventario(request):
    id_inventario = request.POST["txtcodigo"]
    id_producto = request.POST["numproducto"]
    cantidad = request.POST["numcantidad"]
    fecha_ingreso = request.POST["dateingreso"]
    fecha_vencimiento = request.POST["datevencimiento"]
    id_proveedor = request.POST["numproveedor"]
    notas = request.POST["txtnotas"]

    inventario = Inventario.objects.get(id_inventario=id_inventario)
    inventario.id_producto = id_producto
    inventario.cantidad = cantidad
    inventario.fecha_ingreso = fecha_ingreso
    inventario.fecha_vencimiento = fecha_vencimiento
    inventario.id_proveedor = id_proveedor
    inventario.Notas = notas
    inventario.save()  # Guarda los cambios

    return redirect("inventario")

# Borrar un registro del inventario
def borrarInventario(request, id_inventario):
    inventario = Inventario.objects.get(id_inventario=id_inventario)
    inventario.delete()  # Elimina el registro
    return redirect("inventario")
