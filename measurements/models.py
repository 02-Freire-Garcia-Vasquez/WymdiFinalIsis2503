from django.db import models
from variables.models import Variable

class Measurement(models.Model):
    paciente = models.ForeignKey(Variable, on_delete=models.CASCADE, default=None)
    fechaConsulta = models.CharField(max_length=50)
    lugarConsulta = models.CharField(max_length=50)
    tipoConsulta = models.CharField(max_length=50)
    motivoConsulta = models.CharField(max_length=50)
    enfermedad = models.CharField(max_length=50)

    def __str__(self):
        return '%s %s' % (self.value, self.unit)