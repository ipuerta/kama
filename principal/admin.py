from django.contrib import admin
from .models import Genero, Pais, Ciudad, Compañias, Artista, Artista_Nombres, Artista_Compañias, Grupos, Grupos_Nombres, Grupos_Compañias, Artista_Grupos, Secciones, Videos

admin.site.register(Genero)
admin.site.register(Pais)
admin.site.register(Ciudad)
admin.site.register(Compañias)
admin.site.register(Artista)
admin.site.register(Artista_Nombres)
admin.site.register(Artista_Compañias)
admin.site.register(Grupos)
admin.site.register(Grupos_Nombres)
admin.site.register(Grupos_Compañias)
admin.site.register(Artista_Grupos)
admin.site.register(Secciones)
admin.site.register(Videos)