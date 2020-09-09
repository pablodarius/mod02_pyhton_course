from django.contrib import admin
from .models import Markets, Products

# Register your models here.
class MarketsAdmin(admin.ModelAdmin):
    readonly_fields = ("created", "updated")

class ProductsAdmin(admin.ModelAdmin):
    readonly_fields = ("created", "updated")



admin.site.register(Markets, MarketsAdmin)
admin.site.register(Products, ProductsAdmin)

