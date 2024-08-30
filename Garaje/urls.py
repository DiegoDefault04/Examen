from django.urls import path
from .views import lista_contratos

urlpatterns = [
    path('contratos/', lista_contratos, name='lista_contratos'),
]