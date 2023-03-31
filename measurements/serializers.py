from rest_framework import serializers
from . import models


class MeasurementSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'paciente', 'fechaConsulta', 'lugarConsulta', 'tipoConsulta', 'motivoConsulta')
        model = models.Measurement