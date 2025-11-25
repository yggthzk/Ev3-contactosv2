from django.shortcuts import render

def home(request):
    return render(request, "index.html")
#lavistita por defecto al iniciar la pagina