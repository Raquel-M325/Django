from django.shortcuts import render

# Create your views here.
def index(request):
    semana = [
        "Segunda-Feira",
        "Terça-Feira",
        "Quarta-Feira",
        "Quinta-Feira",
        "Sexta-Feira",
        "Sábado",
        "Domingo",
    ]

    #recebe as informacoes do usuario escreveu dos temas e marcou dos dias
    temas = request.GET.get("temas")
    dia_escolhido = request.GET.getlist("dias") #pega os dias escolhidos
    cronograma = {}

    if (temas and dia_escolhido):
        temas_lista = [t.strip() for t in temas.split(",")]  #separa por virgula em lista e espaço

        #depois quero distribuir em cada elemento da lista para os dias que foram marcados
        for i, tema in enumerate(temas_lista): #numera a lista dos temas
            dia_distribuido = dia_escolhido[i % len(dia_escolhido)] #alterna o dia e tema para colocar e determinar

            if (dia_distribuido not in cronograma): #se nao tiver nada, fica vazia tendo lista
                cronograma[dia_distribuido] = []
            
            cronograma[dia_distribuido].append(tema) #senao, ele adiciona o tema e dia juntos em um dicionario do cronograma

    cronograma_lista = []

    for dia in semana:
        cronograma_lista.append({
            "dia" : dia,
            "temas" : cronograma.get(dia,[]),
        })

    return render(request, "index_cronograma.html", {
        "semana" : semana,
        "cronograma_lista" : cronograma_lista,
    })



