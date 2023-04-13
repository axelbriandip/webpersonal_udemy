from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    img = models.ImageField()
    created = models.DateTimeField(auto_now_add=True) # solo se crea una vez
    updated = models.DateTimeField(auto_now=True) # se va actualizando