from django.shortcuts import render
from aplicacion.models import familiar
from django.http import HttpResponse
from django.template import Template, Context

def listado_familiares(request):

    archivo=open(r"C:\Users\martisej\Desktop\Python\mvt_mio\mvt\aplicacion\templates\aplicacion\familiares.html")
    plantilla=Template(archivo.read())
    archivo.close()

    familiares=familiar.objects.all()

    cadena=""

    for persona in familiares:
        
       cadena+= persona.nombre + " " +  str(persona.edad) + " "
       

    datos={"Nombre":cadena}
    contexto=Context(datos)
    documento=plantilla.render(contexto)
    return HttpResponse(documento)



    #return render(request, "aplicacion/familiares.html")

 #   familiares=familiar.objects.all()

  #  cadena=""

   # for persona in familiares:
        
    #    cadena+= persona.nombre + " "

    #return HttpResponse(cadena)

