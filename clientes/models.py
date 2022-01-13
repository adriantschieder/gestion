from django.db import models
from datetime import date

class Clientes(models.Model):
    """ datos de la empresa, condicion iva, telefono, domicilio, mail y cuit
    """
    empresa = models.CharField(max_length=50,null=True,blank=True)
    condicion_iva = models.CharField(max_length=30)
    telefono = models.IntegerField(null=True,blank=True)
    domicilio = models.CharField(max_length=100)
    mail = models.EmailField(null=True,blank=True)
    cuit = models.IntegerField()

    def __str__(self): #es para que cuando lo pidamos me devuelva algo legible, en este caso el nombre
        return f'{self.empresa}'

class Maquinarias(models.Model):
    """ propietario, tipo, modelo y marca de la maquinaria
    """
    propietario = models.ForeignKey(Clientes, null= True, blank = True, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    marca = models.CharField(max_length=50)

    def __str__(self): #es para que cuando lo pidamos me devuelva algo legible, en este caso el nombre
        return f'{self.tipo}-{self.modelo}-{self.marca}'

class Arreglo_Maquinarias(models.Model):
    """ arreglos propios de una maquinaria(propietario, fecha del arreglo y el arreglo en si)
    """
    maquinaria = models.ForeignKey(Maquinarias, null= True, blank = True, on_delete=models.CASCADE)
    fecha_arreglo = models.DateField(auto_now=True)
    arreglo = models.CharField(max_length=200)

