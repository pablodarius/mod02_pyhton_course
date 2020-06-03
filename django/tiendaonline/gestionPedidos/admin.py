from django.contrib import admin
from gestionPedidos.models import clientes, articulos, pedidos

# Register your models here.

class ClientesAdmin(admin.ModelAdmin):
    list_display=("nombre", "email")
    search_fields=("nombre", "email")
    list_filter=("nombre",)

class ArticulosAdmin(admin.ModelAdmin):
    list_display=("nombre", "seccion")
    list_filter=("seccion",)

class PedidosAdmin(admin.ModelAdmin):
    list_display=("numero", "fecha")
    list_filter=("fecha",)
    date_hierarchy="fecha"

admin.site.register(clientes, ClientesAdmin)
admin.site.register(articulos, ArticulosAdmin)
admin.site.register(pedidos, PedidosAdmin)
