import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

y_hat = np.arange(-8, 8.1, 0.1)
print(y_hat)
sns.lineplot(x=y_hat, y=1/(1+np.exp(-y_hat)))
plt.grid()
plt.show()

