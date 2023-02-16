from django.contrib import admin
from.models import Categoria, Producto

# Register your models here.

class CategoriaAdmin(admin.ModelAdmin):
    readonly_fields=("created","updated")                   #es para que los pueda mostrar en pantalla en mi panel de administración

class PostaAdmin(admin.ModelAdmin):
    readonly_fields=("created","updated")

admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Producto, PostaAdmin)