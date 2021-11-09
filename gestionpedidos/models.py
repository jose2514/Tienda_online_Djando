#siempre que se realicen cambios en models 
#se tiene que ejectar en el cmd "python manage.py makemigrations"
#se tiene que ejectar en el cmd "python manage.py migrate"
from django.db import models

# Create your models here.

class Clientes(models.Model):
    nombre=models.CharField(max_length=30)
    direccion=models.CharField(max_length=50, verbose_name="esta es la direccion")#verbose_name  cambia el nombre
    email=models.EmailField(blank=True, null=True)#blank = hace que sea obligatorio  la respuesta
    telefono=models.CharField(max_length=7)
    def __str__(self):
        return (self.nombre)
class articulos(models.Model):
    nombre=models.CharField(max_length=30)
    seccion=models.CharField(max_length=20)
    precio=models.IntegerField()

    def __str__(self):
        return "el nombre es %s la seccion es %s y el precio es %s" %(self.nombre, self.seccion, self.precio)
class pedidos(models.Model):
    numero=models.IntegerField()
    fecha=models.DateField()
    entregado=models.BooleanField()

    