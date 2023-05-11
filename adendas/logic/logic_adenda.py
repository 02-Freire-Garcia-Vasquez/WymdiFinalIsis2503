from ..models import Adenda

def get_adendas():
    queryset = Adenda.objects.all().order_by('paciente')
    return (queryset)

def create_adenda(form):
    measurement = form.save()
    measurement.save()
    return ()

def create_adenda_object(variable_id, fecha, lugar, tipo,motivo,enfer):
    measurement = Adenda()
    measurement.paciente = variable_id
    measurement.fechaConsulta = fecha
    measurement.lugarConsulta = lugar
    measurement.tipoConsulta = tipo
    measurement.motivoConsulta = motivo
    measurement.enfermedad = enfer
    measurement.save()
    return ()