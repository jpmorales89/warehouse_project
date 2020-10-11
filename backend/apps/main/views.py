from django.shortcuts import render
from .models import Producto

def inicio(request):
    return render(request,'index.html')
