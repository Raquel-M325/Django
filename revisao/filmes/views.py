from django.shortcuts import render
from .services import Filmes, Avaliacao
from django.http import JsonResponse


# Create your views here.
filmes = [
    Filmes("The Chosen", "Cristão", "Como um homem chamado Jesus Cristo salvou o mundo"),
    Filmes("Digital Circus", "Fantasia", "Pessoas presas numa plataforma digital pela IA"),
    Filmes("FNAF 3", "Terror", "Animatronics presos numa pizzaria"),
]

titulos = [
    "Avaliação dos Filmes",
    "Selecione qual dos filmes você deseja comentar",
]

def index(request):
    return render(request, "index.html", {
        "titulos" : titulos,
    })

def envia_avaliacao(request):
    if (request.method == "POST"):
        autor = request.POST.get("autor")
        comentario = request.POST.get("comentario")
        nota = request.POST.get("nota")
        avaliacao = Avaliacao(autor, comentario, nota)

        if not avaliacao:
            return JsonResponse({"erro" : "está vazio!"})
            

        return JsonResponse({
            "avaliacao" : avaliacao    
        })