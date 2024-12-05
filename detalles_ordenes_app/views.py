from django.shortcuts import render, redirect
from .models import Detalles

# Vista principal: listar detalles de órdenes
def inicio_vistaDetalles(request):
    losdetalles = Detalles.objects.all()
    return render(request, "gestionarDetalles.html", {"misdetalles": losdetalles})

# Registrar un nuevo detalle de orden
def registrarDetalles(request):
    id_detalles = request.POST["txtcodigo"]
    id_orden = request.POST["numid_orden"]
    id_empleado = request.POST["numid_empleado"]
    direccion_envio = request.POST["txtdireccion"]
    entregado = request.POST.get("chkentregado", False)

    # Convertir el valor del checkbox a Booleano
    entregado = True if entregado == "on" else False

    Detalles.objects.create(
        id_detalles=id_detalles,
        id_orden=id_orden,
        id_empleado=id_empleado,
        direccion_envio=direccion_envio,
        entregado=entregado,
    )

    return redirect("detalles")

# Seleccionar un detalle para editarlo
def seleccionarDetalles(request, id_detalles):
    detalle = Detalles.objects.get(id_detalles=id_detalles)
    return render(request, "editarDetalles.html", {"misdetalles": detalle})

# Editar un detalle
def editarDetalles(request):
    id_detalles = request.POST["txtcodigo"]
    id_orden = request.POST["numid_orden"]
    id_empleado = request.POST["numid_empleado"]
    direccion_envio = request.POST["txtdireccion"]
    entregado = request.POST.get("chkentregado", False)

    # Convertir el valor del checkbox a Booleano
    entregado = True if entregado == "on" else False

    detalle = Detalles.objects.get(id_detalles=id_detalles)
    detalle.id_orden = id_orden
    detalle.id_empleado = id_empleado
    detalle.direccion_envio = direccion_envio
    detalle.entregado = entregado
    detalle.save()

    return redirect("detalles")

# Borrar un detalle
def borrarDetalles(request, id_detalles):
    detalle = Detalles.objects.get(id_detalles=id_detalles)
    detalle.delete()
    return redirect("detalles")
