from tabnanny import verbose
from django.db import models

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=150, verbose_name="Título")
    description = models.TextField(verbose_name="Descripción")
    image = models.ImageField(verbose_name="Imagen", upload_to="projects")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateField(auto_now=True, verbose_name="Fecha de edición")
    link = models.URLField(null=True, blank=True, verbose_name="Dirección")

    class Meta:
        verbose_name = "proyecto"
        verbose_name_plural = "proyectos"
        ordering = ["-created"]

    def __str__(self):
        return self.title