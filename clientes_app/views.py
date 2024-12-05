from django.shortcuts import render, redirect
from .models import Clientes

# Vista principal: mostrar lista de clientes
def inicio_vistaClientes(request):
    losclientes = Clientes.objects.all()
    return render(request, "gestionarClientes.html", {"misclientes": losclientes})

# Registrar un nuevo cliente
def registrarClientes(request):
    id_clientes = request.POST["txtcodigo"]
    nombre = request.POST["txtnombre"]
    apellido = request.POST["txtapellido"]
    email = request.POST["txtemail"]
    telefono = request.POST["txttelefono"]
    fecha_reg = request.POST["datefecha_reg"]
    direccion = request.POST["txtdireccion"]
    codigo_postal = request.POST["txtcodigo_postal"]

    Clientes.objects.create(
        id_clientes=id_clientes, 
        nombre=nombre, 
        apellido=apellido, 
        email=email, 
        telefono=telefono, 
        fecha_reg=fecha_reg, 
        direccion=direccion,
        codigo_postal = codigo_postal
    )

    return redirect("clientes")

# Seleccionar un cliente para editarlo
def seleccionarClientes(request, id_clientes):
    cliente = Clientes.objects.get(id_clientes=id_clientes)
    return render(request, "editarClientes.html", {"misclientes": cliente})

# Editar un cliente existente
def editarClientes(request):
    id_clientes = request.POST["txtcodigo"]
    nombre = request.POST["txtnombre"]
    apellido = request.POST["txtapellido"]
    email = request.POST["txtemail"]
    telefono = request.POST["txttelefono"]
    fecha_reg = request.POST["datefecha_reg"]
    direccion = request.POST["txtdireccion"]
    codigo_postal = request.POST["txtcodigo_postal"]

    cliente = Clientes.objects.get(id_clientes=id_clientes)
    cliente.nombre = nombre
    cliente.apellido = apellido
    cliente.email = email
    cliente.telefono = telefono
    cliente.fecha_reg = fecha_reg
    cliente.direccion = direccion
    cliente.codigo_postal = codigo_postal
    cliente.save()

    return redirect("clientes")

# Borrar un cliente
def borrarClientes(request, id_clientes):
    cliente = Clientes.objects.get(id_clientes=id_clientes)
    cliente.delete()
    return redirect("clientes")
