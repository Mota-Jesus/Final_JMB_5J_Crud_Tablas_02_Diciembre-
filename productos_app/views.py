from django.shortcuts import render, redirect
from .models import Productos

# Vista principal: mostrar lista de productos
def inicio_vistaProductos(request):
    losproductos = Productos.objects.all()
    return render(request, "gestionarProductos.html", {"misproductos": losproductos})

# Registrar un nuevo producto
def registrarProductos(request):
    id_productos = request.POST["txtcodigo"]
    nombre = request.POST["txtnombre"]
    descripcion = request.POST["txtdescripcion"]
    precio = request.POST["numprecio"]
    stock = request.POST["numstock"]
    categoria = request.POST["txtcategoria"]
    fecha_añadido = request.POST["datefecha_a"]
    id_proveedor = request.POST["txtproveedor"]

    guardarproductos = Productos.objects.create(
        id_productos=id_productos,
        nombre=nombre,
        descripcion=descripcion,
        precio=precio,
        stock=stock,
        categoria=categoria,
        fecha_añadido=fecha_añadido,
        id_proveedor=id_proveedor
    )

    return redirect("productos")

# Seleccionar un producto para editarlo
def seleccionarProductos(request, id_productos):
    producto = Productos.objects.get(id_productos=id_productos)
    return render(request, "editarproductos.html", {"misproductos": producto})

# Editar un producto
def editarProductos(request):
    id_productos = request.POST["txtcodigo"]
    nombre = request.POST["txtnombre"]
    descripcion = request.POST["txtdescripcion"]
    precio = request.POST["numprecio"]
    stock = request.POST["numstock"]
    categoria = request.POST["txtcategoria"]
    fecha_añadido = request.POST["datefecha_a"]
    id_proveedor = request.POST["txtproveedor"]

    producto = Productos.objects.get(id_productos=id_productos)
    producto.nombre = nombre
    producto.descripcion = descripcion
    producto.precio = precio
    producto.stock = stock
    producto.categoria = categoria
    producto.fecha_añadido = fecha_añadido
    producto.id_proveedor = id_proveedor
    producto.save()

    return redirect("productos")

# Borrar un producto
def borrarProductos(request, id_productos):
    producto = Productos.objects.get(id_productos=id_productos)
    producto.delete()
    return redirect("productos")
