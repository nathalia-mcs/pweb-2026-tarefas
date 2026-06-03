from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "index.html")

def usuarios(request):
    dados_usuario = [
    {"nome": "Michael Douglas", "matricula": "20201111110090", "idade": 23, "cidade": "São Paulo do Potengi"},
    {"nome": "Nathalia Mileni", "matricula": "20201111110080", "idade": 18, "cidade": "São Pedro"},
    {"nome": "Maria Cícera", "matricula": "20201111110070", "idade": 44, "cidade": "Santa Maria"},
    {"nome": "Daniel Oliveira", "matricula": "20201111110060", "idade": 38, "cidade": "Riachuelo"},
    {"nome": "Lara Yasmin", "matricula": "20201111110050", "idade": 27, "cidade": "Natal"},
    ]
    return render(request, "usuarios.html", dados_usuario)