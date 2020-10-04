from django.http import HttpResponse

def index(request):
    return HttpResponse("Ciao mondo!  Benvenuti!  Questo è il polls index.")
