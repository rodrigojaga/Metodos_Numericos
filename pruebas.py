import numpy as np
import matplotlib.pyplot as plt
import math
x = np.linspace(-10, 10, 100)

f = ((math.e ** (-1*x)) - x)

plt.plot(x, f)
plt.grid()
plt.show()

