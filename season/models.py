from django.db import models

class Season(models.Model):
    key = models.SlugField(verbose_name="Nombre clave", max_length=50, unique=True)
    name = models.CharField(verbose_name="Temporada", max_length=50)
    url = models.URLField(verbose_name="Acceder", null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de Modificación")
    
    class Meta:
        verbose_name = "Temporada"
        verbose_name_plural = "Temporadas"
        ordering = ["name"]
        
    def __str__(self):
        return self.name
