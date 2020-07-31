from django.db import models

#Numero de veces que se va a instanciar un nodo con otro agregandole un peso
class InstancesNumber(models.Model):
    instancesNro = models.IntegerField(max_length=2)

#Clase que maneja el nodo origen cargado
class Source(models.Model):
    source = models.CharField(max_length=2)

    def __str__(self):
        return '{}'.format(self.source)

#Clase que maneja el nodo destino cargado
class Target(models.Model):
    target = models.CharField(max_length=2)

    def __str__(self):
        return '{}'.format(self.target)

#Clase que maneja el peso de la relacion entre el nodo origen y destino cargado
class Weight(models.Model):
    weightNro = models.IntegerField(max_length=2)

    def __str__(self):
        return '{}'.format(self.weightNro)
