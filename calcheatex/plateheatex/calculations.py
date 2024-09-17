import math
from iapws import IAPWS97
import CoolProp.CoolProp as CP

def coldPropertiesCoolant (tempColdIn, tempColdOut, pressureCold, coldHumidity, selectTypeColdCoolant):
    # Перевод едениц измерения
    tempColdIn = tempColdIn + 273.15
    coldHumidity = coldHumidity / 100
    if selectTypeColdCoolant == "humidAir":
        densityColdCoolant = (((pressureCold - CP.HAPropsSI('P_w','T',tempColdIn,'P',pressureCold,'R',coldHumidity))/287.058)+(CP.HAPropsSI('P_w','T',tempColdIn,'P',pressureCold,'R',coldHumidity)/461.522))/tempColdIn
        dynamicViscosityColdCoolant = CP.HAPropsSI("M", "T", tempColdIn,"P",pressureCold,'R',coldHumidity)
        kinematicViscosityColdCoolant = (CP.HAPropsSI("M", "T", tempColdIn,"P",pressureCold,'R',coldHumidity))/densityColdCoolant
        conductivityColdCoolant = CP.HAPropsSI("K", "T", tempColdIn,"P",pressureCold,'R',coldHumidity)
        heatCapacityColdCoolant = CP.HAPropsSI("Cha", "T", tempColdIn,"P",pressureCold,'R',coldHumidity)
        thermDiffusivityColdCoolant = conductivityColdCoolant / (densityColdCoolant*heatCapacityColdCoolant)
        prandtlColdCoolant = kinematicViscosityColdCoolant / thermDiffusivityColdCoolant
        # добавить усреднение температуры и проверку ошибки ввода тем-ры
    else:
        densityColdCoolant = CP.PropsSI("D", "T", tempColdIn, "P", pressureCold, selectTypeColdCoolant)
        dynamicViscosityColdCoolant = CP.PropsSI("V", "T", tempColdIn,"P",pressureCold,selectTypeColdCoolant)
        kinematicViscosityColdCoolant = (CP.PropsSI("V", "T", tempColdIn,"P",pressureCold,selectTypeColdCoolant))/densityColdCoolant
        prandtlColdCoolant = CP.PropsSI("PRANDTL", "T", tempColdIn,"P",pressureCold,selectTypeColdCoolant)
        conductivityColdCoolant = CP.PropsSI("L", "T", tempColdIn,"P",pressureCold,selectTypeColdCoolant)
        heatCapacityColdCoolant = CP.PropsSI("C", "T", tempColdIn,"P",pressureCold,selectTypeColdCoolant)
        thermDiffusivityColdCoolant = conductivityColdCoolant / (densityColdCoolant*heatCapacityColdCoolant)
    return densityColdCoolant, dynamicViscosityColdCoolant, kinematicViscosityColdCoolant, prandtlColdCoolant, conductivityColdCoolant, heatCapacityColdCoolant, thermDiffusivityColdCoolant
def hotPropertiesCoolant (tempHotIn, tempHotOut, pressureHot, hotHumidity, selectTypeHotCoolant):
    # Перевод едениц измерения
    hotHumidity = hotHumidity / 100
    tempHotIn = tempHotIn + 273.15
    if selectTypeHotCoolant == "humidAir":
        densityHotCoolant = (((pressureHot - CP.HAPropsSI('P_w','T',tempHotIn,'P',pressureHot,'R',hotHumidity))/287.058)+(CP.HAPropsSI('P_w','T',tempHotIn,'P',pressureHot,'R',hotHumidity)/461.522))/tempHotIn
        dynamicViscosityHotCoolant = CP.HAPropsSI("M", "T", tempHotIn,"P",pressureHot,'R',hotHumidity)
        kinematicViscosityHotCoolant = (CP.HAPropsSI("M", "T", tempHotIn,"P",pressureHot,'R',hotHumidity))/densityHotCoolant
        conductivityHotCoolant = CP.HAPropsSI("K", "T", tempHotIn,"P",pressureHot,'R',hotHumidity)
        heatCapacityHotCoolant = CP.HAPropsSI("Cha", "T", tempHotIn,"P",pressureHot,'R',hotHumidity)
        thermDiffusivityHotCoolant = conductivityHotCoolant / (densityHotCoolant*heatCapacityHotCoolant)
        prandtlHotCoolant = kinematicViscosityHotCoolant / thermDiffusivityHotCoolant
         # добавить усреднение температуры и проверку ошибки ввода тем-ры
    else:
        densityHotCoolant = CP.PropsSI("D","T", tempHotIn,"P",pressureHot,selectTypeHotCoolant)
        dynamicViscosityHotCoolant = CP.PropsSI("V", "T", tempHotIn,"P",pressureHot,selectTypeHotCoolant)
        kinematicViscosityHotCoolant = (CP.PropsSI("V", "T", tempHotIn,"P",pressureHot,selectTypeHotCoolant))/densityHotCoolant
        prandtlHotCoolant = CP.PropsSI("PRANDTL", "T", tempHotIn,"P",pressureHot,selectTypeHotCoolant)
        conductivityHotCoolant = CP.PropsSI("L", "T", tempHotIn,"P",pressureHot,selectTypeHotCoolant)
        heatCapacityHotCoolant = CP.PropsSI("C", "T", tempHotIn,"P",pressureHot,selectTypeHotCoolant)
        thermDiffusivityHotCoolant = conductivityHotCoolant / (densityHotCoolant*heatCapacityHotCoolant)
    return densityHotCoolant, dynamicViscosityHotCoolant, kinematicViscosityHotCoolant, prandtlHotCoolant, conductivityHotCoolant, heatCapacityHotCoolant, thermDiffusivityHotCoolant

# def calcPartialPressure(inputTemperature):
#     partialPressure = 133.3*math.e**(18.6-(3992/(inputTemperature+233.8)))
#     return partialPressure
