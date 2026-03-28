from django.db import models

class Paises(models.Model):
    nombre = models.CharField(max_length=50)

    class Meta:
        verbose_name = "País"        
        verbose_name_plural = "Países" 

    def __str__(self):
        return self.nombre

class Ciudades(models.Model):
    nombre = models.CharField(max_length=100)
    pais = models.ForeignKey(Paises, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = "Ciudad"        
        verbose_name_plural = "Ciudades" 
    
    def __str__(self):
        return self.nombre

class Compañias(models.Model):
    nombre = models.CharField(max_length=100)
    padre = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    pais = models.ForeignKey(Paises, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = "Compañía"        
        verbose_name_plural = "Compañías" 
    
    def __str__(self):
        return self.nombre


class Artistas(models.Model):
    nombre = models.CharField(max_length=100)
    nombre_coreano = models.CharField(max_length=100, null=True, blank=True)
    nombre_japones = models.CharField(max_length=100, null=True, blank=True)
    nombre_chino = models.CharField(max_length=100, null=True, blank=True)
    nombre_tailandes = models.CharField(max_length=100, null=True, blank=True)
    fecha_nacimiento = models.DateField()
    pais = models.ForeignKey(Paises, on_delete=models.CASCADE)
    ciudad = models.ForeignKey(Ciudades, on_delete=models.CASCADE)
    enlace = models.CharField(max_length=100)
    
    class Meta:
        verbose_name = "Artista"        
        verbose_name_plural = "Artistas" 
    
    def __str__(self):
        return self.nombre

class Artistas_Nombres(models.Model):
    artista = models.ForeignKey(Artistas, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    fecha_desde = models.DateField()
    fecha_hasta = models.DateField(null=True, blank=True)
    
    class Meta:
        verbose_name = "Artista_Nombre"        
        verbose_name_plural = "Artistas_Nombres" 
    
    def __str__(self):
        return self.nombre

class Artistas_Compañias(models.Model):
    artista = models.ForeignKey(Artistas, on_delete=models.CASCADE)
    compañia = models.ForeignKey(Compañias, on_delete=models.CASCADE)
    fecha_desde = models.DateField()
    fecha_hasta = models.DateField(null=True, blank=True)
    
    class Meta:
        verbose_name = "Artista_Compañia"        
        verbose_name_plural = "Artistas_Compañias" 
    
    def __str__(self):
        return self.artista

class Grupos(models.Model):
    nombre = models.CharField(max_length=100)
    nombre_coreano = models.CharField(max_length=100, null=True, blank=True)
    padre = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='hijos')
    nombre_fandom = models.CharField(max_length=100, null=True, blank=True)
    fecha_debut = models.DateField()
    pais = models.ForeignKey(Paises, on_delete=models.CASCADE)
    enlace = models.CharField(max_length=100)
    
    class Meta:
        verbose_name = "Grupo"        
        verbose_name_plural = "Grupos" 
    
    def __str__(self):
        return self.nombre

class Grupos_Nombres(models.Model):
    grupo = models.ForeignKey(Grupos, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    fecha_desde = models.DateField()
    fecha_hasta = models.DateField(null=True, blank=True)
    
    class Meta:
        verbose_name = "Grupo_Nombre"        
        verbose_name_plural = "Grupos_Nombres" 
    
    def __str__(self):
        return self.nombre

class Grupos_Compañias(models.Model):
    grupo = models.ForeignKey(Grupos, on_delete=models.CASCADE)
    compañia = models.ForeignKey(Compañias, on_delete=models.CASCADE)
    fecha_desde = models.DateField()
    fecha_hasta = models.DateField(null=True, blank=True)
    
    class Meta:
        verbose_name = "Grupo_Compañia"        
        verbose_name_plural = "Grupos_Compañias" 
    
    def __str__(self):
        return self.grupo

class Artistas_Grupos(models.Model):
    artista = models.ForeignKey(Artistas, on_delete=models.CASCADE)
    grupo = models.ForeignKey(Grupos, on_delete=models.CASCADE)
    fecha_desde = models.DateField()
    fecha_hasta = models.DateField(null=True, blank=True)
    
    class Meta:
        verbose_name = "Artista_Grupo"        
        verbose_name_plural = "Artistas_Grupos" 
    
    def __str__(self):
        return self.artista.nombre

class Secciones(models.Model):
    nombre = models.CharField(max_length=100)
    padre = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    orden = models.IntegerField()
    seleccionable = models.CharField(max_length=1)
    
    class Meta:
        verbose_name = "Sección"        
        verbose_name_plural = "Secciones" 
    
    def __str__(self):
        return self.titulo

class Videos(models.Model):
    nombre = models.CharField(max_length=100)
    enlace = models.CharField(max_length=100)
    fecha = models.DateField()
    seccion = models.ForeignKey(Secciones, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = "Video"        
        verbose_name_plural = "Videos" 
    
    def __str__(self):
        return self.titulo

class Videos_Grupos(models.Model):
    video = models.ForeignKey(Videos, on_delete=models.CASCADE)
    grupo = models.ForeignKey(Grupos, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = "Video_Grupo"        
        verbose_name_plural = "Videos_Grupos" 

class Videos_Artistas(models.Model):
    video = models.ForeignKey(Videos, on_delete=models.CASCADE)
    artista = models.ForeignKey(Artistas, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = "Video_Artista"        
        verbose_name_plural = "Videos_Artistas" 