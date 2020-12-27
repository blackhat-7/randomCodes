import numpy as np


def check_cond(x):
    mat = np.array([
        [1, 0],
        [0, 10**(-x)]
    ])
    return np.linalg.cond(mat)


for x in range(10, 20):
    print(f"Condition Number with x={x}: {check_cond(x)}")
