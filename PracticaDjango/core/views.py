from email.mime import message
from itertools import product
from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators import csrf
from .models import *
from .forms import *
from django.contrib.auth.forms import UserCreationForm
from core.carrito import Carrito
# Create your views here.
TEMPLATE_DIR =(
    'os.path.join(BASE_DIR, "templates"),'
)

def home(request):
    return render(request, 'home.html')

def catalogo(request):
    productos = Producto.objects.all()
    return render(request, 'catalogo.html', {'productos':productos})

def nosotros(request):
    return render(request, 'nosotros.html')

def contacto(request):
    return render(request, 'contacto.html')

def registro(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, F'Usuario {username} Creado')
            return redirect('home')
    else:
         form = UserRegisterForm()

    context = { 'form' : form}
    return render(request, 'registro.html', context)
def mostrar_clientes(request):
    cliente = Cliente.objects.all()

    datos={
        'cliente': cliente
        }
    return render(request, 'mostrar_clientes.html', datos)

def mostrar_productos(request):
    producto = Producto.objects.all()

    datos={
        'producto': producto
        }
    return render(request, 'mostrar_productos.html', datos)


def form_clientes(request):
    if request.method == 'POST':
        cliente_form = ClienteForm(request.POST)
        if cliente_form.is_valid():
            cliente_form.save()
            return redirect('home')
    else:
        cliente_form = ClienteForm()
    return render(request, 'form_clientes.html', {'cliente_form' : cliente_form})

def form_productos(request):
    if request.method == 'POST':
        producto_form = ProductoForm(request.POST)
        if producto_form.is_valid():
            producto_form.save()
            return redirect('home')
    else:
        producto_form = ProductoForm()
    return render(request, 'form_productos.html', {'producto_form' : producto_form})

def form_mod_clientes(request, id):
    cliente = Cliente.objects.get(rutcliente=id)
    datos={
        'form': ClienteForm(data = request.POST, instance=cliente)
    }
    if request.method=='POST':
        formulario = ClienteForm(data = request.POST, instance=cliente)
        if formulario.is_valid():
            formulario.save()
            return redirect('mostrar_clientes')
    return render(request, 'form_mod_clientes.html', datos)

def form_mod_productos(request, id):
    producto = Producto.objects.get(codigo=id)
    datos={
        'form2' : ProductoForm(data = request.POST, instance=producto)
    }
    if request.method=='POST':
        formulario2 = ProductoForm(data = request.POST, instance=producto)
        if formulario2.is_valid():
            formulario2.save()
            return redirect('mostrar_productos')
    return render(request, 'form_mod_productos.html', datos)

def form_del_clientes(request, id):
    cliente = Cliente.objects.get(rutcliente=id)
    cliente.delete()
    return redirect('mostrar_clientes')

def form_del_productos(request,id):
    producto = Producto.objects.get(codigo=id)
    producto.delete()
    return redirect('mostrar_productos')

def agregar_producto (request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.agregar(producto)
    return redirect("core: catalogo")

def eliminar_producto (request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.eliminar(producto)
    return redirect("core: catalogo")

def restar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.restar(producto)
    return redirect("core: catalogo")

def limpiar_carrito(request, producto_id):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect("core: catalogo")