from django.shortcuts import render,redirect
from .models import Producto
from .forms import productoForm
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
from .serializers import WarehouseSerializer
from rest_framework.decorators import api_view


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
        product_data = JSONParser().parse(request)
        serializer = WarehouseSerializer(data=product_data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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

def listProduct(request):
    if request.method == 'GET':
        products = Producto.objects.all()
        serializer  = WarehouseSerializer(products, many=True)
        return JsonResponse(serializer.data, safe=False)

def deleteProduct(request,id_producto):
    products =Producto.objects.get(id_producto = id_producto)
    products.delete()
    return redirect('index')

