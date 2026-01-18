from django.db import models

class Genero(models.Model):
    nombre = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Género"        
        verbose_name_plural = "Géneros" 

    def __str__(self):
        return self.nombre

class Pais(models.Model):
    nombre = models.CharField(max_length=50)

    class Meta:
        verbose_name = "País"        
        verbose_name_plural = "Países" 

    def __str__(self):
        return self.nombre

class Ciudad(models.Model):
    nombre = models.CharField(max_length=100)
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = "Ciudad"        
        verbose_name_plural = "Ciudades" 
    
    def __str__(self):
        return self.nombre

class Compañias(models.Model):
    id_compañia = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    
    class Meta:
        verbose_name = "Compañía"        
        verbose_name_plural = "Compañías" 
    
    def __str__(self):
        return self.nombre

class Artista(models.Model):
    id_artista = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    nombre_nacimiento = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE)
    ciudad = models.ForeignKey(Ciudad, on_delete=models.CASCADE)
    compañia = models.ForeignKey(Compañias, on_delete=models.CASCADE, null=True, blank=True)
    mega = models.CharField(max_length=100)
    
    class Meta:
        verbose_name = "Artista"        
        verbose_name_plural = "Artistas" 
    
    def __str__(self):
        return self.nombre

class Artista_Nombres(models.Model):
    id_relacion = models.AutoField(primary_key=True)
    artista = models.ForeignKey(Artista, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    fecha_desde = models.DateField()
    fecha_hasta = models.DateField(null=True, blank=True)
    
    class Meta:
        verbose_name = "Artista_Nombres"        
        verbose_name_plural = "Artista_Nombres" 
    
    def __str__(self):
        return self.nombre

class Artista_Compañias(models.Model):
    id_relacion = models.AutoField(primary_key=True)
    artista = models.ForeignKey(Artista, on_delete=models.CASCADE)
    compañia = models.ForeignKey(Compañias, on_delete=models.CASCADE)
    fecha_desde = models.DateField()
    fecha_hasta = models.DateField(null=True, blank=True)
    
    class Meta:
        verbose_name = "Artista_Compañias"        
        verbose_name_plural = "Artista_Compañias" 
    
    def __str__(self):
        return self.artista

class Grupos(models.Model):
    TIPO_CHOICES = [
        ('GG', 'Girl Group'),
        ('BAND', 'Bandas'),
    ]

    id_grupo = models.AutoField(primary_key=True)
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES)
    nombre = models.CharField(max_length=100)
    nombre_fandom = models.CharField(max_length=100, null=True, blank=True)
    fecha_debut = models.DateField()
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE)
    compañia = models.ForeignKey(Compañias, on_delete=models.CASCADE)
    mega = models.CharField(max_length=100)
    
    class Meta:
        verbose_name = "Grupo"        
        verbose_name_plural = "Grupos" 
    
    def __str__(self):
        return self.nombre

class Grupos_Nombres(models.Model):
    id_relacion = models.AutoField(primary_key=True)
    grupo = models.ForeignKey(Grupos, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    fecha_desde = models.DateField()
    fecha_hasta = models.DateField(null=True, blank=True)
    
    class Meta:
        verbose_name = "Grupos_Nombres"        
        verbose_name_plural = "Grupos_Nombres" 
    
    def __str__(self):
        return self.nombre

class Grupos_Compañias(models.Model):
    id_relacion = models.AutoField(primary_key=True)
    grupo = models.ForeignKey(Grupos, on_delete=models.CASCADE)
    compañia = models.ForeignKey(Compañias, on_delete=models.CASCADE)
    fecha_desde = models.DateField()
    fecha_hasta = models.DateField(null=True, blank=True)
    
    class Meta:
        verbose_name = "Grupos_Compañias"        
        verbose_name_plural = "Grupos_Compañias" 
    
    def __str__(self):
        return self.grupo

class Artista_Grupos(models.Model):
    id_relacion = models.AutoField(primary_key=True)
    artista = models.ForeignKey(Artista, on_delete=models.CASCADE)
    grupo = models.ForeignKey(Grupos, on_delete=models.CASCADE)
    fecha_desde = models.DateField()
    fecha_hasta = models.DateField(null=True, blank=True)
    
    class Meta:
        verbose_name = "Artista_Grupos"        
        verbose_name_plural = "Artista_Grupos" 
    
    def __str__(self):
        return self.artista

class Secciones(models.Model):
    id_seccion = models.AutoField(primary_key=True)
    id_seccion_padre = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    orden = models.IntegerField()
    titulo = models.CharField(max_length=100)
    
    class Meta:
        verbose_name = "Sección"        
        verbose_name_plural = "Secciones" 
    
    def __str__(self):
        return self.titulo

class Videos(models.Model):
    id_video = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=100)
    youtube = models.CharField(max_length=100)
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
        verbose_name = "Videos_Grupos"        
        verbose_name_plural = "Videos_Grupos" 

class Videos_Artistas(models.Model):
    video = models.ForeignKey(Videos, on_delete=models.CASCADE)
    artista = models.ForeignKey(Artista, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = "Videos_Artistas"        
        verbose_name_plural = "Videos_Artistas" 

class Artistas_Generos(models.Model):
    artista = models.ForeignKey(Artista, on_delete=models.CASCADE, null=True, blank=True)
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE, null=True, blank=True)
    
    class Meta:
        verbose_name = "Artistas_Generos"        
        verbose_name_plural = "Artistas_Generos" 

class Grupos_Generos(models.Model):
    grupo = models.ForeignKey(Grupos, on_delete=models.CASCADE, null=True, blank=True)
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE, null=True, blank=True)
    
    class Meta:
        verbose_name = "Grupos_Generos"        
        verbose_name_plural = "Grupos_Generos" 