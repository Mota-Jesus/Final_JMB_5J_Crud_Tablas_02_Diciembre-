from django.shortcuts import render, redirect
from .models import Ordenes

# Vista principal: mostrar lista de empleados
def inicio_vistaEmpleados(request):
    losempleados = Ordenes.objects.all()
    return render(request, "gestionarEmpleados.html", {"misempleados": losempleados})

# Registrar un nuevo empleado
def registrarEmpleados(request):
    id_empleado = request.POST["txtcodigo"]
    nombre = request.POST["txtnombre"]
    telefono = request.POST["txttelefono"]
    direccion = request.POST["txtdireccion"]
    puesto = request.POST["txtpuesto"]

    guardarEmpleados = Ordenes.objects.create(
        id_empleado=id_empleado, nombre=nombre, telefono=telefono, direccion=direccion, puesto=puesto
    )

    return redirect("empleados")

# Seleccionar un empleado para editarlo
def seleccionarEmpleados(request, id_empleado):
    empleado = Ordenes.objects.get(id_empleado=id_empleado)
    return render(request, "editarEmpleados.html", {"misempleados": empleado})

# Editar un empleado
def editarEmpleados(request):
    id_empleado = request.POST["txtcodigo"]
    nombre = request.POST["txtnombre"]
    telefono = request.POST["txttelefono"]
    direccion = request.POST["txtdireccion"]
    puesto = request.POST["txtpuesto"]

    empleado = Ordenes.objects.get(id_empleado=id_empleado)
    empleado.nombre = nombre
    empleado.telefono = telefono
    empleado.direccion = direccion
    empleado.puesto = puesto
    empleado.save()

    return redirect("empleados")

# Borrar un empleado
def borrarEmpleados(request, id_empleado):
    empleado = Ordenes.objects.get(id_empleado=id_empleado)
    empleado.delete()
    return redirect("empleados")
