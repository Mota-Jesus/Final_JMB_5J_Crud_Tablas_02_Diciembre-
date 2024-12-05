from django.shortcuts import render, redirect
from .models import Ordenes

# Vista principal: mostrar lista de órdenes
def inicio_vistaOrdenes(request):
    lasordenes = Ordenes.objects.all()
    return render(request, "gestionarOrdenes.html", {"misordenes": lasordenes})

# Registrar una nueva orden
def registrarOrdenes(request):
    id_orden = request.POST["txtidorden"]
    id_cliente = request.POST["txtidcliente"]
    id_empleado = request.POST["txtidempleado"]
    id_producto = request.POST["txtidproducto"]
    cantidad = request.POST["numcantidad"]
    fecha_orden = request.POST["datefechaorden"]
    total = request.POST["numtotal"]

    guardarordenes = Ordenes.objects.create(
        id_orden=id_orden,
        id_cliente=id_cliente,
        id_empleado=id_empleado,
        id_producto=id_producto,
        cantidad=cantidad,
        fecha_orden=fecha_orden,
        total=total,
    )

    return redirect("ordenes")

# Seleccionar una orden para editarla
def seleccionarOrdenes(request, id_orden):
    orden = Ordenes.objects.get(id_orden=id_orden)
    return render(request, "editarOrdenes.html", {"misordenes": orden})

# Editar una orden
def editarOrdenes(request):
    id_orden = request.POST["txtidorden"]
    id_cliente = request.POST["txtidcliente"]
    id_empleado = request.POST["txtidempleado"]
    id_producto = request.POST["txtidproducto"]
    cantidad = request.POST["numcantidad"]
    fecha_orden = request.POST["datefechaorden"]
    total = request.POST["numtotal"]

    orden = Ordenes.objects.get(id_orden=id_orden)
    orden.id_cliente = id_cliente
    orden.id_empleado = id_empleado
    orden.id_producto = id_producto
    orden.cantidad = cantidad
    orden.fecha_orden = fecha_orden
    orden.total = total
    orden.save()

    return redirect("ordenes")

# Borrar una orden
def borrarOrdenes(request, id_orden):
    orden = Ordenes.objects.get(id_orden=id_orden)
    orden.delete()
    return redirect("ordenes")
