import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft
from scipy.signal import find_peaks

# Parameters
sampling_frequency = 1000  # Sampling frequency in Hz
signal_frequency = 5      # Frequency of the sine wave in Hz
duration = 1              # Duration of the signal in seconds

# Generate a sine wave signal
t = np.linspace(0, duration, int(sampling_frequency * duration), endpoint=False)
signal = np.sin(2 * np.pi * signal_frequency * t)

# Perform FFT
fft_result = fft(signal)

# Calculate the frequencies corresponding to FFT bins
frequencies = np.fft.fftfreq(len(fft_result), 1 / sampling_frequency)

# Find the peak frequency
peaks, _ = find_peaks(np.abs(fft_result[:len(fft_result)//2]))
peak_frequency = frequencies[peaks[0]]

# Plot the original signal and its FFT
plt.figure(figsize=(12, 6))
plt.subplot(2, 1, 1)
plt.plot(t, signal)
plt.title('Original Sine Wave Signal')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')

plt.subplot(2, 1, 2)
plt.plot(frequencies[:len(fft_result)//2], np.abs(fft_result[:len(fft_result)//2]))
plt.title('FFT of the Signal')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude')
plt.axvline(x=peak_frequency, color='r', linestyle='--', label=f'Peak Frequency: {peak_frequency:.2f} Hz')
plt.legend()

plt.tight_layout()
plt.show()