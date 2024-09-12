import math
from iapws import IAPWS97
import CoolProp.CoolProp as CP

def coldDensity (tempColdIn, tempColdOut, pressureCold, selectTypeColdCoolant):
    tempColdIn = tempColdIn + 273.15
    if selectTypeColdCoolant == "humidAir":
        densityColdCoolant = (((pressureCold - CP.HAPropsSI('P_w','T',tempColdIn,'P',pressureCold,'R',0.1))/287.058)+(CP.HAPropsSI('P_w','T',tempColdIn,'P',pressureCold,'R',0.1)/461.522))/tempColdIn
        return densityColdCoolant
        # добавить выбор влажности и усреднение тем-р
    else:
        densityColdCoolant = CP.PropsSI("D", "T", tempColdIn, "P", pressureCold, selectTypeColdCoolant)
        return densityColdCoolant
    
def hotDensity (tempHotIn, tempHotOut, pressureHot, selectTypeHotCoolant):
    tempHotIn = tempHotIn + 273.15
    if selectTypeHotCoolant == "humidAir":
        densityHotCoolant = (((pressureHot - CP.HAPropsSI('P_w','T',tempHotIn,'P',pressureHot,'R',0.1))/287.058)+(CP.HAPropsSI('P_w','T',tempHotIn,'P',pressureHot,'R',0.1)/461.522))/tempHotIn
         # добавить выбор влажности и усреднение тем-р
        return densityHotCoolant
    else:
        densityHotCoolant = CP.PropsSI("D", "T", tempHotIn, "P", pressureHot, selectTypeHotCoolant)
        return densityHotCoolant

# def calcThermDiffusivity(thermConductivity, substanceDensity, heatCapacity):
#     thermDiffusivity = thermConductivity/(substanceDensity*heatCapacity*10**3)
#     return thermDiffusivity

# def calcPartialPressure(inputTemperature):
#     partialPressure = 133.3*math.e**(18.6-(3992/(inputTemperature+233.8)))
#     return partialPressure
