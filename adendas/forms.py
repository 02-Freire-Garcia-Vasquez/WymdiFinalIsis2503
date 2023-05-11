from django import forms
from .models import Adenda

class AdendaForm(forms.ModelForm):
    class Meta:
        model = Adenda
        fields = [
            'paciente',
            'fechaConsulta',
            'lugarConsulta',
            'tipoConsulta',
            'motivoConsulta',
            'enfermedad',
        ]

        labels = {
            'paciente' : 'Paciente',
            'fechaConsulta' : 'FechaConsulta',
            'lugarConsulta' : 'LugarConsulta',
            'tipoConsulta' : 'TipoConsulta',
            'motivoConsulta' : 'MotivoConsulta',
            'enfermedad' : 'Enfermedad',
        }
