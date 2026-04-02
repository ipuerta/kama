from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models.functions import Lower
from datetime import datetime
from .models import Paises, Ciudades, Grupos, Artistas, Artistas_Grupos, Compañias, Grupos_Compañias, Artistas_Compañias, Secciones, Videos, Videos_Grupos, Videos_Artistas
from .forms import AltaGrupoForm, ModGrupoForm, AltaArtistaForm, ModArtistaForm, AltaRelacion, AltaCiudad, AltaPais, AltaCompañia, ModCompañiaForm, AltaGrupoCompañia, AltaArtistaCompañia
from .forms import AltaVideo, AltaVideoGrupo, AltaVideoArtista, AltaSeccion
from django.views.decorators.csrf import csrf_protect


def obtenerArbolSecciones(seccionesFiltrar):
    # Obtener todos los ids
    idsSecciones = []

    def obtenerIdPadres (idHijo):
        seccionPadre = Secciones.objects.get(id=idHijo).padre
        if seccionPadre:
            if seccionPadre.id not in idsSecciones:
                idsSecciones.append(seccionPadre.id)
                obtenerIdPadres (seccionPadre.id)

    for s in seccionesFiltrar:
        if s.id not in idsSecciones:
            idsSecciones.append(s.id)
            obtenerIdPadres (s.id)

    # Obtener todas las secciones
    seccionesPadres = Secciones.objects.filter(id__in=idsSecciones, padre__isnull=True).order_by('orden')

    # Ordenar las secciones y añadir el nivel
    arbolSecciones = []

    def ordenar(nodos, idPadre=0, nivel=0):
        for nodo in nodos:
            print(f"Nodo: {nodo.id} {nodo.nombre} Nivel {nivel} Padre {idPadre}")

            arbolSecciones.append((nodo.id, nodo.nombre, nivel, idPadre))
            
            hijos = nodo.hijos.filter(id__in=idsSecciones).order_by('orden')
            ordenar(hijos, nodo.id, nivel + 1)

    ordenar(seccionesPadres)

    return arbolSecciones

def inicio(request):
    paises = Paises.objects.all().order_by(Lower('nombre'))

    contexto = {
        'paises': paises,
    }

    # Renderizamos el template pasando el contexto
    return render(request, 'principal/inicio.html', contexto)

def login_view(request):
    return render(request, 'principal/login.html')

def grupos(request):
    paises = Paises.objects.all().order_by(Lower('nombre'))
    grupos = Grupos.objects.all().order_by(Lower('nombre'))

    contexto = {
        'paises': paises,
        'grupos': grupos
    }

    return render(request, 'principal/listado_grupos.html', contexto)

def alta_grupo(request):
    paises = Paises.objects.all().order_by(Lower('nombre'))
    contexto = {
        'paises': paises,
    }
    
    if request.method == 'POST':
        form = AltaGrupoForm(request.POST)
        if form.is_valid():
            grupo = form.save()
            return redirect('info_grupo',  id=grupo.id)

    form = AltaGrupoForm()
    contexto = {
        'paises': paises,
        'form': form
    }
     
    return render(request, 'principal/alta_grupo.html', contexto)

def info_grupo(request, id):
    grupo = get_object_or_404(Grupos, id=id)
    hijos = grupo.hijos.all()

    if request.method == 'POST':
        if request.POST.get("formulario") == "modGrupo":
            form = ModGrupoForm(request.POST, instance=grupo)
            if form.is_valid():
                form.save()
            else:
                print(form.errors)

        if request.POST.get("formulario") == "altaGrupoCompañia":
            form2 = AltaGrupoCompañia(request.POST)
            if form2.is_valid():
                form2.save()
            else:
                print(form2.errors)

        if request.POST.get("formulario") == "modGrupoCompañia":
            grupoCompañia = get_object_or_404(Grupos_Compañias, id=request.POST.get("id_relacion"))
            form2 = AltaGrupoCompañia(request.POST, instance=grupoCompañia)
            if form2.is_valid():
                form2.save()
            else:
                print(form2.errors)

    paises = Paises.objects.all().order_by(Lower('nombre'))
    grupo = get_object_or_404(Grupos, id=id)
    relaciones = Artistas_Grupos.objects.filter(grupo=id).order_by(Lower('artista__nombre'),'artista__fecha_nacimiento')
    compañias = Grupos_Compañias.objects.filter(grupo=id).order_by(Lower('compañia__nombre'))
    form = ModGrupoForm(instance=grupo)
    form2 = AltaGrupoCompañia(initial={'grupo' : grupo})

    videos = Videos.objects.filter(videos_grupos__grupo=grupo).order_by('fecha','nombre')
    secciones = Secciones.objects.filter(videos__videos_grupos__grupo=grupo).distinct()

    arbolSecciones = obtenerArbolSecciones(secciones)

    contexto = {
        'paises': paises,
        'grupo': grupo,
        'hijos': hijos,
        'relaciones': relaciones,
        'compañias': compañias,
        'videos': videos,
        'arbolSecciones': arbolSecciones,
        'form': form,
        'form2': form2
    }
     
    return render(request, 'principal/info_grupo.html', contexto)

