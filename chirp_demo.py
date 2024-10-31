import numpy as np
import matplotlib.pyplot as plt

# Constants
c = 299792458  # Speed of light in m/s
slope = 4.724e15  # Chirp slope (Hz/s), for max range of 127m
tx_chirp = 78e9  # Frequency of signal 1 in Hz
rx1_chirp = 77e9  # Frequency of signal 2 in Hz
rx2_chirp = 77.5001e9  # Frequency of signal 2 in Hz

t = np.linspace(0, 1e-9, 1000)  # Time array over 1 ns with 1000 samples

# Generate signals
s1 = np.sin(2 * np.pi * tx_chirp * t)
s2 = np.sin(2 * np.pi * rx1_chirp * t)

# Generate IF signal
IF_signal = np.sin(2 * np.pi * (tx_chirp - rx1_chirp) * t)  # IF frequency is rx1_chirp - tx_chirp

# get the if frequency of tx and rx1
IF_frequency = tx_chirp - rx1_chirp

# get the if frequency of tx and rx2
IF_frequency2 = tx_chirp - rx2_chirp

#print the IF frequencies
print("The IF frequency is: ", IF_frequency, "Hz")
print("The IF frequency is: ", IF_frequency2, "Hz")

# Calculate the range of the target in meters with 4 decimal places
R = (c * IF_frequency) / (2 * slope)  # Distance in meters
R2 = (c * IF_frequency2) / (2 * slope)  # Distance in meters

# print the range of the target in millimeters
print("The range of the target is: ", R, "meters")
print("The range of the target is: ", R2, "meters")



