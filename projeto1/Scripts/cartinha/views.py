from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    #dicionario_contexto = {'msgnegrito':""}
    return render(request, 'django/index.html')
