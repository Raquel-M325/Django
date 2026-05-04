from django.shortcuts import render

# Create your views here.
def index(request):

    montante = None
    parcela = None

    exibicao = [
        {"nome_request" : "dinheiro", "mostrar" : "Digite o valor do empréstimo:"},
        {"nome_request" : "juros", "mostrar" : "Digite a taxa de juros ao mês (%):"},
        {"nome_request" : "parcelas", "mostrar" : "Digite o número de parcelas:"},
    ]

    #entrada que está só em string
    valor = request.GET.get("dinheiro")
    taxa = request.GET.get("juros")
    numero_de_parcelas = request.GET.get("parcelas")

    #receber as informacoes do usuario se preencheu tudo
    if (valor and taxa and numero_de_parcelas):
        valor = float(valor)
        taxa = float(taxa) / 100 #em %
        numero_de_parcelas = int(numero_de_parcelas)

        #calcula com as informações
        montante = valor * (1 + taxa)**numero_de_parcelas
        parcela = montante / numero_de_parcelas

    #os que eu quero enviar as informacoes, tem que colocar todos
    return render(request, "index_emprestimo.html", {
        "dinheiro" : valor,
        "juros" : taxa * 100 if taxa else None, #0.02 para 2%, se não preencheu, não faz a conversão
        "parcela"  : parcela,
        "montante" : montante,
        "parcelas" : numero_de_parcelas,
        "exibicao" : exibicao,
    })
