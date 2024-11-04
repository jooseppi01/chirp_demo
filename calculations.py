import numpy as np


'''
1ghz = 1e9 hz
1hz = 1e-9 ghz
1mhz/s = 1e12 hz/s

1hz/s = 1e-12 mhz/µs
1µs = 1e-6 s

1mm = 1e-3 m
'''

# Constants
c = 299792458  # Speed of light in m/s  
d = 100 # Distance to object in meters
b = 4e9 # Bandwidth in Hz
maxIF = b
theta = np.radians(45) # Angle in radians
antDist = 0.00195 # Distance between antennas in meters
lambda_ = c / 77e9 # Wavelength in meters



slope = (c * maxIF) / (2 * d)
print("The slope is in hz/s: ", slope)
slope_mhzµs = slope * 1e-12 # Convert to MHz/µs
print("The slope is: ", slope_mhzμs, "MHz/µs")

Tc = b / slope # Chirp time in seconds
print("The chirp time is in seconds: ", Tc)
Tc_µs = Tc * 1e6 # Chirp time in microseconds
print("The chirp time is: ", Tc_µs, "µs")

dres = c / (2 * b) # Range resolution in meters
dres = dres * 100
print("The range resolution is: ", dres, "cm")

range = (c * b) / (2 * slope) # Range in meters
print("The range is in meters: ", range)

s = 4.721e15 
f = (s * 2 * d) / c # Frequency of IF in Hz
aa = f * 1e-9
print(f"The frequency of IF is in gHz: {f} Hz")
print(aa)

rx2_extra = antDist * np.sin(theta) # Extra distance in meters
print("The extra distance is in meters: ", rx2_extra)

phase_diff = (2 * np.pi * rx2_extra) / lambda_ # Phase difference in radians
print("The phase difference is in radians: ", phase_diff)
phase_diffdeg = np.degrees(phase_diff)
print("The phase difference is in degrees: ", phase_diffdeg)



kulma = np.arcsin((phase_diff * lambda_) / (2 * np.pi * antDist)) # Angle in radians
print("The angle is in radians: ", kulma)
kulmadeg = np.degrees(kulma)
print("The angle is in degrees: ", kulmadeg)

max_angle = np.arcsin((lambda_) / (2 * antDist)) # Maximum angle in radians
print("The maximum angle is in radians: ", max_angle)
max_angle = np.degrees(max_angle)
print("The maximum angle is in degrees: ", max_angle)

#calculate coordinates
x = d * np.cos(kulma) * np.sin(kulma)
y = d * np.cos(kulma) * np.cos(kulma)
z = d * np.sin(kulma)
print("The x coordinate is: ", x)
print("The y coordinate is: ", y)
print("The z coordinate is: ", z)

#plot coordinates
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter
ax.scatter(x, y, z, c='r', marker='o')
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')
plt.show()

