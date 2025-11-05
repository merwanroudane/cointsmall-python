import numpy as np
from cointsmall import test_cointegration_breaks, get_critical_value

# Your data (replace with your actual data)
Y = np.array([1.2, 1.5, 1.8, 2.1, 2.3, 2.5, 2.7, 3.0, 3.2, 3.5,
              3.8, 4.0, 4.2, 4.5, 4.7, 5.0, 5.2, 5.5, 5.8, 6.0])
X = np.array([0.5, 0.7, 0.9, 1.1, 1.2, 1.4, 1.5, 1.7, 1.8, 2.0,
              2.2, 2.3, 2.5, 2.6, 2.8, 2.9, 3.1, 3.2, 3.4, 3.5]).reshape(-1, 1)

# Test for cointegration
result = test_cointegration_breaks(Y, X, n_breaks=0, model='o')

print(f"Are Y and X cointegrated? {result.reject_null}")
print(f"Test statistic: {result.statistic:.4f}")
print(f"Critical value: {result.critical_value:.4f}")