from django.db import models

class Cliente(models.Model):
    nombre_cliente = models.CharField(max_length=45)
    cedula_cliente = models.IntegerField()
    fecha_nacimiento = models.DateField()
    email = models.EmailField(max_length=45)
    direccion = models.CharField(max_length=45)
    telefono = models.CharField(max_length=45)

class Especializacion(models.Model):
    nombre = models.CharField(max_length=45)

class Abogado(models.Model):
    nombre_abogado = models.CharField(max_length=45)
    cedula_abogado = models.DecimalField(max_digits=10, decimal_places=0)
    especializacion = models.ForeignKey(Especializacion, on_delete=models.CASCADE)
    email = models.EmailField(max_length=45)
    direccion = models.CharField(max_length=45)
    telefono = models.CharField(max_length=45)

class Asesoria(models.Model):
    descripcion = models.CharField(max_length=200)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    id_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    id_abogado = models.ForeignKey(Abogado, on_delete=models.CASCADE)

class TipoProceso(models.Model):
    descripcion = models.CharField(max_length=45)

class Proceso(models.Model):
    doc_online = models.CharField(max_length=45)
    doc_fisico = models.CharField(max_length=45)
    id_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    id_abogado = models.ForeignKey(Abogado, on_delete=models.CASCADE)
    tipo_proceso = models.ForeignKey(TipoProceso, on_delete=models.CASCADE)

class Audiencia(models.Model):
    lugar = models.CharField(max_length=45)
    fecha_hora = models.DateTimeField()
    id_proceso = models.ForeignKey(Proceso, on_delete=models.CASCADE)

class TipoContabilidad(models.Model):
    descripcion = models.CharField(max_length=50)

class ContabilidadOficina(models.Model):
    tipo_contabilidad = models.ForeignKey(TipoContabilidad, on_delete=models.CASCADE)
    id_abogado = models.ForeignKey(Abogado, on_delete=models.CASCADE)
    valor = models.DecimalField(max_digits=10, decimal_places=2)

class ContabilidadProcesos(models.Model):
    tipo_contabilidad = models.ForeignKey(TipoContabilidad, on_delete=models.CASCADE)
    id_proceso = models.ForeignKey(Proceso, on_delete=models.CASCADE)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
