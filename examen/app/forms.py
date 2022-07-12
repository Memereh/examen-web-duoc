from dataclasses import fields
from django import forms
from .models import *

class ContactoForm(forms.ModelForm):
    
    class Meta:
        model = CONTACTO
        #fields = ['nombre', 'tipo_consulta', 'email', 'avisos', 'mensaje']
        fields = '__all__'