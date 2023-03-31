from ..models import Measurement

def get_measurements():
    queryset = Measurement.objects.all().order_by('paciente')
    return (queryset)

def create_measurement(form):
    measurement = form.save()
    measurement.save()
    return ()

def create_measurement_object(variable_id, fecha, lugar, tipo,motivo):
    measurement = Measurement()
    measurement.paciente = variable_id
    measurement.fechaConsulta = fecha
    measurement.lugarConsulta = lugar
    measurement.tipoConsulta = tipo
    measurement.motivoConsulta = motivo
    measurement.save()
    return ()