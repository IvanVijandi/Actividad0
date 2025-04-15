from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hola, esta es mi primer View para la actividad0")