def artistas(request):
    paises = Paises.objects.all().order_by(Lower('nombre'))
    artistas = Artistas.objects.all().order_by(Lower('nombre'),'fecha_nacimiento')

    contexto = {
        'paises': paises,
        'artistas': artistas
    }

    return render(request, 'principal/listado_artistas.html', contexto)

def alta_artista(request):
    paises = Paises.objects.all().order_by(Lower('nombre'))
    contexto = {
        'paises': paises,
    }
    
    if request.method == 'POST':
        form = AltaArtistaForm(request.POST)
        if form.is_valid():
            artista = form.save()
            return redirect('info_artista',  id=artista.id)

    ciudades = Ciudades.objects.all()
    form = AltaArtistaForm()
    contexto = {
        'paises': paises,
        'ciudades': ciudades,
        'form': form
    }
     
    return render(request, 'principal/alta_artista.html', contexto)

def info_artista(request, id):
    artista = get_object_or_404(Artistas, id=id)

    if request.method == 'POST':

        if request.POST.get("formulario") == "modArtista":
            form = ModArtistaForm(request.POST, instance=artista)
            if form.is_valid():
                form.save()
            else:
                print(form.errors)

        if request.POST.get("formulario") == "altaRelacion":
            form2 = AltaRelacion(request.POST)
            if form2.is_valid():
                form2.save()
            else:
                print(form2.errors)

        if request.POST.get("formulario") == "modRelacion":
            artistaGrupo = get_object_or_404(Artistas_Grupos, id=request.POST.get("id_relacion"))
            form2 = AltaRelacion(request.POST, instance=artistaGrupo)
            if form2.is_valid():
                form2.save()
            else:
                print(form2.errors)

        if request.POST.get("formulario") == "altaArtistaCompañia":
            form3 = AltaArtistaCompañia(request.POST)
            if form3.is_valid():
                form3.save()
            else:
                print(form3.errors)

        if request.POST.get("formulario") == "modArtistaCompañia":
            artistaCompañia = get_object_or_404(Artistas_Compañias, id=request.POST.get("id_relacion"))
            form3 = AltaArtistaCompañia(request.POST, instance=artistaCompañia)
            if form3.is_valid():
                form3.save()
            else:
                print(form2.errors)

    paises = Paises.objects.all().order_by(Lower('nombre'))
    artista = get_object_or_404(Artistas, id=id)
    relaciones = Artistas_Grupos.objects.filter(artista=id).order_by(Lower('grupo__nombre'))
    compañias = Artistas_Compañias.objects.filter(artista=id).order_by(Lower('compañia__nombre'))
    form = ModArtistaForm(instance=artista)
    form2 = AltaRelacion(initial={'artista' : artista})
    form3 = AltaArtistaCompañia(initial={'artista' : artista})

    videos = Videos.objects.filter(videos_artistas__artista=artista).order_by('fecha','nombre')
    secciones = Secciones.objects.filter(videos__videos_artistas__artista=artista).distinct()

    arbolSecciones = obtenerArbolSecciones(secciones)

    contexto = {
        'paises': paises,
        'artista': artista,
        'relaciones': relaciones,
        'compañias': compañias,
        'videos': videos,
        'arbolSecciones': arbolSecciones,
        'form': form,
        'form2': form2,
        'form3': form3
    }
     
    return render(request, 'principal/info_artista.html', contexto)

