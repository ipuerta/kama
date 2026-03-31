from django import forms
from django.db.models.functions import Lower
from .models import Grupos, Artistas, Artistas_Grupos, Ciudades, Paises, Compañias, Grupos_Compañias, Artistas_Compañias, Videos, Secciones, Videos_Grupos, Videos_Artistas

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
        
        self.fields['padre'].queryset = Grupos.objects.all().order_by(Lower('nombre'))
        self.fields['pais'].queryset = Paises.objects.all().order_by(Lower('nombre'))

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
        
        self.fields['padre'].queryset = Grupos.objects.all().order_by(Lower('nombre'))
        self.fields['pais'].queryset = Paises.objects.all().order_by(Lower('nombre'))

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
        
        self.fields['pais'].queryset = Paises.objects.all().order_by(Lower('nombre'))
        self.fields['ciudad'].queryset = Ciudades.objects.all().order_by(Lower('nombre'))

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
        
        self.fields['pais'].queryset = Paises.objects.all().order_by(Lower('nombre'))
        self.fields['ciudad'].queryset = Ciudades.objects.all().order_by(Lower('nombre'))

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
        
        self.fields['grupo'].queryset = Grupos.objects.all().order_by(Lower('nombre'))

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

class AltaCompañia(forms.ModelForm):
    class Meta:
        model = Compañias
        fields = ['nombre', 'padre', 'pais']
        
        # Personalizamos los widgets (el HTML que se genera)
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}),
            'padre': forms.Select(attrs={'class': 'form-select'}),
            'pais': forms.Select(attrs={'class': 'form-select'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['padre'].queryset = Compañias.objects.all().order_by(Lower('nombre'))
        self.fields['pais'].queryset = Paises.objects.all().order_by(Lower('nombre'))

class ModCompañiaForm(forms.ModelForm):
    class Meta:
        model = Compañias
        fields = ['nombre', 'padre', 'pais']
        
        # Personalizamos los widgets (el HTML que se genera)
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}),
            'padre': forms.Select(attrs={'class': 'form-select'}),
            'pais': forms.Select(attrs={'class': 'form-select'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['padre'].queryset = Compañias.objects.all().order_by(Lower('nombre'))
        self.fields['pais'].queryset = Paises.objects.all().order_by(Lower('nombre'))

class AltaGrupoCompañia(forms.ModelForm):
    class Meta:
        model = Grupos_Compañias
        fields = ['grupo', 'compañia', 'fecha_desde', 'fecha_hasta']
        
        # Personalizamos los widgets (el HTML que se genera)
        widgets = {
            'grupo': forms.HiddenInput(),
            'compañia': forms.Select(attrs={'class': 'form-select'}),
            'fecha_desde': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'fecha_hasta': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['compañia'].queryset = Compañias.objects.all().order_by(Lower('nombre'))

class AltaArtistaCompañia(forms.ModelForm):
    class Meta:
        model = Artistas_Compañias
        fields = ['artista', 'compañia', 'fecha_desde', 'fecha_hasta']
        
        # Personalizamos los widgets (el HTML que se genera)
        widgets = {
            'artista': forms.HiddenInput(),
            'compañia': forms.Select(attrs={'class': 'form-select'}),
            'fecha_desde': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'fecha_hasta': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['compañia'].queryset = Compañias.objects.all().order_by(Lower('nombre'))

class AltaVideo(forms.ModelForm):
    class Meta:
        model = Videos
        fields = ['nombre', 'enlace', 'fecha', 'seccion']
        
        # Personalizamos los widgets (el HTML que se genera)
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}),
            'enlace': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}),
            'fecha': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'seccion': forms.HiddenInput(attrs={'class': 'form-control', 'placeholder': ''}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['seccion'].queryset = Secciones.objects.all().order_by('orden')

class AltaVideoGrupo(forms.ModelForm):
    class Meta:
        model = Videos_Grupos
        fields = ['video', 'grupo']
        
        # Personalizamos los widgets (el HTML que se genera)
        widgets = {
            'video': forms.HiddenInput(),
            'grupo': forms.Select(attrs={'class': 'form-select'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['grupo'].queryset = Grupos.objects.all().order_by(Lower('nombre'))

class AltaVideoArtista(forms.ModelForm):
    class Meta:
        model = Videos_Artistas
        fields = ['video', 'artista']
        
        # Personalizamos los widgets (el HTML que se genera)
        widgets = {
            'video': forms.HiddenInput(),
            'artista': forms.Select(attrs={'class': 'form-select'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['artista'].queryset = Artistas.objects.all().order_by(Lower('nombre'))

class AltaSeccion(forms.ModelForm):
    class Meta:
        model = Secciones
        fields = ['nombre', 'padre', 'orden']
        
        # Personalizamos los widgets (el HTML que se genera)
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}),
            'padre': forms.HiddenInput(attrs={'class': 'form-control', 'placeholder': ''}),
            'orden': forms.HiddenInput(attrs={'class': 'form-control', 'placeholder': ''}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)