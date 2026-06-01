import numpy as np
from numpy.typing import NDArray


class Solution:
    
    def sigmoid(self, z: NDArray[np.float64]) -> NDArray[np.float64]:
        # z is a 1D NumPy array
        # Formula: 1 / (1 + e^(-z))
        # return np.round(your_answer, 5)
        formula = 1 / ( 1 + np.exp(-z))
        return np.round(formula, 5)
    

    def relu(self, z: NDArray[np.float64]) -> NDArray[np.float64]:
        # z is a 1D NumPy array
        # Formula: max(0, z) element-wise
        relu = []
        for i in z:
            if i <= 0.0:
                relu.append(0.0)
            else:
                relu.append(i)
        return np.array(relu)
