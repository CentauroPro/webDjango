from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=100, verbose_name="Nombre de Categoria")
    created=models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creacion")
    updated=models.DateTimeField(auto_now=True, verbose_name="Fecha de Modificación")
    
    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"
        ordering = ["-created"]
    
    def __str__(self):
        return self.name


class Blog(models.Model):
    title = models.CharField(max_length=255, verbose_name="Titulo")
    image= models.ImageField(verbose_name="Imagen",upload_to="blogs")
    content = models.TextField(verbose_name="Contenido")
    quote = models.TextField(verbose_name="Cita", default="“There are always two people in every picture: the photographer and the viewer.” - Ansel Adams")
    publicationDate = models.DateTimeField(verbose_name=" fecha de Publicacion", default=now)
    comments = models.IntegerField(verbose_name="Número de Comentarios", default=0)
    author = models.ForeignKey(User, verbose_name="Autor", on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category, verbose_name="Categorias")
    created=models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creacion")
    updated=models.DateTimeField(auto_now=True, verbose_name="Fecha de Modificación")
    
    
    class Meta:
        verbose_name = "Entrada"
        verbose_name_plural = "Entradas"
        ordering = ["title"]
        
    def __str__(self):
        return self.title