def info_pais(request, id):
    paises = Paises.objects.all().order_by(Lower('nombre'))
    pais = get_object_or_404(Paises, id=id)
    ciudades = Ciudades.objects.filter(pais=id).order_by(Lower('nombre'))
    grupos = Grupos.objects.filter(pais=id).order_by(Lower('nombre'))
    artistas = Artistas.objects.filter(pais=id).order_by(Lower('nombre'),'fecha_nacimiento')
    compañias = Compañias.objects.filter(pais=id).order_by(Lower('nombre'))

    if request.method == 'POST':
        if request.POST.get("formulario") == "altaCiudad":
            form = AltaCiudad(request.POST)
            if form.is_valid():
                form.save()
            else:
                print(form.errors)
                
    form = AltaCiudad(initial={'pais' : pais})

    contexto = {
        'paises': paises,
        'pais': pais,
        'ciudades': ciudades,
        'grupos': grupos,
        'artistas': artistas,
        'compañias': compañias,
        'form': form
    }
     
    return render(request, 'principal/info_pais.html', contexto)

def alta_pais(request):
    paises = Paises.objects.all().order_by(Lower('nombre'))
    contexto = {
        'paises': paises,
    }
    
    if request.method == 'POST':
        form = AltaPais(request.POST)
        if form.is_valid():
            pais = form.save()
            return redirect('info_pais',  id=pais.id)
    
    form = AltaPais()
    contexto = {
        'paises': paises,
        'form': form
    }
     
    return render(request, 'principal/alta_pais.html', contexto)

def alta_compañia(request):
    paises = Paises.objects.all().order_by(Lower('nombre'))
    contexto = {
        'paises': paises,
    }
    
    if request.method == 'POST':
        form = AltaCompañia(request.POST)
        if form.is_valid():
            compañia = form.save()
            return redirect('info_comp',  id=compañia.id)
    
    form = AltaCompañia()
    contexto = {
        'paises': paises,
        'form': form
    }
     
    return render(request, 'principal/alta_comp.html', contexto)

def compañias(request):
    paises = Paises.objects.all().order_by(Lower('nombre'))
    compañias = Compañias.objects.all().order_by(Lower('nombre'))

    contexto = {
        'paises': paises,
        'compañias': compañias
    }

    return render(request, 'principal/listado_comps.html', contexto)

def info_compañia(request, id):
    compañia = get_object_or_404(Compañias, id=id)

    if request.method == 'POST':

        if request.POST.get("formulario") == "modCompañia":
            form = ModCompañiaForm(request.POST, instance=compañia)
            if form.is_valid():
                form.save()
            else:
                print(form.errors)

    paises = Paises.objects.all().order_by(Lower('nombre'))
    compañia = get_object_or_404(Compañias, id=id)
    grupos = Grupos_Compañias.objects.filter(compañia=id).order_by(Lower('grupo__nombre'))
    artistas = Artistas_Compañias.objects.filter(compañia=id).order_by(Lower('artista__nombre'),'artista__fecha_nacimiento')
    form = ModCompañiaForm(instance=compañia)

    contexto = {
        'paises': paises,
        'compañia': compañia,
        'grupos': grupos,
        'artistas': artistas,
        'form': form
    }
     
    return render(request, 'principal/info_comp.html', contexto)


