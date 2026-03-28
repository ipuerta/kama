from django import forms
from .models import Grupos, Artistas, Artistas_Grupos, Ciudades, Paises

class AltaGrupoForm(forms.ModelForm):
    class Meta:
        model = Grupos
        fields = ['nombre', 'nombre_coreano', 'padre', 'nombre_fandom', 'fecha_debut', 'pais', 'enlace']
        
        # Personalizamos los widgets (el HTML que se genera)
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}),
            'nombre_coreano': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}),
            'padre': forms.Select(attrs={'class': 'form-select'}),
            'nombre_fandom': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}),
            'fecha_debut': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'pais': forms.Select(attrs={'class': 'form-select'}),
            'enlace': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class ModGrupoForm(forms.ModelForm):
    class Meta:
        model = Grupos
        fields = ['nombre', 'nombre_coreano', 'padre', 'nombre_fandom', 'fecha_debut', 'pais', 'enlace']
        
        # Personalizamos los widgets (el HTML que se genera)
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre_coreano': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}),
            'padre': forms.Select(attrs={'class': 'form-select'}),
            'nombre_fandom': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_debut': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'pais': forms.Select(attrs={'class': 'form-select'}),
            'enlace': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class AltaArtistaForm(forms.ModelForm):
    class Meta:
        model = Artistas
        fields = ['nombre', 'nombre_coreano', 'nombre_japones', 'nombre_chino', 'nombre_tailandes', 'fecha_nacimiento', 'pais', 'ciudad', 'enlace']
        
        # Personalizamos los widgets (el HTML que se genera)
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}),
            'nombre_coreano': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}),
            'nombre_japones': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}),
            'nombre_chino': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}),
            'nombre_tailandes': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}),
            'fecha_nacimiento': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'pais': forms.Select(attrs={'class': 'form-select'}),
            'ciudad': forms.Select(attrs={'class': 'form-select'}),
            'enlace': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class ModArtistaForm(forms.ModelForm):
    class Meta:
        model = Artistas
        fields = ['nombre', 'nombre_coreano', 'nombre_japones', 'nombre_chino', 'nombre_tailandes', 'fecha_nacimiento', 'pais', 'ciudad', 'enlace']
        
        # Personalizamos los widgets (el HTML que se genera)
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}),
            'nombre_coreano': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}),
            'nombre_japones': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}),
            'nombre_chino': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}),
            'nombre_tailandes': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}),
            'fecha_nacimiento': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'pais': forms.Select(attrs={'class': 'form-select'}),
            'ciudad': forms.Select(attrs={'class': 'form-select'}),
            'enlace': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class AltaRelacion(forms.ModelForm):
    class Meta:
        model = Artistas_Grupos
        fields = ['artista', 'grupo', 'fecha_desde', 'fecha_hasta']
        
        # Personalizamos los widgets (el HTML que se genera)
        widgets = {
            'artista': forms.HiddenInput(),
            'grupo': forms.Select(attrs={'class': 'form-select'}),
            'fecha_desde': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'fecha_hasta': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class AltaCiudad(forms.ModelForm):
    class Meta:
        model = Ciudades
        fields = ['nombre', 'pais']
        
        # Personalizamos los widgets (el HTML que se genera)
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}),
            'pais': forms.HiddenInput(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class AltaPais(forms.ModelForm):
    class Meta:
        model = Paises
        fields = ['nombre', ]
        
        # Personalizamos los widgets (el HTML que se genera)
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

#class BandaForm(forms.ModelForm):
#    class Meta:
#        model = Grupos
#        # Definimos los campos que pediste
#        # fields = ['nombre', 'tipo', 'nombre_fandom', 'fecha_debut', 'pais', 'ciudad', 'compañia', 'mega']
#        fields = ['nombre', 'tipo', 'nombre_fandom', 'fecha_debut', 'pais', 'compañia', 'mega']
        
#        # Personalizamos los widgets (el HTML que se genera)
#        widgets = {
#            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}),
#            'tipo': forms.Select(attrs={'class': 'form-control', 'readonly': 'readonly'}),
#            'nombre_fandom': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}),
#            'fecha_debut': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
#            'pais': forms.Select(attrs={'class': 'form-select'}),
#            #'ciudad': forms.Select(attrs={'class': 'form-select', 'disabled': 'disabled'}),
#            'compañia': forms.Select(attrs={'class': 'form-select'}),
#            'mega': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}),
#        }

#    def __init__(self, *args, **kwargs):
#        super().__init__(*args, **kwargs)
#        # Bloqueamos el campo 'tipo' para que siempre sea BAND
#        self.fields['tipo'].initial = 'BAND' 
#        # Esto hace que aunque el usuario intente cambiarlo en el HTML, el servidor lo ignore
#        self.fields['tipo'].disabled = True

#class ArtistaForm(forms.ModelForm):
#    class Meta:
#        model = Artista
#        # Definimos los campos que pediste
#        fields = ['nombre', 'nombre_nacimiento', 'fecha_nacimiento', 'pais', 'ciudad', 'compañia', 'mega']
        
#        # Personalizamos los widgets (el HTML que se genera)
#        widgets = {
#            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}),
#            'nombre_nacimiento': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}),
#            'fecha_nacimiento': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
#            'pais': forms.Select(attrs={'class': 'form-select'}),
#            'ciudad': forms.Select(attrs={'class': 'form-select', 'disabled': 'disabled'}),
#            'compañia': forms.Select(attrs={'class': 'form-select'}),
#            'mega': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}),
#        }

#    def __init__(self, *args, **kwargs):
#        super().__init__(*args, **kwargs)

#class PaisForm(forms.ModelForm):
#    class Meta:
#        model = Pais
#        fields = ['nombre']
#        widgets = {
#            'nombre': forms.TextInput(attrs={'class': 'form-control', 'id': 'id_nombre_pais'})
#        }

#class CompañiasForm(forms.ModelForm):
#    class Meta:
#        model = Compañias
#        fields = ['nombre']
#        widgets = {
#            'nombre': forms.TextInput(attrs={'class': 'form-control', 'id': 'id_compañia'})
#        }