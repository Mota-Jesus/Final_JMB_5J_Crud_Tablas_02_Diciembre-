from django.shortcuts import render, redirect
from .models import Proveedor

# Vista principal: mostrar lista de proveedores
def inicio_vistaProveedores(request):
    losproveedores = Proveedor.objects.all()
    return render(request, "gestionarProveedores.html", {"misproveedores": losproveedores})

# Registrar un nuevo proveedor
def registrarProveedores(request):
    id_proveedor = request.POST["txtcodigo"]
    nombre = request.POST["txtnombre"]
    contacto = request.POST["txtcontacto"]
    telefono = request.POST["txttelefono"]
    email = request.POST["txtemail"]
    direccion = request.POST["txtdireccion"]
    fecha_registro = request.POST["datefecha_reg"]

    guardarproveedor = Proveedor.objects.create(
        id_proveedor=id_proveedor, nombre=nombre, contacto=contacto, telefono=telefono, email=email, direccion=direccion, fecha_registro=fecha_registro
    )

    return redirect("proveedores")

# Seleccionar un proveedor para editarlo
def seleccionarProveedores(request, id_proveedor):
    proveedor = Proveedor.objects.get(id_proveedor=id_proveedor)
    return render(request, "editarproveedores.html", {"misproveedores": proveedor})

# Editar un proveedor
def editarProveedores(request):
    id_proveedor = request.POST["txtcodigo"]
    nombre = request.POST["txtnombre"]
    contacto = request.POST["txtcontacto"]
    telefono = request.POST["txttelefono"]
    email = request.POST["txtemail"]
    direccion = request.POST["txtdireccion"]
    fecha_registro = request.POST["datefecha_reg"]

    proveedor = Proveedor.objects.get(id_proveedor=id_proveedor)
    proveedor.nombre = nombre
    proveedor.contacto = contacto
    proveedor.telefono = telefono
    proveedor.email = email
    proveedor.direccion = direccion
    proveedor.fecha_registro = fecha_registro
    proveedor.save()  # Guarda el registro actualizado

    return redirect("proveedores")

# Borrar un proveedor
def borrarProveedores(request, id_proveedor):
    proveedor = Proveedor.objects.get(id_proveedor=id_proveedor)
    proveedor.delete()  # Elimina el registro
    return redirect("proveedores")
