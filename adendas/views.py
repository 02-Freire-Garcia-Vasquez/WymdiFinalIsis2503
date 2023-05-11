from django.shortcuts import render
from .forms import AdendaForm
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from .logic.logic_adenda import create_adenda, get_adendas
from django.contrib.auth.decorators import login_required
from monitoring.auth0backend import getRole

@login_required
def adenda_list(request):
    role = getRole(request)
    if role == "Enfermero" or role == "Administrador":
        adendas = get_adendas()
        context = {
            'adenda_list': adendas
        }
        return render(request, 'Adenda/adendas.html', context)
    else:
        return HttpResponse("Unauthorized User")

def adenda_create(request):
    role = getRole(request)
    if role == "Enfermero":
        if request.method == 'POST':
            form = AdendaForm(request.POST)
            if form.is_valid():
                create_adenda(form)
                messages.add_message(request, messages.SUCCESS, 'Adenda create successful')
                return HttpResponseRedirect(reverse('adendaCreate'))
            else:
                print(form.errors)
        else:
            form = AdendaForm()

        context = {
            'form': form,
        }

        return render(request, 'Adenda/adendaCreate.html', context)
    else:
        return HttpResponse("Unauthorized User")