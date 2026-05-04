from django.shortcuts import render

# Create your views here.
def index(request):
    total = None

    consumo = request.GET.get("consumo") #como se fosse um input da página

    if (consumo):
        consumo = float(consumo) #pega o valor em real

        if (consumo <= 100):
            total = consumo * 0.50

        elif (consumo <= 200):
            total =  (100 * 0.50) + (consumo - 100) * 0.75

        else:
            total = (100 * 0.50) + (100 * 0.75) + (consumo - 200) * 1 

    return render(request, 'index_energia.html', {
        "custo": total,
    })