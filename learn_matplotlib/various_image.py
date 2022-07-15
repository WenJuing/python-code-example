from matplotlib import pyplot as plt
import numpy as np

x = np.arange(0, 2*np.pi, 0.001*np.pi)
y = np.sin(x)
y2 = np.cos(x)
plt.plot(x, y, color="red")
plt.plot(x, y2, color="blue")
plt.show()
