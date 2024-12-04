from django.shortcuts import render, redirect
from .models import Ordenes

# Vista principal: mostrar lista de órdenes
def inicio_vistaOrdenes(request):
    lasordenes = Ordenes.objects.all()
    return render(request, "gestionarOrdenes.html", {"misordenes": lasordenes})

# Registrar una nueva orden
def registrarOrdenes(request):
    id_orden = request.POST["txtcodigo"]
    id_cliente = request.POST["numcliente"]
    fecha_orden = request.POST["datefecha_orden"]
    total = request.POST["numtotal"]
    estado = request.POST["txtestado"]
    metodo_pago = request.POST["txtmetodo_pago"]
    comentarios = request.POST["txtcomentarios"]

    guardarorden = Ordenes.objects.create(
        id_orden=id_orden,
        id_cliente=id_cliente,
        fecha_orden=fecha_orden,
        total=total,
        estado=estado,
        metodo_pago=metodo_pago,
        comentarios=comentarios
    )

    return redirect("ordenes")

# Seleccionar una orden para editar
def seleccionarOrdenes(request, id_orden):
    orden = Ordenes.objects.get(id_orden=id_orden)
    return render(request, "editarordenes.html", {"misordenes": orden})

# Editar una orden
def editarOrdenes(request):
    id_orden = request.POST["txtcodigo"]
    id_cliente = request.POST["numcliente"]
    fecha_orden = request.POST["datefecha_orden"]
    total = request.POST["numtotal"]
    estado = request.POST["txtestado"]
    metodo_pago = request.POST["txtmetodo_pago"]
    comentarios = request.POST["txtcomentarios"]

    orden = Ordenes.objects.get(id_orden=id_orden)
    orden.id_cliente = id_cliente
    orden.fecha_orden = fecha_orden
    orden.total = total
    orden.estado = estado
    orden.metodo_pago = metodo_pago
    orden.comentarios = comentarios
    orden.save()  # Guarda el registro actualizado

    return redirect("ordenes")

# Borrar una orden
def borrarOrdenes(request, id_orden):
    orden = Ordenes.objects.get(id_orden=id_orden)
    orden.delete()  # Elimina el registro
    return redirect("ordenes")
