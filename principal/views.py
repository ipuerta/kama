from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models.functions import Lower
from datetime import datetime
from .models import Paises, Ciudades, Grupos, Artistas, Artistas_Grupos
from .forms import AltaGrupoForm, ModGrupoForm, AltaArtistaForm, ModArtistaForm, AltaRelacion, AltaCiudad, AltaPais
from django.views.decorators.csrf import csrf_protect

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
            form.save()
            return render(request, 'principal/inicio.html', contexto)
    else:
        form = AltaGrupoForm()
        contexto = {
            'paises': paises,
            'form': form
        }
     
    return render(request, 'principal/alta_grupo.html', contexto)

def info_grupo(request, id):
    grupo = get_object_or_404(Grupos, id=id)
    hijos = grupo.hijos.all()
    relaciones = Artistas_Grupos.objects.filter(grupo=id)

    if request.method == 'POST':
        form = ModGrupoForm(request.POST, instance=grupo)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)

    paises = Paises.objects.all().order_by(Lower('nombre'))
    grupo = get_object_or_404(Grupos, id=id)
    form = ModGrupoForm(instance=grupo)

    contexto = {
        'paises': paises,
        'grupo': grupo,
        'hijos': hijos,
        'relaciones': relaciones,
        'form': form
    }
     
    return render(request, 'principal/info_grupo.html', contexto)

def artistas(request):
    paises = Paises.objects.all().order_by(Lower('nombre'))
    artistas = Artistas.objects.all().order_by(Lower('nombre'))

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
            form.save()
            return render(request, 'principal/inicio.html', contexto)
    else:
        form = AltaArtistaForm()
        contexto = {
            'paises': paises,
            'form': form
        }
     
    return render(request, 'principal/alta_artista.html', contexto)

def info_artista(request, id):
    artista = get_object_or_404(Artistas, id=id)
    relaciones = Artistas_Grupos.objects.filter(artista=id)

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

    paises = Paises.objects.all().order_by(Lower('nombre'))
    artista = get_object_or_404(Artistas, id=id)
    relaciones = Artistas_Grupos.objects.filter(artista=id)
    form = ModArtistaForm(instance=artista)
    form2 = AltaRelacion(initial={'artista' : artista})

    contexto = {
        'paises': paises,
        'artista': artista,
        'relaciones': relaciones,
        'form': form,
        'form2': form2
    }
     
    return render(request, 'principal/info_artista.html', contexto)

def info_pais(request, id):
    paises = Paises.objects.all().order_by(Lower('nombre'))
    pais = get_object_or_404(Paises, id=id)
    ciudades = Ciudades.objects.filter(pais=id).order_by(Lower('nombre'))
    grupos = Grupos.objects.filter(pais=id).order_by(Lower('nombre'))

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
            form.save()
            return render(request, 'principal/inicio.html', contexto)
    else:
        form = AltaPais()
        contexto = {
            'paises': paises,
            'form': form
        }
     
    return render(request, 'principal/alta_pais.html', contexto)


#def videos(request):
#    girl_groups = Grupos.objects.none()
#    bandas = Grupos.objects.none()
#    solistas = Artista.objects.none()

#    # Obtener parámetros del formulario
#    es_peticion_busqueda = 'q' in request.GET or 'generos' in request.GET or 'totales' in request.GET
#    query = request.GET.get('q', '')
#    generos_seleccionados = request.GET.get('generos', '').split(',')
#    totales_seleccionados = request.GET.get('totales', '').split(',')

#    # Limpiar listas vacías
#    generos_seleccionados = [g for g in generos_seleccionados if g]
#    totales_seleccionados = [t for t in totales_seleccionados if t]

#    # --- LÓGICA PARA GRUPOS (Girl Groups y Bandas) ---
#    # Si no hay filtros de "Total" o si se seleccionó GG o BAND
#    if not totales_seleccionados or 'GG' in totales_seleccionados or 'BAND' in totales_seleccionados:
#        grupos_base = Grupos.objects.all()
        
#        if query:
#            grupos_base = grupos_base.filter(nombre__icontains=query)
        
#        if generos_seleccionados:
#            # Filtramos grupos que tengan relación con los géneros seleccionados en la tabla intermedia
#            grupos_base = grupos_base.filter(grupos_generos__genero__nombre__in=generos_seleccionados).distinct()

#        # Separamos por tipo y ordenamos
#        if not totales_seleccionados or 'GG' in totales_seleccionados:
#            girl_groups = grupos_base.filter(tipo='GG').order_by(Lower('nombre'))
        
#        if not totales_seleccionados or 'BAND' in totales_seleccionados:
#            bandas = grupos_base.filter(tipo='BAND').order_by(Lower('nombre'))

#    # --- LÓGICA PARA ARTISTAS (Solistas) ---
#    if not totales_seleccionados or 'SOLO' in totales_seleccionados: # Asumiendo 'SOLO' para Artistas
#        artistas_base = Artista.objects.all()

#        if query:
#            artistas_base = artistas_base.filter(nombre__icontains=query)
        
#        if generos_seleccionados:
#            artistas_base = artistas_base.filter(artistas_generos__genero__nombre__in=generos_seleccionados).distinct()
        
