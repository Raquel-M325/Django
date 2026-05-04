from django.shortcuts import render
from django.http import JsonResponse
from .services import Previsao

lista_cidade = {
    "Natal":           {"Clima": "Chuvoso", "Temperatura": "22°C"},
    "Parnamirim":      {"Clima": "Nublado", "Temperatura": "27°C"},
    "Macaíba":         {"Clima": "Ensolarado", "Temperatura": "29°C"},
    "Mossoró":         {"Clima": "Parcialmente Nublado", "Temperatura": "31°C"},
    "Caicó":           {"Clima": "Tempestuoso", "Temperatura": "28°C"},
    "Currais Novos":   {"Clima": "Nevoeiro", "Temperatura": "24°C"},
    "Açu":             {"Clima": "Ventoso", "Temperatura": "30°C"},
    "Pau dos Ferros":  {"Clima": "Chuvoso", "Temperatura": "25°C"},
    "Santa Cruz":      {"Clima": "Nublado", "Temperatura": "26°C"},
    "Apodi":           {"Clima": "Ensolarado", "Temperatura": "33°C"},
}

titulos = [
    "Previsão de Tempo",
    "Busque a sua cidade e veja a previsão do tempo!"
]

def index(request):
    return render(request, "previsao/index.html", {
        "titulo": titulos
    })

def receber_cidade(request):
    if request.method == "GET":
        cidade = request.GET.get("cidade")

        if not cidade:
            return JsonResponse({"erro": "O campo está vazio! Por favor preencha"})

        dados = lista_cidade.get(cidade.title())

        if not dados:
            return JsonResponse({"erro": "Cidade não encontrada!"})

        previsao = Previsao(cidade, dados["Clima"], dados["Temperatura"])

        return JsonResponse({
            "cidade": previsao.cidade,
            "clima": previsao.clima,
            "temperatura": previsao.temperatura,
            "confirmacao": "Enviado com sucesso!"
        })