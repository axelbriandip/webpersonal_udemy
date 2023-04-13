from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200, verbose_name = 'Título')
    description = models.TextField(verbose_name = 'Descripción')
    img = models.ImageField(verbose_name = 'Imágen', upload_to='media/projects')
    URLField = models.URLField(null = True, blank = True, verbose_name='Link')
    created = models.DateTimeField(auto_now_add=True, verbose_name = 'Creación') # solo se crea una vez
    updated = models.DateTimeField(auto_now=True, verbose_name = 'Última edición') # se va actualizando

    class Meta:
        verbose_name = 'Proyecto'
        verbose_name_plural = 'Proyectos'
        ordering = ['-created'] # ordenar por..
    
    def __str__(self):
        return self.title # para que se listen con los títulos