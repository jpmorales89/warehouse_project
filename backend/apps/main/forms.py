from django import forms
from .models import Producto

# if i want to retrieve specific fields, use this syntx ('nombre','descripcion')
class productoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'