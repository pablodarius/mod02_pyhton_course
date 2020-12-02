from django.shortcuts import render
from .forms import FormularioContanto

# Create your views here.
def contacto(request):
    formulario_contacto = FormularioContanto()
    return render(request, "contacto/contacto.html", {'miFormulario': formulario_contacto})