from django.shortcuts import render
from .models import MiInformacion  # Asegúrate de que esto esté importado

#Descomentar las comillas para que se pueda ver la informacion
def index(request):
    participante = {
        'nombre': 'Diego Alberto Martinez Hernandez',
        'fecha_nacimiento': '1998-04-14',
        'direccion': '16 de septiembre',
        'telefono': '233-119-2357',
        'email': 'martinez.hdz.diegoa@gmail.com',
        'sexo': 'Masculino'
    } 
    #participante = MiInformacion.objects.first() #Esta linea seria para obtener lo primero que tenga el modelo desde la BD
    return render(request, 'participante/index.html', {'participante': participante})
