import numpy as np
import matplotlib.pyplot as plt

# Parameters
fs = 500
t = np.linspace(0, 1, fs, endpoint=False)

# Signals
sine_original = np.sin(2 * np.pi * 10 * t)
sine_scaled = 3 * sine_original  # scaling by factor 3

# Plot
plt.figure(figsize=(10, 5))
plt.plot(t, sine_original, label="Original (10 Hz Sine)")
plt.plot(t, sine_scaled, label="Scaled (×3)")
plt.legend()
plt.title("Amplitude Scaled Sine Wave (10 Hz)")
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.show()
