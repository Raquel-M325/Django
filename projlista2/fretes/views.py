from django.shortcuts import render
from .services import Servico

distancias_fixas = {
    ("Fortaleza", "Natal"): 537,
    ("Fortaleza", "Recife"): 800,
    ("Fortaleza", "Joao Pessoa"): 688,
    ("Fortaleza", "Maceio"): 1075,
    ("Fortaleza", "Aracaju"): 1183,
    ("Fortaleza", "Salvador"): 1389,
    ("Fortaleza", "Teresina"): 634,
    ("Fortaleza", "Sao Luis"): 1070,
    ("Natal", "Joao Pessoa"): 185,
    ("Natal", "Maceio"): 572,
    ("Natal", "Aracaju"): 788,
    ("Recife", "Joao Pessoa"): 120,
    ("Recife", "Maceio"): 285,
    ("Recife", "Aracaju"): 501,
    ("Joao Pessoa", "Aracaju"): 611,
    ("Maceio", "Aracaju"): 294,
    ("Teresina", "Sao Luis"): 446,
}

lista_tabela_coluna = [
    "Origem",
    "Destino",
    "Custo",
]
    
# Create your views here.
def index(request):
    return render(request, "fretes/index.html", {
        "h1_titulo" : "Calculadora de Fretes",
    })

def frete(request):
    if (request.method == "POST"):
        origem = request.POST.get("origem")
        destino = request.POST.get("destino")

        #pega o valor da tupla do dicionario para usar como km_rodado e calcular automaticamente, seja qualquer ordem
        distancia = distancias_fixas.get((origem, destino)) or distancias_fixas.get((destino, origem))

        if not distancia:
            return render(request, 'fretes/tabela.html', {
                "erro" : "Não está cadastrado dessa rota, tente novamente colocando outra rota!"
            })
        
        custo = Servico(distancia).calc_custo() #insere o valor para calculo, já sendo o valor calculado reservado

        return render(request, 'fretes/tabela.html', {
            "valor" : custo,
            "origem" : origem,
            "destino" : destino,
            "lista_tabela_coluna" : lista_tabela_coluna
        }) #envio esses dados para tabela, se fosse para formulario nao faria sentido por nao estar usando


        