#        solistas = artistas_base.order_by(Lower('nombre'))

    
#    generos_estaticos = [
#        {'id': 'K-POP', 'nombre': 'K-POP'},
#        {'id': 'K-ROCK', 'nombre': 'K-ROCK'},
#        {'id': 'J-POP', 'nombre': 'J-POP'},
#        {'id': 'J-ROCK', 'nombre': 'J-ROCK'},
#    ]
#    totales_estaticos = [
#        {'id': 'GG', 'nombre': 'Girl Groups'},
#        {'id': 'BAND', 'nombre': 'Bandas'},
#        {'id': 'SOLO', 'nombre': 'Artistas/Solistas'},
#    ]
#    contexto = {
#        'busqueda_realizada': es_peticion_busqueda,
#        'generos': generos_estaticos,
#        'totales': totales_estaticos,
#        'girl_groups': girl_groups,
#        'bandas': bandas,
#        'solistas': solistas,
#        'generos_seleccionados': generos_seleccionados,
#        'totales_seleccionados': totales_seleccionados,
#        'query': query,
#    }

#    return render(request, 'principal/videos.html', contexto)

#def alta_girl_group(request):
#    if request.method == 'POST':
#        form = GirlGroupForm(request.POST)
#        if form.is_valid():
#            # Forzamos el tipo GG antes de guardar por seguridad
#            grupo = form.save(commit=False)
#            grupo.tipo = 'GG'
#            grupo.save()

#            next_url = request.POST.get('next') or request.META.get('HTTP_REFERER')
#            if next_url:
#                return redirect(next_url)
#            return redirect('videos') # Redirigir a la lista tras guardar
#            # return render(request, 'principal/videos.html')
#    else:
#        # Iniciamos el formulario con el valor por defecto
#        form = GirlGroupForm(initial={'tipo': 'GG'})

#    next_url = request.GET.get('next', '')
#    return render(request, 'principal/alta_girl_group.html', {'form': form, 'next_url': next_url})

#def alta_banda(request):
#    if request.method == 'POST':
#        form = BandaForm(request.POST)
#        if form.is_valid():
#            # Forzamos el tipo BAND antes de guardar por seguridad
#            grupo = form.save(commit=False)
#            grupo.tipo = 'BAND'
#            grupo.save()

#            next_url = request.POST.get('next') or request.META.get('HTTP_REFERER')
#            if next_url:
#                return redirect(next_url)
#            return redirect('videos') # Redirigir a la lista tras guardar
#            # return render(request, 'principal/videos.html')
#    else:
#        # Iniciamos el formulario con el valor por defecto
#        form = GirlGroupForm(initial={'tipo': 'BAND'})

#    next_url = request.GET.get('next', '')
#    return render(request, 'principal/alta_girl_group.html', {'form': form, 'next_url': next_url})

#def alta_artista(request):
#    if request.method == 'POST':
#        form = ArtistaForm(request.POST)
#        if form.is_valid():
#            grupo = form.save(commit=False)
#            grupo.save()

#            next_url = request.POST.get('next') or request.META.get('HTTP_REFERER')
#            if next_url:
#                return redirect(next_url)
#            return redirect('videos') # Redirigir a la lista tras guardar
#            # return render(request, 'principal/videos.html')
#    else:
#        # Iniciamos el formulario con el valor por defecto
#        form = ArtistaForm()

#    next_url = request.GET.get('next', '')
#    return render(request, 'principal/alta_artista.html', {'form': form, 'next_url': next_url})

#@csrf_protect
#def ajax_crear_pais(request):
#    if request.method == "POST":
#        nombre = request.POST.get('nombre', '').strip()
#        if nombre:
#            try:
#                # get_or_create devuelve una tupla: (objeto, creado_si_o_no)
#                pais, created = Pais.objects.get_or_create(nombre=nombre)
#                return JsonResponse({
#                    'id': pais.id,
#                    'nombre': pais.nombre
#                }, status=200)
#            except Exception as e:
#                return JsonResponse({'error': str(e)}, status=500)
    
#    return JsonResponse({'error': 'Nombre no proporcionado'}, status=400)

## views.py
#def ajax_cargar_ciudades(request):
#    pais_id = request.GET.get('pais_id')
#    ciudades = Ciudad.objects.filter(pais_id=pais_id).order_by('nombre')
    
#    # Creamos una lista de diccionarios para enviar como JSON
#    lista_ciudades = [{'id': c.id, 'nombre': c.nombre} for c in ciudades]
#    return JsonResponse(lista_ciudades, safe=False)

#def ajax_crear_ciudad(request):
#    if request.method == "POST":
#        nombre = request.POST.get('nombre')
#        pais_id = request.POST.get('pais_id') # Recibiremos el ID, es más seguro
        
#        if nombre and pais_id:
#            try:
#                # Buscamos el objeto Pais por su ID
#                pais_obj = Pais.objects.get(id=pais_id)
#                ciudad = Ciudad.objects.create(nombre=nombre, pais=pais_obj)
#                return JsonResponse({'id': ciudad.id, 'nombre': ciudad.nombre}, status=200)
#            except Exception as e:
#                return JsonResponse({'error': str(e)}, status=500)
                
#    return JsonResponse({'error': 'Faltan datos'}, status=400)

#@csrf_protect
#def ajax_crear_compañia(request):
#    if request.method == "POST":
#        nombre = request.POST.get('nombre', '').strip()

#        if nombre:
#            try:
#                # get_or_create devuelve una tupla: (objeto, creado_si_o_no)
#                compañia, created = Compañias.objects.get_or_create(nombre=nombre)
#                return JsonResponse({
#                    'id': compañia.id_compañia,
#                    'nombre': compañia.nombre
#                }, status=200)
#            except Exception as e:
#                return JsonResponse({'error': str(e)}, status=500)
    
#    return JsonResponse({'error': 'Nombre no proporcionado'}, status=400)

#def detalle_grupo(request, id_grupo):
#    # Buscar el grupo
#    grupo = get_object_or_404(Grupos, id_grupo=id_grupo)

#    return render(request, 'principal/detalle_grupo.html', {
#        'grupo': grupo
#        })