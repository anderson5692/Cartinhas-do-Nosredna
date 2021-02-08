from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    #d1 = {'':""}
    return render(request, 'django/index.html')
    return render(request, 'django/page1.html')
    
