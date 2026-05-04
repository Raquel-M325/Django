from django.shortcuts import render
from django.http import JsonResponse

def mensagem(request):
    return JsonResponse({'texto' : 'Olá servidor'})

# Create your views here.
