import numpy as np


'''
1ghz = 1e9 hz
1hz = 1e10-9 ghz
1mhz/s = 1e12 hz/s
1hz/s = 1e-12 mhz/µs
1µs = 1e-6 s
'''

# Constants
c = 299792458  # Speed of light in m/s  
d = 127 # Distance to object in meters
b = 4e9 # Bandwidth in Hz
maxIF = b

slope = (c * maxIF) / (2 * d)
print("The slope is in hz/s: ", slope)
slope_mhzµs = slope * 1e-12 # Convert to MHz/µs
Tc = b / slope # Chirp time in seconds
print("The chirp time is in seconds: ", Tc)
Tc_µs = Tc * 1e6 # Chirp time in microseconds
print("The slope is: ", slope_mhzμs, "MHz/µs")
print("The chirp time is: ", Tc_µs, "µs")


dres = c / (2 * b) # Range resolution in meters
B = c / (2 * dres) # Bandwidth in Hz

range = (c * b) / (2 * slope) # Range in meters
print("The range is in meters: ", range)

   	
