from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.db.models.signals import post_save


class Especializacion(models.Model):
    nombre = models.CharField(max_length=45)

    def __str__(self):
        return self.nombre

class Cliente(models.Model):
    nombre_cliente = models.CharField(max_length=45)
    cedula_cliente = models.IntegerField()
    fecha_nacimiento = models.DateField()
    email = models.EmailField(max_length=45)
    direccion = models.CharField(max_length=45)
    telefono = models.CharField(max_length=45)

    def __str__(self):
        return self.nombre_cliente

class Abogado(models.Model):
    nombre_abogado = models.CharField(max_length=45)
    cedula_abogado = models.FloatField()
    especializacion = models.ForeignKey(Especializacion, on_delete=models.CASCADE)
    email = models.EmailField(max_length=45)
    direccion = models.CharField(max_length=45)
    telefono = models.CharField(max_length=45)

    def __str__(self):
        return self.nombre_abogado

class TipoProceso(models.Model):
    descripcion = models.CharField(max_length=45)

    def __str__(self):
        return self.descripcion

class Proceso(models.Model):
    doc_online = models.CharField(max_length=45)
    doc_fisico = models.CharField(max_length=45)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    abogado = models.ForeignKey(Abogado, on_delete=models.CASCADE)
    tipo_proceso = models.ForeignKey(TipoProceso, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.cliente} - {self.abogado} - {self.tipo_proceso}"

class Audiencia(models.Model):
    lugar = models.CharField(max_length=45)
    fecha_hora = models.DateTimeField()
    proceso = models.ForeignKey(Proceso, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.lugar} - {self.fecha_hora}"

class TipoContabilidad(models.Model):
    descripcion = models.CharField(max_length=50)

    def __str__(self):
        return self.descripcion

class ContabilidadOficina(models.Model):
    tipo_contabilidad = models.ForeignKey(TipoContabilidad, on_delete=models.CASCADE)
    abogado = models.ForeignKey(Abogado, on_delete=models.CASCADE)
    valor = models.FloatField()

    def __str__(self):
        return f"{self.tipo_contabilidad} - {self.valor}"

class ContabilidadProceso(models.Model):
    tipo_contabilidad = models.ForeignKey(TipoContabilidad, on_delete=models.CASCADE)
    proceso = models.ForeignKey(Proceso, on_delete=models.CASCADE)
    valor = models.FloatField()

    def __str__(self):
        return f"{self.tipo_contabilidad} - {self.valor}"

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_abogado = models.BooleanField(default=False)
    is_cliente = models.BooleanField(default=False)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()