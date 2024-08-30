from django.shortcuts import render
from django.shortcuts import render
from .models import Contrato

def lista_contratos(request):
    contratos = Contrato.objects.select_related('cliente', 'automovil').all()
    for contrato in contratos:
        contrato.costo_total = contrato.automovil.precio + sum(car.costo for car in contrato.automovil.caracteristicas.all())
    return render(request, 'garaje/contratos.html', {'contratos': contratos})
