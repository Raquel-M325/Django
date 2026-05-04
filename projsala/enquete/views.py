from django.shortcuts import render

# Create your views here. PRECISO VER

votos = { #dicionário geral
    "Digital Circus" : 0,
    "Steven Universe" : 0,
    "Apenas um show" : 0,
    "Gravity Falls" : 0,
}

def index(request):
    desenhos = list(votos.keys()) #precisei tirar para verificar o dicionario em votos, já que ficaria redondante se fizesse a lista separado, então aqui já converte e pegar as chaves para copiar

    escolheu_opcao_desenho = request.GET.get("desenho")

    if escolheu_opcao_desenho: #se ocorrer um voto
        votos[escolheu_opcao_desenho] += 1

    return render(request, "index.html", {
        "desenhos" : desenhos, 
        "resultados" : votos,
    })