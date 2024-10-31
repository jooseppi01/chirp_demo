import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Määritellään etäisyys ja kulmat
distances = [16, 20, 25]  # Etäisyydet metreissä (voit lisätä tai muuttaa)
angles_azimuth = [30, 45, 60]  # Azimuti-kulmat asteina
angles_elevation = [0, 10, 20]  # Elevation-kulmat asteina

# Muutetaan kulmat radiaaneiksi laskelmia varten
angles_azimuth_rad = np.radians(angles_azimuth)
angles_elevation_rad = np.radians(angles_elevation)

# Tyhjät listat x, y ja z koordinaateille
x_coords = []
y_coords = []
z_coords = []

# Lasketaan kullekin etäisyydelle ja kulmalle koordinaatit
for R, theta, phi in zip(distances, angles_azimuth_rad, angles_elevation_rad):
    x = R * np.cos(phi) * np.sin(theta)
    y = R * np.cos(phi) * np.cos(theta)
    z = R * np.sin(phi)
    
    x_coords.append(x)
    y_coords.append(y)
    z_coords.append(z)

# Piirretään 3D-pistepilvi
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Piirretään pisteet
ax.scatter(x_coords, y_coords, z_coords, c='b', marker='o', s=50, label='Kohteet')

# Asetetaan akselien nimet
ax.set_xlabel('X (m)')
ax.set_ylabel('Y (m)')
ax.set_zlabel('Z (m)')

# Asetetaan otsikko ja legendat
ax.set_title('3D-pistepilvi kohteiden sijainnista')
ax.legend()

# Näytetään kuvaaja
plt.show()
