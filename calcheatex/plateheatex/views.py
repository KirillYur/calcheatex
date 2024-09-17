from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from .calculations import *
from django.http import JsonResponse

def index(request):

        return render(request, 'plateheatex/index.html', {'total_result': 0})

def calc(request):

        tempHotIn = float(request.POST.get('tempHotIn', 0))
        tempHotOut = float(request.POST.get('tempHotOut', 0))
        pressureHot = float(request.POST.get('pressureHot', 0))
        selectTypeHotCoolant = str(request.POST.get('selectTypeHotCoolant'))

        tempColdIn = float(request.POST.get('tempColdIn', 0))
        tempColdOut = float(request.POST.get('tempColdOut', 0))
        pressureCold = float(request.POST.get('pressureCold', 0))
        selectTypeColdCoolant = str(request.POST.get('selectTypeColdCoolant'))
        
        flowHot = request.POST.get('flowHot', 0)
        if flowHot == '':
                flowHot = 0
        else:
                flowHot = float(flowHot)
        
        hotHumidity = request.POST.get('hotHumidity', 0)
        if hotHumidity == '':
                hotHumidity = 0
        else:
                hotHumidity = float(hotHumidity)

        flowCold = request.POST.get('flowCold', 0)
        if flowCold == '':
                flowCold = 0
        else:
                flowCold = float(flowCold)
        
        coldHumidity = request.POST.get('coldHumidity', 0)
        if coldHumidity == '':
                coldHumidity = 0
        else:
                coldHumidity = float(coldHumidity)

        densityColdCoolant, dynamicViscosityColdCoolant, kinematicViscosityColdCoolant, prandtlColdCoolant, conductivityColdCoolant, heatCapacityColdCoolant, thermDiffusivityColdCoolant = hotPropertiesCoolant(tempHotIn, tempHotOut, pressureHot, hotHumidity, selectTypeHotCoolant)
        densityHotCoolant, dynamicViscosityHotCoolant, kinematicViscosityHotCoolant, prandtlHotCoolant, conductivityHotCoolant, heatCapacityHotCoolant, thermDiffusivityHotCoolant = coldPropertiesCoolant(tempColdIn, tempColdOut, pressureCold, coldHumidity, selectTypeColdCoolant)
        
        propertiesCoolants = {
        'densityColdCoolant': round(densityColdCoolant, 3),
        'dynamicViscosityColdCoolant': f"{dynamicViscosityColdCoolant:.3e}",
        'kinematicViscosityColdCoolant': f"{kinematicViscosityColdCoolant:.3e}",
        'prandtlColdCoolant': round(prandtlColdCoolant, 3),
        'conductivityColdCoolant': round(conductivityColdCoolant, 3),
        'heatCapacityColdCoolant': round(heatCapacityColdCoolant, 3),
        'thermDiffusivityColdCoolant': f"{thermDiffusivityColdCoolant:.3e}",

        'densityHotCoolant': round(densityHotCoolant, 3),
        'dynamicViscosityHotCoolant': f"{dynamicViscosityHotCoolant:.3e}",
        'kinematicViscosityHotCoolant': f"{kinematicViscosityHotCoolant:.3e}",
        'prandtlHotCoolant': round(prandtlHotCoolant, 3),
        'conductivityHotCoolant': round(conductivityHotCoolant, 3),
        'heatCapacityHotCoolant': round(heatCapacityHotCoolant, 3),
        'thermDiffusivityHotCoolant': f"{thermDiffusivityHotCoolant:.3e}",
        }
        # resultPartialPressure = calcPartialPressure(inputTemperature)

        return JsonResponse({'propertiesCoolants' : propertiesCoolants
        })

def types(request, types_id):
        return HttpResponse ("Теплообменники по типам")

def page_not_found(request, exception):
        return HttpResponseNotFound("<h1>Страница не найдена</h1>")

