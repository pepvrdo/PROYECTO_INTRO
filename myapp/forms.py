from django import forms
from .models import Usuario

class RegistroUsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['name', 'apellido', 'contacto', 'num_contacto', 'texto']
        labels = {
            'name': 'Nombre',
            'apellido': 'Apellido',
            'contacto': 'Contacto de emergencia',
            'num_contacto': 'Número de contacto',
            'texto': 'Mensaje de ayuda',
        }