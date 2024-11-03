import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Määritellään vakioita

c = 299792458   # Valon nopeus m/s
R = 70          # Etäisyys kohteeseen m
d = 0.002       # antennien välinen etäisyys m (2mm)

IF1 = 77.1e9      # RX1 IF taajuus Hz
IF2 = 77.2e9      # RX2 IF taajuus Hz
IF3 = 77.3e9        # RX3 IF taajuus Hz
IF4 = 77.4e9        # RX4 IF taajuus Hz


al1 = c / (IF1)
al2 = c / (IF2)
al3 = c / (IF3)
al4 = c / (IF4)

# lasketaan vaihe-ero
ve = 2 * np.pi * d / al1
ve2 = 2 * np.pi * d / al2
ve3 = 2 * np.pi * d / al3
ve4 = 2 * np.pi * d / al4

# print aallonpituudet
print(al1, al2, al3, al4)

# laske vaihe-erot
print(ve, ve2, ve3, ve4)


kulma = np.sin(0.0039 * np.pi) / (2 * np.pi * 0.004)
print(kulma)

kulma2 = np.arcsin(kulma)
print(kulma2)

# lasketaan koordinaatit

x = R * np.cos(kulma2) * np.sin(0.0039)
y = R * np.cos(kulma2) * np.cos(0.0039)
z = R * np.sin(kulma2)

print(x, y, z)

# Piirretään 3D-pistepilvi
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Piirretään pisteet
ax.scatter(x, y, z, c='b', marker='o', s=50, label='Kohteet')

# Asetetaan akselien nimet
ax.set_xlabel('X (m)')
ax.set_ylabel('Y (m)')
ax.set_zlabel('Z (m)')
ax.set_xlim([-100, 100])
ax.set_ylim([-100, 100])
ax.set_zlim([-100, 100])

# Asetetaan otsikko ja legendat
ax.set_title('3D-pistepilvi kohteiden sijainnista')
ax.legend()

# Näytetään kuvaaja
plt.show()

