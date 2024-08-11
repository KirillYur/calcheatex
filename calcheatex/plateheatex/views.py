from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from .calculations import *
from django.http import JsonResponse

def index(request):

        return render(request, 'plateheatex/index.html', {'total_result': 0})

def calc(request):

        thermConductivity = float(request.POST.get('thermConductivity', 0))
        substanceDensity = float(request.POST.get('substanceDensity', 0))
        heatCapacity = float(request.POST.get('heatCapacity', 0))
        inputTemperature = float(request.POST.get('inputTemperature', 0))

        resultThermDiffusivity = calcThermDiffusivity(thermConductivity, substanceDensity, heatCapacity)

        resultPartialPressure = calcPartialPressure(inputTemperature)

        return JsonResponse({'resultThermDiffusivity' : resultThermDiffusivity,
                              'resultPartialPressure' : resultPartialPressure})

def types(request, types_id):
        return HttpResponse ("Теплообменники по типам")

def page_not_found(request, exception):
        return HttpResponseNotFound("<h1>Страница не найдена</h1>")

