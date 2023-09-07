from django.db import models

# Create your models here.
class Project(models.Model):
    image=models.ImageField(verbose_name="Imagen", upload_to="project")
    title=models.CharField(max_length=100, verbose_name="Titulo")
    created=models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")
    updated=models.DateTimeField(auto_now=True, verbose_name="Fecha de Modificacion")
    
    
    class Meta:
        verbose_name="Creacion"
        verbose_name_plural="Creaciones"
        ordering=["-created"]
        
    def __str__(self):
        return self.title    
