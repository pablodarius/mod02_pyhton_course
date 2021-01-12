from django.shortcuts import render, redirect
from .forms import FormularioContanto

# Create your views here.
def contacto(request):
    formulario_contacto = FormularioContanto()
    if request.method == "POST":
        formulario_contacto = FormularioContanto(data=request.POST)
        if formulario_contacto.is_valid():
            nombre = request.POST.get("nombre")
            email = request.POST.get("email")
            contenido = request.POST.get("contenido")
            return redirect("/contacto/?valido")

    return render(request, "contacto/contacto.html", {'miFormulario': formulario_contacto})