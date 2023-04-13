from django.contrib import admin
from .models import Project

# Register your models here.
class ProjectAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated') # también visualizar estos campos (sólo lectura)

admin.site.register(Project, ProjectAdmin)