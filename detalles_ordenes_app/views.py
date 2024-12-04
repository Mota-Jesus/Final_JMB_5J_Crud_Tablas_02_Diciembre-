from django.shortcuts import render, redirect
from .models import Detalles

# Vista principal: mostrar lista de detalles de las órdenes
def inicio_vistaDetalles(request):
    losdetalles = Detalles.objects.all()
    return render(request, "gestionarDetalles.html", {"misdetalles": losdetalles})

# Registrar un nuevo detalle de orden
def registrarDetalles(request):
    id_detalles = request.POST["txtcodigo"]
    id_orden = request.POST["numorden"]
    id_producto = request.POST["numproducto"]
    cantidad = request.POST["numcantidad"]
    precio_unitario = request.POST["numprecio_unitario"]
    subtotal = request.POST["numsubtotal"]
    descuento = request.POST["numdescuento"]

    guardar_detalles = Detalles.objects.create(
        id_detalles=id_detalles,
        id_orden=id_orden,
        id_producto=id_producto,
        cantidad=cantidad,
        precio_unitario=precio_unitario,
        subtotal=subtotal,
        descuento=descuento
    )

    return redirect("detalles_ordenes")

# Seleccionar un detalle de orden para editarlo
def seleccionarDetalles(request, id_detalles):
    detalle = Detalles.objects.get(id_detalles=id_detalles)
    return render(request, "editardetalles.html", {"misdetalles": detalle})

# Editar un detalle de orden
def editarDetalles(request):
    id_detalles = request.POST["txtcodigo"]
    id_orden = request.POST["numorden"]
    id_producto = request.POST["numproducto"]
    cantidad = request.POST["numcantidad"]
    precio_unitario = request.POST["numprecio_unitario"]
    subtotal = request.POST["numsubtotal"]
    descuento = request.POST["numdescuento"]

    detalle = Detalles.objects.get(id_detalles=id_detalles)
    detalle.id_orden = id_orden
    detalle.id_producto = id_producto
    detalle.cantidad = cantidad
    detalle.precio_unitario = precio_unitario
    detalle.subtotal = subtotal
    detalle.descuento = descuento
    detalle.save()  # Guarda el registro actualizado

    return redirect("detalles_ordenes")

# Borrar un detalle de orden
def borrarDetalles(request, id_detalles):
    detalle = Detalles.objects.get(id_detalles=id_detalles)
    detalle.delete()  # Elimina el registro
    return redirect("detalles_ordenes")
