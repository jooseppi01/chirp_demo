import numpy as np
import matplotlib.pyplot as plt

# Constants
c = 299792458  # Speed of light in m/s
slope = 0.004  # Chirp slope (0.001 GHz/µs)
f1 = 77e9  # Frequency of signal 1 in Hz
f2 = 78e9  # Frequency of signal 2 in Hz
t = np.linspace(0, 1e-9, 1000)  # Time array over 1 ns with 1000 samples

#funktio joka muuttaa sekunnit mikrosekunneiksi
def to_µs(seconds):
    return seconds * 1e6

d = 150
tt = (to_μs(d) / c) * 2
print(f"Time to target: {tt} µs")

h = tt * 4
print(f"slope change: {h} ghz")


# Generate signals
s1 = np.sin(2 * np.pi * f1 * t)
s2 = np.sin(2 * np.pi * f2 * t)

# Generate IF signal
IF_signal = np.sin(2 * np.pi * (f2 - f1) * t)  # IF frequency is f2 - f1

# Calculate IF frequency signal
IF_frequency_signal = s1 * s2

# Perform FFT on IF frequency signal
fft_result = np.fft.fft(IF_frequency_signal)
fft_freq = np.fft.fftfreq(len(t), d=(t[1] - t[0]))  # Frequency axis for FFT result

# get the highest peak in the FFT result
# Frequency in gHz
IF_frequency = fft_freq[np.argmax(np.abs(fft_result))] / 1e9
print(f"Estimated IF Frequency: {IF_frequency} gHz")

# Calculate the range of the target
range_to_target = (c * IF_frequency) / (slope)  # Distance in meters
print(f"Estimated Distance to Target: {range_to_target} meters")

aa = 100 / c
print(aa)


# Plotting
plt.figure(figsize=(12, 10))

# Plot Signal 1 (77 GHz)
plt.subplot(3, 1, 1)
plt.plot(t * 1e9, s1, label='77 GHz Signal', color='blue')
plt.title('77 GHz Signal')
plt.xlabel('Time (ns)')
plt.ylabel('Amplitude')
plt.grid()

# Plot Signal 2 (87 GHz)
plt.subplot(3, 1, 2)
plt.plot(t * 1e9, s2, label='78 GHz Signal', color='orange')
plt.title('78 GHz Signal')
plt.xlabel('Time (ns)')
plt.ylabel('Amplitude')
plt.grid()

#Plot IF Signal
plt.subplot(3, 1, 3)
plt.plot(t * 1e9, IF_signal, label='IF Signal', color='green')
plt.title('Intermediate Frequency (IF) Signal')
plt.xlabel('Time (ns)')
plt.ylabel('Amplitude')
plt.grid()

# # FFT of IF Signal
# plt.subplot(3, 1, 3)
# plt.plot(fft_freq / 1e9, np.abs(fft_result), label='FFT of IF Signal', color='red')
# plt.title('FFT of the IF Signal')
# plt.xlabel('Frequency (GHz)')
# plt.ylabel('Magnitude')
# plt.xlim(-100, 100)  # Limit x-axis for better visibility
# plt.grid()

plt.tight_layout()
plt.show()
