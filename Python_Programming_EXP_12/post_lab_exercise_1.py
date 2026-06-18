import numpy as np
import matplotlib.pyplot as plt

# Parameters
fs = 1000
t = np.linspace(0, 1, fs, endpoint=False)

# Signals
sine1 = np.sin(2 * np.pi * 5 * t)
sine2 = np.sin(2 * np.pi * 10 * t)
# Addition
added_signal = sine1 + sine2

# Plot
plt.figure(figsize=(10, 5))
plt.plot(t, sine1, label="5 Hz Sine")
plt.plot(t, sine2, label="10 Hz Sine")
plt.plot(t, added_signal, label="Added Signal", linewidth=2)
plt.legend()
plt.title("Addition of 5 Hz and 10 Hz Sine Waves")
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.show()