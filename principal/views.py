from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from datetime import datetime
from .models import Artista, Grupos, Genero, Pais, Ciudad, Compañias
from .forms import GirlGroupForm
from django.views.decorators.csrf import csrf_protect

def inicio(request):
    # Creamos un diccionario con datos para el HTML
    contexto = {
        'fecha': datetime.now()
    }
    # Renderizamos el template pasando el contexto
    return render(request, 'principal/inicio.html', contexto)

def premios(request):
    return render(request, 'principal/premios.html')

def wiki(request):
    return render(request, 'principal/wiki.html')

def videos(request):
    girl_groups = Grupos.objects.none()
    bandas = Grupos.objects.none()
    solistas = Artista.objects.none()

    # Obtener parámetros del formulario
    es_peticion_busqueda = 'q' in request.GET or 'generos' in request.GET or 'totales' in request.GET
    query = request.GET.get('q', '')
    generos_seleccionados = request.GET.get('generos', '').split(',')
    totales_seleccionados = request.GET.get('totales', '').split(',')

    # Limpiar listas vacías
    generos_seleccionados = [g for g in generos_seleccionados if g]
    totales_seleccionados = [t for t in totales_seleccionados if t]

    # --- LÓGICA PARA GRUPOS (Girl Groups y Bandas) ---
    # Si no hay filtros de "Total" o si se seleccionó GG o BAND
    if not totales_seleccionados or 'GG' in totales_seleccionados or 'BAND' in totales_seleccionados:
        grupos_base = Grupos.objects.all()
        
        if query:
            grupos_base = grupos_base.filter(nombre__icontains=query)
        
        if generos_seleccionados:
            # Filtramos grupos que tengan relación con los géneros seleccionados en la tabla intermedia
            grupos_base = grupos_base.filter(grupos_generos__genero__nombre__in=generos_seleccionados).distinct()

        # Separamos por tipo y ordenamos
        if not totales_seleccionados or 'GG' in totales_seleccionados:
            girl_groups = grupos_base.filter(tipo='GG').order_by('nombre')
        
        if not totales_seleccionados or 'BAND' in totales_seleccionados:
            bandas = grupos_base.filter(tipo='BAND').order_by('nombre')

    # --- LÓGICA PARA ARTISTAS (Solistas) ---
    if not totales_seleccionados or 'SOLO' in totales_seleccionados: # Asumiendo 'SOLO' para Artistas
        artistas_base = Artista.objects.all()

        if query:
            artistas_base = artistas_base.filter(nombre__icontains=query)
        
        if generos_seleccionados:
            artistas_base = artistas_base.filter(artistas_generos__genero__nombre__in=generos_seleccionados).distinct()
        
        solistas = artistas_base.order_by('nombre')

    
    generos_estaticos = [
        {'id': 'K-POP', 'nombre': 'K-POP'},
        {'id': 'K-ROCK', 'nombre': 'K-ROCK'},
        {'id': 'J-POP', 'nombre': 'J-POP'},
        {'id': 'J-ROCK', 'nombre': 'J-ROCK'},
    ]
    totales_estaticos = [
        {'id': 'GG', 'nombre': 'Girl Groups'},
        {'id': 'BAND', 'nombre': 'Bandas'},
        {'id': 'SOLO', 'nombre': 'Artistas/Solistas'},
    ]
    contexto = {
        'busqueda_realizada': es_peticion_busqueda,
        'generos': generos_estaticos,
        'totales': totales_estaticos,
        'girl_groups': girl_groups,
        'bandas': bandas,
        'solistas': solistas,
        'generos_seleccionados': generos_seleccionados,
        'totales_seleccionados': totales_seleccionados,
        'query': query,
    }

    return render(request, 'principal/videos.html', contexto)

def login_view(request):
    return render(request, 'principal/login.html')

def alta_girl_group(request):
    if request.method == 'POST':
        form = GirlGroupForm(request.POST)
        if form.is_valid():
            # Forzamos el tipo GG antes de guardar por seguridad
            grupo = form.save(commit=False)
            grupo.tipo = 'GG'
            grupo.save()
            # return redirect('videos') # Redirigir a la lista tras guardar
            return render(request, 'principal/videos.html')
    else:
        # Iniciamos el formulario con el valor por defecto
        form = GirlGroupForm(initial={'tipo': 'GG'})
    
    return render(request, 'principal/alta_girl_group.html', {'form': form})

@csrf_protect
def ajax_crear_pais(request):
    if request.method == "POST":
        nombre = request.POST.get('nombre', '').strip()
        if nombre:
            try:
                # get_or_create devuelve una tupla: (objeto, creado_si_o_no)
                pais, created = Pais.objects.get_or_create(nombre=nombre)
                return JsonResponse({
                    'id': pais.id,
                    'nombre': pais.nombre
                }, status=200)
            except Exception as e:
                return JsonResponse({'error': str(e)}, status=500)
    
    return JsonResponse({'error': 'Nombre no proporcionado'}, status=400)

# views.py
def ajax_cargar_ciudades(request):
    pais_id = request.GET.get('pais_id')
    ciudades = Ciudad.objects.filter(pais_id=pais_id).order_by('nombre')
    
    # Creamos una lista de diccionarios para enviar como JSON
    lista_ciudades = [{'id': c.id, 'nombre': c.nombre} for c in ciudades]
    return JsonResponse(lista_ciudades, safe=False)

def ajax_crear_ciudad(request):
    if request.method == "POST":
        nombre = request.POST.get('nombre')
        pais_id = request.POST.get('pais_id') # Recibiremos el ID, es más seguro
        
        if nombre and pais_id:
            try:
                # Buscamos el objeto Pais por su ID
                pais_obj = Pais.objects.get(id=pais_id)
                ciudad = Ciudad.objects.create(nombre=nombre, pais=pais_obj)
                return JsonResponse({'id': ciudad.id, 'nombre': ciudad.nombre}, status=200)
            except Exception as e:
                return JsonResponse({'error': str(e)}, status=500)
                
    return JsonResponse({'error': 'Faltan datos'}, status=400)

@csrf_protect
def ajax_crear_compañia(request):
    if request.method == "POST":
        nombre = request.POST.get('nombre', '').strip()

        if nombre:
            try:
                # get_or_create devuelve una tupla: (objeto, creado_si_o_no)
                compañia, created = Compañias.objects.get_or_create(nombre=nombre)
                return JsonResponse({
                    'id': compañia.id_compañia,
                    'nombre': compañia.nombre
                }, status=200)
            except Exception as e:
                return JsonResponse({'error': str(e)}, status=500)
    
    return JsonResponse({'error': 'Nombre no proporcionado'}, status=400)