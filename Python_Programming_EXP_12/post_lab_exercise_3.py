import numpy as np
import matplotlib.pyplot as plt

# Parameters
fs = 500
t = np.linspace(0, 1, fs, endpoint=False)

# Signals
sine_original = np.sin(2 * np.pi * 5 * t)
sine_shifted = np.sin(2 * np.pi * 5 * (t - 0.1))  # shift by 0.1 sec

# Plot
plt.figure(figsize=(10, 5))
plt.plot(t, sine_original, label="Original (5 Hz Sine)")
plt.plot(t, sine_shifted, label="Shifted by 0.1s")
plt.legend()
plt.title("Time-Shifted Sine Wave (5 Hz)")
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.show()