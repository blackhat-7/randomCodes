import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

x = np.arange(0, 1.1, 0.01)
print(x)
sns.lineplot(x=x, y=(np.log(x) - np.log(1 - x)))
plt.grid()
plt.show()
