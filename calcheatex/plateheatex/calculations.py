import math
from iapws import IAPWS97
import CoolProp.CoolProp as CP

def calcCoolantProperty (tempHotIn, tempHotOut, pressureHot,
                        tempColdIn, tempColdOut, pressureCold, selectTypeColdCoolant, wetAir):
    tempHotIn = tempHotIn +273.15
    if selectTypeColdCoolant == wetAir:
        densityHotCoolant = IAPWS97(T = tempHotIn, x = 0.5)
    else:
        densityHotCoolant = CP.PropsSI("D", "T", tempHotIn, "P", pressureHot, selectTypeColdCoolant)
    return densityHotCoolant
# def calcThermDiffusivity(thermConductivity, substanceDensity, heatCapacity):
#     thermDiffusivity = thermConductivity/(substanceDensity*heatCapacity*10**3)
#     return thermDiffusivity

# def calcPartialPressure(inputTemperature):
#     partialPressure = 133.3*math.e**(18.6-(3992/(inputTemperature+233.8)))
#     return partialPressure
