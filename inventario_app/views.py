from django.shortcuts import render, redirect
from .models import Inventario

# Vista principal: mostrar lista de inventarios
def inicio_vistaInventario(request):
    losinventarios = Inventario.objects.all()
    return render(request, "gestionarInventarios.html", {"misinventarios": losinventarios})

# Registrar un nuevo inventario
def registrarInventario(request):
    id_inventario = request.POST["txtcodigo"]
    id_producto = request.POST["numproducto"]
    cantidad = request.POST["numcantidad"]
    fecha_ingreso = request.POST["datefecha_ingreso"]
    fecha_vencimiento = request.POST["datefecha_vencimiento"]
    proveedor = request.POST["txtproveedor"]
    notas = request.POST["txtnotas"]

    guardarinventario = Inventario.objects.create(
        id_inventario=id_inventario,
        id_producto=id_producto,
        cantidad=cantidad,
        fecha_ingreso=fecha_ingreso,
        fecha_vencimiento=fecha_vencimiento,
        proveedor=proveedor,
        Notas=notas
    )

    return redirect("inventarios")

# Seleccionar un inventario para editarlo
def seleccionarInventario(request, id_inventario):
    inventario = Inventario.objects.get(id_inventario=id_inventario)
    return render(request, "editarinventarios.html", {"misinventarios": inventario})

# Editar un inventario
def editarInventario(request):
    id_inventario = request.POST["txtcodigo"]
    id_producto = request.POST["numproducto"]
    cantidad = request.POST["numcantidad"]
    fecha_ingreso = request.POST["datefecha_ingreso"]
    fecha_vencimiento = request.POST["datefecha_vencimiento"]
    proveedor = request.POST["txtproveedor"]
    notas = request.POST["txtnotas"]

    inventario = Inventario.objects.get(id_inventario=id_inventario)
    inventario.id_producto = id_producto
    inventario.cantidad = cantidad
    inventario.fecha_ingreso = fecha_ingreso
    inventario.fecha_vencimiento = fecha_vencimiento
    inventario.proveedor = proveedor
    inventario.Notas = notas
    inventario.save()  # Guarda el registro actualizado

    return redirect("inventarios")

# Borrar un inventario
def borrarInventario(request, id_inventario):
    inventario = Inventario.objects.get(id_inventario=id_inventario)
    inventario.delete()  # Elimina el registro
    return redirect("inventarios")
