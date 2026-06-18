import numpy as np
import matplotlib.pyplot as plt

# Parameters
fs = 500
t = np.linspace(0, 1, fs, endpoint=False)

# Signals
sine_original = np.sin(2 * np.pi * 5 * t)
sine_reversed = sine_original[::-1]  # reverse array

# Plot
plt.figure(figsize=(10, 5))
plt.plot(t, sine_original, label="Original (5 Hz Sine)")
plt.plot(t, sine_reversed, label="Reversed in Time")
plt.legend()
plt.title("Time-Reversed Sine Wave (5 Hz)")
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.show() 