from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render


def saludo(request):
    return HttpResponse('Bienvenidos a la Familia Vega Silva')

def template_familia(request):
    context = {
        'Integrante_1':'Fabian Andres Vega Silva, nació el 16-12-1997 y tiene 24 años',
        'Integrante_2':'Gerardo del Carmen Vega Martinez, nació el 25-03-1958 y tiene 64 años, es mi Padre',
        'Integrante_3':'Gilda Silva Mejias, nació el 06-05-1958, tiene 64 años y es mi Madre'
                
    }
    return render (request, 'familia.html', context = context)