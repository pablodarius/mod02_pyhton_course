from django.http import HttpResponse
import datetime
from django.template import Template, Context

class Person():
    def __init__(self, name, seconod_name):
        self.name = name
        self.seconod_name = seconod_name

def saludo(request): # first view
    themes = ["Templates","Models","Forms","Views","Deploy"]
    #themes = []

    p1 = Person("Pablo", "Pantoja")

    name = "Juan"
    #second_name = "Díaz"
    time = datetime.datetime.now()

    doc_externo = open("c:/Users/Pablo/Desktop/CURSO PYTHON/mod02_pyhton_course/django/Proyecto1/Proyecto1/templates/mytemplate.html")
    plt = Template(doc_externo.read())
    doc_externo.close()

    # ctx = Context({"name":name, "second_name":"Díaz", "time":time})
    ctx = Context({"name":p1.name, "second_name":p1.seconod_name, "time":time, "themes":themes})
    document = plt.render(ctx)

    return HttpResponse(document)


def despedida(request):
    return HttpResponse("See you!")

def time_clock(request):
    time = datetime.datetime.now()
    documento = "<html><body><h1>Date and time %s</h2></body></html>" % time

    return HttpResponse(documento)

def future_age(request, age, year):    
    period = year - 2020
    futureAge = age + period
    documento = "<html><body><h2>In %s you will %s years old</h2></body></html>" %(year, futureAge)

    return HttpResponse(documento)