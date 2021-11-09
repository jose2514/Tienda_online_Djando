from django.contrib import admin
from gestionpedidos.models import Clientes,articulos,pedidos
# Register your models here.
class ClientesAdmin(admin.ModelAdmin):
    list_display=("nombre","telefono")#pone nomres y telefonos 
    search_fields=("nombre","telefono")#pones busqueda por nombre y telefonos
class articulosAdmin(admin.ModelAdmin):
    list_filter=("seccion",)#filtrar por seccion 
class pedidosAdmin(admin.ModelAdmin):
    list_display=("numero","fecha")
    list_filter=("fecha",)
    date_hierarchy="fecha"
admin.site.register(Clientes,ClientesAdmin)
admin.site.register(articulos,articulosAdmin)
admin.site.register(pedidos,pedidosAdmin)