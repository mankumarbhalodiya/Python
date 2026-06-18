import numpy as np
import matplotlib.pyplot as plt

# Parameters
fs = 500
t = np.linspace(0, 2, 2 * fs, endpoint=False)

# Signals
sine = np.sin(2 * np.pi * 5 * t)
cosine = np.cos(2 * np.pi * 10 * t)

# Multiplication
product_signal = sine * cosine

# Plot
plt.figure(figsize=(10, 5))
plt.plot(t, sine, label="5 Hz Sine")
plt.plot(t, cosine, label="10 Hz Cosine")
plt.plot(t, product_signal, label="Product Signal", linewidth=2)
plt.legend()
plt.title("Multiplication of 5 Hz Sine and 10 Hz Cosine")
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.show()