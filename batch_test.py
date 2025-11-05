import numpy as np
from cointsmall import test_cointegration_breaks

# Simulate multiple variable pairs
np.random.seed(42)
T = 50

pairs = {
    'Pair_1': (np.random.randn(T), np.random.randn(T, 1)),
    'Pair_2': (np.random.randn(T), np.random.randn(T, 1)),
    'Pair_3': (np.random.randn(T), np.random.randn(T, 1)),
}

print("Testing multiple pairs for cointegration:")
print("-" * 60)

for name, (Y, X) in pairs.items():
    result = test_cointegration_breaks(Y, X, n_breaks=0, model='o')
    status = "✓ Cointegrated" if result.reject_null else "✗ Not cointegrated"
    print(f"{name}: {status} (stat={result.statistic:.4f})")