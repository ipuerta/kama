from django.db import models

class Genero(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Pais(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Ciudad(models.Model):
    nombre = models.CharField(max_length=100)
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombre

class Compañias(models.Model):
    id_compañia = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    
    def __str__(self):
        return self.id_compañia

class Artista(models.Model):
    id_artista = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    nombre_nacimiento = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE)
    ciudad = models.ForeignKey(Ciudad, on_delete=models.CASCADE)
    compañia = models.ForeignKey(Compañias, on_delete=models.CASCADE, null=True, blank=True)
    mega = models.CharField(max_length=100)
    
    def __str__(self):
        return self.id_artista

class Artista_Nombres(models.Model):
    id_relacion = models.AutoField(primary_key=True)
    artista = models.ForeignKey(Artista, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    fecha_desde = models.DateField()
    fecha_hasta = models.DateField(null=True, blank=True)
    
    def __str__(self):
        return self.id_relacion

class Artista_Compañias(models.Model):
    id_relacion = models.AutoField(primary_key=True)
    artista = models.ForeignKey(Artista, on_delete=models.CASCADE)
    compañia = models.ForeignKey(Compañias, on_delete=models.CASCADE)
    fecha_desde = models.DateField()
    fecha_hasta = models.DateField(null=True, blank=True)
    
    def __str__(self):
        return self.id_relacion

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
    ciudad = models.ForeignKey(Ciudad, on_delete=models.CASCADE)
    compañia = models.ForeignKey(Compañias, on_delete=models.CASCADE)
    mega = models.CharField(max_length=100)
    
    def __str__(self):
        return self.id_grupo

class Grupos_Nombres(models.Model):
    id_relacion = models.AutoField(primary_key=True)
    grupo = models.ForeignKey(Grupos, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    fecha_desde = models.DateField()
    fecha_hasta = models.DateField(null=True, blank=True)
    
    def __str__(self):
        return self.id_relacion

class Grupos_Compañias(models.Model):
    id_relacion = models.AutoField(primary_key=True)
    grupo = models.ForeignKey(Grupos, on_delete=models.CASCADE)
    compañia = models.ForeignKey(Compañias, on_delete=models.CASCADE)
    fecha_desde = models.DateField()
    fecha_hasta = models.DateField(null=True, blank=True)
    
    def __str__(self):
        return self.id_relacion

class Artista_Grupos(models.Model):
    id_relacion = models.AutoField(primary_key=True)
    artista = models.ForeignKey(Artista, on_delete=models.CASCADE)
    grupo = models.ForeignKey(Grupos, on_delete=models.CASCADE)
    fecha_desde = models.DateField()
    fecha_hasta = models.DateField(null=True, blank=True)
    
    def __str__(self):
        return self.id_relacion

class Secciones(models.Model):
    id_seccion = models.AutoField(primary_key=True)
    id_seccion_padre = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    orden = models.IntegerField()
    titulo = models.CharField(max_length=100)
    
    def __str__(self):
        return self.id_seccion

class Videos(models.Model):
    id_video = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=100)
    youtube = models.CharField(max_length=100)
    fecha = models.DateField()
    grupo = models.ForeignKey(Grupos, on_delete=models.CASCADE, null=True, blank=True)
    artista = models.ForeignKey(Artista, on_delete=models.CASCADE, null=True, blank=True)
    seccion = models.ForeignKey(Secciones, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.id_seccion

class Artistas_Generos(models.Model):
    artista = models.ForeignKey(Artista, on_delete=models.CASCADE, null=True, blank=True)
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE, null=True, blank=True)

class Grupos_Generos(models.Model):
    grupo = models.ForeignKey(Grupos, on_delete=models.CASCADE, null=True, blank=True)
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE, null=True, blank=True)