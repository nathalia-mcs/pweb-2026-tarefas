from django.shortcuts import render

# Create your views here.

def index(request):
    dados_usuario = {"nome": "Michael Douglas", "idade": 23}
    return render(request, "index.html", dados_usuario)