import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

def load_sin(fs=44000, duration=0.2):
    t = np.linspace(0, duration, int(fs * duration), endpoint=False)
    audio = 0.5 * np.sin(2 * np.pi * 440 * t) + \
            0.4 * np.sin(2 * np.pi * 880 * t) + \
            0.2 * np.exp(-4 * t) * np.sin(2 * np.pi * 1000 * t)
    return fs, audio

# Load signal
fs, x = load_sin(fs=14400, duration=0.5)

# Create impulse response
h = np.zeros_like(x)
t = np.linspace(0, len(h) / fs, len(h), endpoint=False)
h[::int(fs * 0.01)] = np.exp(-t[::int(fs * 0.01)] * 10)

# Linear convolution
y_linear = signal.convolve(x, h, mode='full')

# Circular convolution using FFT
N = len(x) + len(h) - 1
h_pad = np.pad(h, (0, N - len(h)))
x_pad = np.pad(x, (0, N - len(x)))
y_circ = np.real(np.fft.ifft(np.fft.fft(x_pad) * np.fft.fft(h_pad)))

# Truncate circular conv to match linear length
y_circ_trunc = y_circ[:len(y_linear)]

# Plotting
fig, axes = plt.subplots(4, 1, figsize=(12, 10))

# Time axes matching signal lengths
time_x = np.arange(len(x)) / fs
time_h = np.arange(len(h)) / fs
time_y = np.arange(len(y_linear)) / fs
time_circ = np.arange(len(y_circ_trunc)) / fs

axes[0].plot(time_x, x)
axes[0].set_title('Original Audio')
axes[0].grid(True)

axes[1].plot(time_h, h)
axes[1].set_title('Impulse Response')
axes[1].grid(True)

axes[2].plot(time_y, y_linear)
axes[2].set_title('Linear Convolution')
axes[2].grid(True)

axes[3].plot(time_circ, y_circ_trunc)
axes[3].set_title('Circular Convolution')
axes[3].grid(True)

plt.tight_layout()

# Difference plot
min_len = min(len(y_linear), len(y_circ_trunc))
time_diff = np.arange(min_len) / fs
diff = y_linear[:min_len] - y_circ_trunc[:min_len]

plt.figure(figsize=(12, 4))
plt.plot(time_diff, diff)
plt.title('Difference: Linear - Circular')
plt.xlabel('Time (s)')
plt.grid(True)
plt.show()

print('Linear convolution shows true filtering effect; circular convolution has wrap-around artifacts.')
