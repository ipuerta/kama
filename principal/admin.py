from django.contrib import admin
from .models import (Genero, Pais, Ciudad, Compañias, Artista, Artista_Nombres, Artista_Compañias, Grupos, Grupos_Nombres, Grupos_Compañias, Artista_Grupos, Secciones, Videos, Videos_Grupos,
                     Videos_Artistas, Artistas_Generos, Grupos_Generos)

@admin.register(Genero)
class GeneroAdmin(admin.ModelAdmin):
    # 'id' es el nombre del campo automático que crea Django
    list_display = ('id', 'nombre')
    
    # Opcional: permite que se pueda hacer clic en el nombre para editar
    list_display_links = ('nombre',)
    
    # Opcional: añade un buscador por nombre
    search_fields = ('nombre',)

@admin.register(Pais)
class PaisAdmin(admin.ModelAdmin):
    # 'id' es el nombre del campo automático que crea Django
    list_display = ('id', 'nombre')
    
    # Opcional: permite que se pueda hacer clic en el nombre para editar
    list_display_links = ('nombre',)
    
    # Opcional: añade un buscador por nombre
    search_fields = ('nombre',)

@admin.register(Ciudad)
class CiudadAdmin(admin.ModelAdmin):
    # 'id' es el nombre del campo automático que crea Django
    list_display = ('id', 'nombre', 'pais')
    
    # Opcional: permite que se pueda hacer clic en el nombre para editar
    list_display_links = ('nombre',)
    
    # Opcional: añade un buscador por nombre
    search_fields = ('nombre',)
    
@admin.register(Compañias)
class CompañiasAdmin(admin.ModelAdmin):
    # 'id' es el nombre del campo automático que crea Django
    list_display = ('id_compañia', 'nombre')
    
    # Opcional: permite que se pueda hacer clic en el nombre para editar
    list_display_links = ('nombre',)
    
    # Opcional: añade un buscador por nombre
    search_fields = ('nombre',)
    
@admin.register(Artista)
class ArtistaAdmin(admin.ModelAdmin):
    # 'id' es el nombre del campo automático que crea Django
    list_display = ('id_artista', 'nombre', 'nombre_nacimiento', 'fecha_nacimiento', 'pais', 'ciudad', 'compañia', 'mega')
    
    # Opcional: permite que se pueda hacer clic en el nombre para editar
    list_display_links = ('nombre',)
    
    # Opcional: añade un buscador por nombre
    search_fields = ('nombre',)
    
@admin.register(Artista_Nombres)
class ArtistaNombresAdmin(admin.ModelAdmin):
    # 'id' es el nombre del campo automático que crea Django
    list_display = ('id_relacion', 'artista', 'nombre', 'fecha_desde', 'fecha_hasta')
    
    # Opcional: permite que se pueda hacer clic en el nombre para editar
    list_display_links = ('artista',)
    
    # Opcional: añade un buscador por nombre
    search_fields = ('nombre',)
    
@admin.register(Artista_Compañias)
class ArtistaCompañiasAdmin(admin.ModelAdmin):
    # 'id' es el nombre del campo automático que crea Django
    list_display = ('id_relacion', 'artista', 'compañia', 'fecha_desde', 'fecha_hasta')
    
    # Opcional: permite que se pueda hacer clic en el nombre para editar
    list_display_links = ('artista',)
     
@admin.register(Grupos)
class GruposAdmin(admin.ModelAdmin):
    # 'id' es el nombre del campo automático que crea Django
    list_display = ('id_grupo', 'tipo', 'nombre', 'nombre_fandom', 'fecha_debut', 'pais', 'ciudad', 'compañia', 'mega')
    
    # Opcional: permite que se pueda hacer clic en el nombre para editar
    list_display_links = ('nombre',)
    
    # Opcional: añade un buscador por nombre
    search_fields = ('nombre', 'nombre_fandom')
     
@admin.register(Grupos_Nombres)
class GruposNombresAdmin(admin.ModelAdmin):
    # 'id' es el nombre del campo automático que crea Django
    list_display = ('id_relacion', 'grupo', 'nombre', 'fecha_desde', 'fecha_hasta')
    
    # Opcional: permite que se pueda hacer clic en el nombre para editar
    list_display_links = ('nombre',)
    
    # Opcional: añade un buscador por nombre
    search_fields = ('nombre', )
     
@admin.register(Grupos_Compañias)
class GruposCompañiasAdmin(admin.ModelAdmin):
    # 'id' es el nombre del campo automático que crea Django
    list_display = ('id_relacion', 'grupo', 'compañia', 'fecha_desde', 'fecha_hasta')
    
    # Opcional: permite que se pueda hacer clic en el nombre para editar
    list_display_links = ('grupo',)
     
@admin.register(Artista_Grupos)
class ArtistaGruposAdmin(admin.ModelAdmin):
    # 'id' es el nombre del campo automático que crea Django
    list_display = ('id_relacion', 'artista', 'grupo', 'fecha_desde', 'fecha_hasta')
    
    # Opcional: permite que se pueda hacer clic en el nombre para editar
    list_display_links = ('artista',)
     
@admin.register(Secciones)
class SeccionesAdmin(admin.ModelAdmin):
    # 'id' es el nombre del campo automático que crea Django
    list_display = ('id_seccion', 'id_seccion_padre', 'orden', 'titulo')
    
    # Opcional: permite que se pueda hacer clic en el nombre para editar
    list_display_links = ('titulo',)
    
    # Opcional: permite que se pueda hacer clic en el nombre para editar
    search_fields = ('titulo',)
     
@admin.register(Videos)
class VideosAdmin(admin.ModelAdmin):
    # 'id' es el nombre del campo automático que crea Django
    list_display = ('id_video', 'titulo', 'youtube', 'fecha', 'seccion')
    
    # Opcional: permite que se pueda hacer clic en el nombre para editar
    list_display_links = ('titulo',)
    
    # Opcional: permite que se pueda hacer clic en el nombre para editar
    search_fields = ('titulo',)
     
@admin.register(Videos_Grupos)
class VideosGruposAdmin(admin.ModelAdmin):
    # 'id' es el nombre del campo automático que crea Django
    list_display = ('video', 'grupo')
    
    # Opcional: permite que se pueda hacer clic en el nombre para editar
    list_display_links = ('video',)
     
@admin.register(Videos_Artistas)
class VideosArtistasAdmin(admin.ModelAdmin):
    # 'id' es el nombre del campo automático que crea Django
    list_display = ('video', 'artista')
    
    # Opcional: permite que se pueda hacer clic en el nombre para editar
    list_display_links = ('video',)
     
@admin.register(Artistas_Generos)
class ArtistasGenerosAdmin(admin.ModelAdmin):
    # 'id' es el nombre del campo automático que crea Django
    list_display = ('artista', 'genero')
    
    # Opcional: permite que se pueda hacer clic en el nombre para editar
    list_display_links = ('artista',)
     
@admin.register(Grupos_Generos)
class GruposGenerosAdmin(admin.ModelAdmin):
    # 'id' es el nombre del campo automático que crea Django
    list_display = ('grupo', 'genero')
    
    # Opcional: permite que se pueda hacer clic en el nombre para editar
    list_display_links = ('grupo',)





