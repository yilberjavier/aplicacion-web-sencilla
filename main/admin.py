from django.contrib import admin
from .models import Curso
from tinymce import TinyMCE
from django.db import models
# Register your models here.

class CursoAdmin(admin.ModelAdmin):
    #fields = ('curso_publicado', 'curso_titulo', 'curso_contenido')

    fieldsets = [
        ('Titulo/fecha', {'fields': [ 'curso_titulo','curso_publicado']}),
        ('contenido', {'fields':['curso_contenido']})
    ]

    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()}
    }



admin.site.register(Curso, CursoAdmin)