def alta_video(request):
    paises = Paises.objects.all().order_by(Lower('nombre'))

    datos_form2 = {
        'nombre': '',
        'enlace': '',
        'fecha': '',
        'seccion0': '',
        'seccion1': '',
        'seccion2': '',
        'seccion3': '',
        'seccion4': ''
    }
    
    if request.method == 'POST':
        if request.POST.get("formulario") == "altaVideo":
            form = AltaVideo(request.POST)
            if form.is_valid():
                video = form.save()
                return redirect('info_video',  id=video.id)
        if request.POST.get("formulario") == "altaSeccion":
            form2 = AltaSeccion(request.POST)
            if form2.is_valid():
                save_form2 = form2.save()
                seccion0 = ''
                seccion1 = ''
                seccion2 = ''
                seccion3 = ''
                seccion4 = ''
                if request.POST.get("fSeccion0") == '':
                    seccion0 = save_form2.id
                elif request.POST.get("fSeccion1") == '':
                    seccion0 = request.POST.get("fSeccion0")
                    seccion1 = save_form2.id
                elif request.POST.get("fSeccion2") == '':
                    seccion0 = request.POST.get("fSeccion0")
                    seccion1 = request.POST.get("fSeccion1")
                    seccion2 = save_form2.id
                elif request.POST.get("fSeccion3") == '':
                    seccion0 = request.POST.get("fSeccion0")
                    seccion1 = request.POST.get("fSeccion1")
                    seccion2 = request.POST.get("fSeccion2")
                    seccion3 = save_form2.id
                elif request.POST.get("fSeccion4") == '':
                    seccion0 = request.POST.get("fSeccion0")
                    seccion1 = request.POST.get("fSeccion1")
                    seccion2 = request.POST.get("fSeccion2")
                    seccion3 = request.POST.get("fSeccion3")
                    seccion4 = save_form2.id

                datos_form2 = {
                    'nombre': request.POST.get("fNombre"),
                    'enlace': request.POST.get("fEnlace"),
                    'fecha': request.POST.get("fFecha"),
                    'seccion0': seccion0,
                    'seccion1': seccion1,
                    'seccion2': seccion2,
                    'seccion3': seccion3,
                    'seccion4': seccion4,
                    'seccionNombre': save_form2.nombre,
                    'seccionPadre': save_form2.padre,
                    'seccionOrden': save_form2.orden
                }

    secciones = obtenerArbolSecciones(Secciones.objects.all())
    form = AltaVideo()
    form2 = AltaSeccion()

    contexto = {
        'paises': paises,
        'secciones': secciones,
        'form': form,
        'form2': form2,
        'datos_form2': datos_form2
    }
     
    return render(request, 'principal/alta_video.html', contexto)


def info_video(request, id):
    video = get_object_or_404(Videos, id=id)

    if request.method == 'POST':

        if request.POST.get("formulario") == "modCompañia":
            form = AltaVideo(request.POST, instance=video)
            if form.is_valid():
                form.save()
            else:
                print(form.errors)

        if request.POST.get("formulario") == "altaVideoGrupo":
            form2 = AltaVideoGrupo(request.POST)
            if form2.is_valid():
                form2.save()
            else:
                print(form2.errors)

        if request.POST.get("formulario") == "borraVideoGrupo":
            idBorrar = request.POST.get("id_relacion")

            if idBorrar:
                Videos_Grupos.objects.filter(id=idBorrar).delete()
            else:
                print("Error al borrar")

        if request.POST.get("formulario") == "altaVideoArtista":
            form3 = AltaVideoArtista(request.POST)
            if form3.is_valid():
                form3.save()
            else:
                print(form3.errors)

        if request.POST.get("formulario") == "borraVideoArtista":
            idBorrar = request.POST.get("id_relacion")

            if idBorrar:
                Videos_Artistas.objects.filter(id=idBorrar).delete()
            else:
                print("Error al borrar")

    paises = Paises.objects.all().order_by(Lower('nombre'))
    video = get_object_or_404(Videos, id=id)
    seccionesFiltradas = obtenerArbolSecciones(Secciones.objects.filter(id=video.seccion.id))
    secciones = obtenerArbolSecciones(Secciones.objects.all())
    grupos = Grupos.objects.all()
    gruposFiltrados = Videos_Grupos.objects.filter(video=video)
    artistas = Artistas.objects.all()
    artistasFiltrados = Videos_Artistas.objects.filter(video=video)
    form = AltaVideo(instance=video)
    form2 = AltaVideoGrupo(initial={'video' : video})
    form3 = AltaVideoArtista(initial={'video' : video})

    contexto = {
        'paises': paises,
        'video': video,
        'seccionesFiltradas': seccionesFiltradas,
        'secciones': secciones,
        'grupos': grupos,
        'gruposFiltrados': gruposFiltrados,
        'artistas': artistas,
        'artistasFiltrados': artistasFiltrados,
        'form': form,
        'form2': form2,
        'form3': form3
    }
     
    return render(request, 'principal/info_video.html', contexto)