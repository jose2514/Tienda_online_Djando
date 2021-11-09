from django.shortcuts import render
from django.http import HttpResponse
from gestionpedidos.models import articulos
from django.core.mail import send_mail
from django.conf import settings
from gestionpedidos.forms import formulariocontacto
# Create your views here.
def busqueda_productos(request):
    return render(request, "busqueda_productos.html")
def buscar(request):
    if request.GET["producto"]:
        #mensaje="articulo buscado:%r" %request.GET["producto"]
        guardar_producto=request.GET["producto"]
        if len(guardar_producto)>20:
            mensaje="texto con muchos caracteres:"
        else:
            articulos2=articulos.objects.filter(nombre__icontains=guardar_producto)
            return render(request, "resultado_busqueda.html",{"articulos2":articulos2, "query":guardar_producto})
    else:
        mensaje="no a introducido articulo:"
    return HttpResponse(mensaje)    

# def contacto(request):
#     if request.method=="POST":
#         subject=request.POST["asunto"]
#         message=request.POST["mensaje"] + " " + request.POST["email"]
#         email_from=settings.EMAIL_HOST_USER
#         recipient_list=["branndonloaiza@gmail.com"]
#         #recipient_list=["jose.parra.curtidor@unillanos.edu.co"]
#         send_mail(subject, message, email_from, recipient_list)

#         return render(request,"gracias.html")
#     return render(request,"contacto.html")

def contacto(request):
    if request.method=="POST":
        miformulario=formulariocontacto(request.POST)
        if miformulario.is_valid():
            infform=miformulario.cleaned_data
            send_mail(infform["asunto"], infform["mensaje"], 
            infform.get("email",""),["jose.parra.curtidor@unillanos.edu.co"],)
            return render(request,"gracias.html")
    
    else:
        miformulario=formulariocontacto()
    return render(request,"formulario_contacto.html",{"form":miformulario})