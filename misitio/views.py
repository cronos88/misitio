from django.http import HttpResponse, Http404
import datetime

def hola(request):
    return HttpResponse("Hola Mundo")

def fecha_actual(request):
    ahora = datetime.datetime.now()
    html = "<html><body><h1>Fecha: </h1><h3>{0}</h3></body></html>".format(ahora)
    return HttpResponse(html)

def horas_adelante(request, offset):
    try:
        offset=int(offset)
    except ValueError:
        raise Http404

    dt= datetime.datetime.now()+datetime.timedelta(hours=offset)

    html = "<html><body><h1>En {0} hora(s), serán:<h1><h3>{1}</h3></body></html>".format(offset, dt)
    return HttpResponse(html)




