#coding UTF-8

import numpy as np
import matplotlib.pyplot as plt

x = np.random.normal(0, 1, 1000)

plt.hist(x,bins=30)
plt.show()