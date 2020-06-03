from django.shortcuts import render
from django.http import HttpResponse
from gestionPedidos.models import articulos
from django.core.mail import send_mail
from django.conf import settings
from gestionPedidos.forms import FormularioContacto

# Create your views here.
def busquedaProductos(request):
    return render(request, "busqueda_productos.html")

def buscar(request):
    if request.GET["prd"]:
        # mensaje = "Artículo bu scado: %r" %request.GET["prd"]
        producto = request.GET["prd"]
        if len(producto) > 20:
            mensaje = "Texto demasiado largo"
        else:
            artc = articulos.objects.filter(nombre__icontains=producto)
            return render(request, "resultados_busqueda.html", {"articulos": artc, "query": producto})
    else:
        mensaje = "No hay nada para buscar"    

    return HttpResponse(mensaje)

def contacto(request):
    if request.method=="POST":
        miFormulario = FormularioContacto(request.POST)

        if miFormulario.is_valid():
            infoForm = miFormulario.cleaned_data
            send_mail(infoForm['asunto'], infoForm['mensaje'], infoForm.get('email', 'pablopantoja1985@gmail.com'), ['pablopantoja1985@gmail.com'],)
            return render(request, "gracias.html")
            
    else:
        miFormulario = FormularioContacto()

    return  render(request, "form_contacto.html", {"form": miFormulario})



    """
    if request.method=="POST":
        subject = request.POST["asunto"]
        message = request.POST["mensaje"] + " " + request.POST["email"]
        email_from = settings.EMAIL_HOST_USER
        recipient_list = ["pablopantoja1985@gmail.com"]

        send_mail(subject, message, email_from, recipient_list)

        return render(request, "gracias.html")

    return  render(request, "contacto.html")
    """