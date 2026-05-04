from django.shortcuts import render
from django.http import JsonResponse
from .services import Postagem, Comentario

# Create
postagens = [
    #usei isso na classe Postagem para aproveitar usar em substituicao de um dicionario
    Postagem("Que jogo gostaria de ver, comente", "Pode ser sobre jogos internacionais"),
    Postagem("Criticas sobre o jogo Garden of banban", "Diga o que observou sobre esse jogo"),
]

def index(request):
    return render(request, "comentarios/index.html", {
        'postagens' : postagens,
        "h1_titulo" : "Sistema de Comentários"

    })

def envie_comentario(request):
    if request.method == "POST":
        autor = request.POST.get("autor")
        conteudo = request.POST.get("conteudo")
        comentario = Comentario(conteudo, autor) #usei a classe do Comentario, pode usar diretamente os atributos

        return JsonResponse({
            "ok" : "Enviado com sucesso!",
            "completo" : f"<b>{comentario.autor}</b>: {comentario.conteudo}",        
        })



