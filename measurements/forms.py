from django import forms
from .models import Measurement

class MeasurementForm(forms.ModelForm):
    class Meta:
        model = Measurement
        fields = [
            'paciente',
            'fechaConsulta',
            'lugarConsulta',
            'tipoConsulta',
            'motivoConsulta',
            #'enfermedad',
        ]

        labels = {
            'paciente' : 'Paciente',
            'fechaConsulta' : 'FechaConsulta',
            'lugarConsulta' : 'LugarConsulta',
            'tipoConsulta' : 'TipoConsulta',
            'motivoConsulta' : 'MotivoConsulta',
            #'enfermedad' : 'Enfermedad',
        }
