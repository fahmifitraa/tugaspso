import matplotlib.pyplot as plt
import numpy as np
mu, sigma = 0, 500
x = np.arange(1, 100, 0.1)  # x axis
z = np.random.normal(mu, sigma, len(x))  # noise
y = x ** 2 + z # data
#plt.plot(x, y, linewidth=2, linestyle="-", c="b")  # it include some noise

from scipy.signal import savgol_filter
w = savgol_filter(y, 101, 2)
#plt.plot(x, w, 'b')  # high frequency noise removed

#plot all
fig, ax = plt.subplots(1,2)
ax[0].plot(x, y, linewidth=2, linestyle="-", c="b")
ax[1].plot(x, w, 'b')