from datetime import date
from django.shortcuts import render
from .models import Atendimento

def lista_atendimentos(request):

    atendimentos = Atendimento.objects.all()

    context = {
        "atendimentos": atendimentos,
        "hoje": date.today(),
    }

    return render(request, "lista.html", context)