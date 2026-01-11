from django import forms
from .models import Grupos, Artista, Pais, Ciudad, Compañias

class GirlGroupForm(forms.ModelForm):
    class Meta:
        model = Grupos
        # Definimos los campos que pediste
        # fields = ['nombre', 'tipo', 'nombre_fandom', 'fecha_debut', 'pais', 'ciudad', 'compañia', 'mega']
        fields = ['nombre', 'tipo', 'nombre_fandom', 'fecha_debut', 'pais', 'compañia', 'mega']
        
        # Personalizamos los widgets (el HTML que se genera)
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}),
            'tipo': forms.Select(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'nombre_fandom': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}),
            'fecha_debut': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'pais': forms.Select(attrs={'class': 'form-select'}),
            #'ciudad': forms.Select(attrs={'class': 'form-select', 'disabled': 'disabled'}),
            'compañia': forms.Select(attrs={'class': 'form-select'}),
            'mega': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Bloqueamos el campo 'tipo' para que siempre sea GG
        self.fields['tipo'].initial = 'GG' 
        # Esto hace que aunque el usuario intente cambiarlo en el HTML, el servidor lo ignore
        self.fields['tipo'].disabled = True

class ArtistaForm(forms.ModelForm):
    class Meta:
        model = Artista
        # Definimos los campos que pediste
        fields = ['nombre', 'nombre_nacimiento', 'fecha_nacimiento', 'pais', 'ciudad', 'compañia', 'mega']
        
        # Personalizamos los widgets (el HTML que se genera)
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}),
            'nombre_nacimiento': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}),
            'fecha_nacimiento': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'pais': forms.Select(attrs={'class': 'form-select'}),
            'ciudad': forms.Select(attrs={'class': 'form-select', 'disabled': 'disabled'}),
            'compañia': forms.Select(attrs={'class': 'form-select'}),
            'mega': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class PaisForm(forms.ModelForm):
    class Meta:
        model = Pais
        fields = ['nombre']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'id': 'id_nombre_pais'})
        }

class CompañiasForm(forms.ModelForm):
    class Meta:
        model = Compañias
        fields = ['nombre']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'id': 'id_compañia'})
        }