from django.db import models

# Create your models here.
class Project(models.Model):
    image=models.ImageField(verbose_name="Imagen", upload_to="project")
    created=models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")
    updated=models.DateTimeField(auto_now=True, verbose_name="Fecha de Modificacion")
    
    
    class Meta:
        verbose_name="GRID"
        verbose_name_plural="GRIS"
        ordering=["-created"]
        
    def __str__(self):
        return self.image.name  
