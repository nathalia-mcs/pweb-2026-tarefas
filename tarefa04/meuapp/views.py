from datetime import date
from django.shortcuts import render
from .models import atendimentos

def lista_atendimentos(request):

    atendimento = atendimentos.objects.all()

    context = {
        "atendimentos": atendimentos,
        "hoje": date.today()
    }

    return render(request, "lista.html", context)