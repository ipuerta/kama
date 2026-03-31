from django.contrib import admin
from .models import (Paises, Ciudades, Compañias, Artistas, Artistas_Nombres, Artistas_Compañias, Grupos, Grupos_Nombres, Grupos_Compañias, Artistas_Grupos, 
                     Secciones, Videos, Videos_Grupos, Videos_Artistas)

#@admin.register(Paises)
#class PaisesAdmin(admin.ModelAdmin):
#    Campos que se muestran en el admin
#    list_display = ('nombre')
    
#    Opcional: permite que se pueda hacer clic en los campos para editar
#    list_display_links = ('nombre',)
    
#    Opcional: añade un buscador por los campos indicados
#    search_fields = ('nombre',)

@admin.register(Paises)
class PaisesAdmin(admin.ModelAdmin):
    list_display = ('nombre', )
    
    list_display_links = ('nombre',)
    
    search_fields = ('nombre',)

@admin.register(Ciudades)
class CiudadesAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'pais')
    
    list_display_links = ('nombre',)
    
    search_fields = ('nombre',)
    
@admin.register(Compañias)
class CompañiasAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'padre', 'pais')
    
    list_display_links = ('nombre',)
    
    search_fields = ('nombre',)
    
@admin.register(Artistas)
class ArtistasAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'nombre_coreano', 'nombre_japones', 'nombre_chino', 'nombre_tailandes', 'fecha_nacimiento', 'pais', 'ciudad', 'enlace')
    
    list_display_links = ('nombre',)
    
    search_fields = ('nombre',)
    
@admin.register(Artistas_Nombres)
class ArtistasNombresAdmin(admin.ModelAdmin):
    list_display = ('artista', 'nombre', 'fecha_desde', 'fecha_hasta')
    
    list_display_links = ('artista',)
    
    search_fields = ('nombre',)
    
@admin.register(Artistas_Compañias)
class ArtistasCompañiasAdmin(admin.ModelAdmin):
    list_display = ('artista', 'compañia', 'fecha_desde', 'fecha_hasta')
    
    list_display_links = ('artista',)

    search_fields = ('artista.nombre', 'compañia.nombre')
     
@admin.register(Grupos)
class GruposAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'nombre_coreano', 'padre', 'nombre_fandom', 'fecha_debut', 'pais', 'enlace')
    
    list_display_links = ('nombre',)
    
    search_fields = ('nombre', 'nombre_fandom')
     
@admin.register(Grupos_Nombres)
class GruposNombresAdmin(admin.ModelAdmin):
    list_display = ('grupo', 'nombre', 'fecha_desde', 'fecha_hasta')
    
    list_display_links = ('nombre',)
    
    search_fields = ('grupo.nombre', 'nombre')
     
@admin.register(Grupos_Compañias)
class GruposCompañiasAdmin(admin.ModelAdmin):
    list_display = ('grupo', 'compañia', 'fecha_desde', 'fecha_hasta')
    
    list_display_links = ('grupo',)
    
    search_fields = ('grupo.nombre', 'compañia.nombre')
     
@admin.register(Artistas_Grupos)
class ArtistasGruposAdmin(admin.ModelAdmin):
    list_display = ('artista', 'grupo', 'fecha_desde', 'fecha_hasta')
    
    list_display_links = ('artista',)
    
    search_fields = ('artista.nombre', 'grupo.nombre')
     
@admin.register(Secciones)
class SeccionesAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'padre', 'orden')
    
    list_display_links = ('nombre',)
    
    search_fields = ('nombre',)
     
@admin.register(Videos)
class VideosAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'enlace', 'fecha', 'seccion')
    
    list_display_links = ('nombre',)
    
    search_fields = ('nombre',)
     
@admin.register(Videos_Grupos)
class VideosGruposAdmin(admin.ModelAdmin):
    list_display = ('video', 'grupo')
    
    list_display_links = ('video',)
    
    search_fields = ('video', 'grupo.nombre')
     
@admin.register(Videos_Artistas)
class VideosArtistasAdmin(admin.ModelAdmin):
    list_display = ('video', 'artista')
    
    list_display_links = ('video',)
    
    search_fields = ('video', 'artista.nombre')





