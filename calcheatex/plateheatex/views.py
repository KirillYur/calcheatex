from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from .calculations import *
from django.http import JsonResponse

def index(request):

        return render(request, 'plateheatex/index.html', {'total_result': 0})

def calc(request):

        tempHotIn = float(request.POST.get('tempHotIn', 0))
        tempHotOut = float(request.POST.get('tempHotOut', 0))
        flowHot = float(request.POST.get('flowHot', 0))
        pressureHot = float(request.POST.get('pressureHot', 0))

        tempColdIn = float(request.POST.get('tempColdIn', 0))
        tempColdOut = float(request.POST.get('tempColdOut', 0))
        flowCold = float(request.POST.get('flowCold', 0))
        pressureCold = float(request.POST.get('pressureCold', 0))
        
        selectTypeColdCoolant = str(request.POST.get('selectTypeColdCoolant'))
        selectTypeHotCoolant = str(request.POST.get('selectTypeHotCoolant'))

        resultHotDensity = hotDensity(tempHotIn, tempHotOut, pressureHot, selectTypeHotCoolant)
        resultColdDensity = coldDensity(tempColdIn, tempColdOut, pressureCold, selectTypeColdCoolant)

        # resultPartialPressure = calcPartialPressure(inputTemperature)

        return JsonResponse({'resultHotDensity' : resultHotDensity,
                             'resultColdDensity' : resultColdDensity,
                        #       'resultPartialPressure' : resultPartialPressure
                        })

def types(request, types_id):
        return HttpResponse ("Теплообменники по типам")

def page_not_found(request, exception):
        return HttpResponseNotFound("<h1>Страница не найдена</h1>")

