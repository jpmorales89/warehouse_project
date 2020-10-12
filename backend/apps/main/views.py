from django.shortcuts import render,redirect
from .models import Producto
from .forms import productoForm


def inicio(request):
    allProducts = Producto.objects.all()
    print(allProducts)
    context = {
        'products': allProducts
    }
    return render(request, 'index.html', context)


def createProduct(request):
    if request.method == 'GET':
        form = productoForm()
        context = {
        'form': form
        }
    else:
        form = productoForm(request.POST)
        context = {
        'form': form
        }
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request, 'create_product.html', context)

def editProduct(request,id_producto):
    products =Producto.objects.get(id_producto = id_producto)
    if request.method == 'GET':
        form = productoForm(instance= products)
        context = {
            'form': form
        }
    else:
        form = productoForm(request.POST, instance=products)
        if form.is_valid:
            form.save()
            return redirect('index')
    return render(request,'create_product.html',context)

def deleteProduct(request,id_producto):
    products =Producto.objects.get(id_producto = id_producto)
    products.delete()
    return redirect('index')

