import math

def calcThermDiffusivity(thermConductivity, substanceDensity, heatCapacity):
    thermDiffusivity = thermConductivity/(substanceDensity*heatCapacity*10**3)
    return thermDiffusivity

def calcPartialPressure(inputTemperature):
    partialPressure = 133.3*math.e**(18.6-(3992/(inputTemperature+233.8)))
    return partialPressure
