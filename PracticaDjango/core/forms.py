from pyexpat import model
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.forms import widgets
from django.forms.models import ModelChoiceField
from django.forms.widgets import Widget
from . models import Cliente, Producto

class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label="Usuario", widget=forms.TextInput)
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    class meta:
        model = User
        fields ={'username','email','password1','password2'}
        help_text = {k:" " for k in fields}

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['codigo','nombre','precio','stock','descripcion']
        labels ={
            'codigo':'Codigo',
            'nombre':'Nombre',
            'precio':'Precio',
            'stock':'Stock',
            'descripcion':'Descripcion',
        }
        widgets={
            'codigo': forms.NumberInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ingrese Codigo',
                    'id':'codigo'
                }
            ),
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese Nombre',
                    'id' : 'nombre'
                }
            ),
            'precio': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder' : 'Ingrese Precio',
                    'id' : 'precio'
                }
            ),
            'stock': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese Stock',
                    'id' : 'stock'
                }
            ),
            'descripcion': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder' : 'Ingrese Descripcion'
                }
            )
        }

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields =['rutcliente','nombre','correo','telefono','direccion']
        labels ={
            'rutcliente': 'Rut cliente: ',
            'nombre': 'Nombre: ',
            'correo': 'Correo: ',
            'telefono': 'Telefono: ',
            'direccion': 'Direccion: ',
        }
        widgets={
            'rutcliente': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese Rut',
                    'id' : 'rutcliente'
                    }
            ),
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese nombre',
                    'id' : 'nombre'
                }
            ),
            'correo': forms.EmailInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese Correo',
                    'id' : 'correo'
                }
            ),
            'telefono': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese Telefono',
                    'id' : 'telefono'
                }
            ),
            'direccion': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese direccion',
                    'id' : 'direccion'
                }
            )
        }