# Project Structure

## cointsmall - Python Package

Complete Python implementation of the R package "cointsmall" for cointegration testing with structural breaks in very small samples.

```
cointsmall_python/
│
├── cointsmall/                    # Main package directory
│   ├── __init__.py               # Package initialization
│   ├── adf_test.py               # ADF test with automatic lag selection
│   ├── cointegration_test.py    # Main cointegration test implementation
│   ├── composite_test.py         # Composite testing procedure
│   ├── critical_values.py        # Critical value computation
│   └── verify.py                 # Verification against paper
│
├── examples/                      # Example scripts
│   ├── quick_start.py            # Quick start guide
│   └── comprehensive_examples.py # Comprehensive usage examples
│
├── docs/                          # Documentation
│   └── API.md                    # Complete API documentation
│
├── setup.py                       # Package installation script
├── requirements.txt               # Python dependencies
├── README.md                      # Main documentation
├── LICENSE                        # GPL-3 license
└── MANIFEST.in                    # Package manifest

```

## File Descriptions

### Core Package Files

**cointsmall/__init__.py**
- Package initialization
- Exports main functions and classes
- Version information

**cointsmall/adf_test.py**
- `adf_test_residuals()`: ADF test with automatic lag selection
- `ADFTestResult`: Result container class
- Implements Breusch-Godfrey test for serial correlation

**cointsmall/cointegration_test.py**
- `test_cointegration_breaks()`: Main testing function
- `CointegrationTestResult`: Result container class
- Grid search over possible break dates
- Supports 0, 1, or 2 structural breaks

**cointsmall/composite_test.py**
- `composite_cointegration_test()`: Automatic model selection
- `CompositeCointegrationResult`: Result container class
- Tests multiple model specifications
- Selects best model using decision rules from paper

**cointsmall/critical_values.py**
- `get_critical_value()`: Size-corrected critical values
- Surface response coefficients (fitted to match paper)
- Supports T ≥ 15, m ≤ 3, b ≤ 2

**cointsmall/verify.py**
- `verify_critical_values()`: Verify against Trinh (2022) Table 1
- `compare_critical_values_across_sample_sizes()`: Utility function

### Example Scripts

**examples/quick_start.py**
- Basic usage examples
- Step-by-step tutorial
- Demonstrates all main functions

**examples/comprehensive_examples.py**
- Seven detailed examples covering:
  1. Basic test without breaks
  2. Test with one break
  3. Test with two breaks
  4. Composite testing
  5. Critical values
  6. Verification
  7. Small sample analysis

### Documentation

**docs/API.md**
- Complete API documentation
- Function signatures and parameters
- Usage examples
- Return value descriptions
- Model specifications
- Limitations

**README.md**
- Package overview
- Installation instructions
- Quick start guide
- Citation information

## Installation

### From Source
```bash
cd cointsmall_python
pip install -e .
```

### Requirements
- numpy >= 1.19.0
- scipy >= 1.5.0
- statsmodels >= 0.12.0
- pandas >= 1.1.0

## Usage Examples

### Basic Test
```python
import numpy as np
from cointsmall import test_cointegration_breaks

np.random.seed(42)
T = 50
X = np.random.randn(T, 1)
Y = 2 + 1.5 * X[:, 0] + np.random.randn(T) * 0.3

result = test_cointegration_breaks(Y, X, n_breaks=0, model='o')
print(result)
```

### Composite Test
```python
from cointsmall import composite_cointegration_test

result = composite_cointegration_test(Y, X, max_breaks=2)
print(result)
result.summary()
```

### Critical Values
```python
from cointsmall import get_critical_value

cv = get_critical_value(T=30, m=1, b=1, model='cs')
print(f"Critical value: {cv:.4f}")
```

## Testing

Run quick start:
```bash
python examples/quick_start.py
```

Run comprehensive examples:
```bash
python examples/comprehensive_examples.py
```

Verify implementation:
```python
from cointsmall import verify_critical_values
verify_critical_values()
```

## Key Features

1. **Small Sample Optimization**: Designed for T < 50
2. **Structural Breaks**: Handles up to 2 endogenous breaks
3. **Size-Corrected Critical Values**: Based on surface response methodology
4. **Automatic Model Selection**: Composite testing procedure
5. **Multiple Model Types**: No breaks, intercept breaks, intercept+slope breaks
6. **Verified Implementation**: Matches critical values from Trinh (2022)

## Differences from R Package

This Python implementation closely follows the R package but has some differences:

1. **Syntax**: Python/NumPy syntax instead of R
2. **Dependencies**: Uses statsmodels instead of lmtest
3. **Result Objects**: Uses Python classes instead of R S3 objects
4. **Array Indexing**: 0-based indexing (Python) vs 1-based (R)

## References

Trinh, J. (2022). Testing for cointegration with structural changes in very 
small sample. THEMA Working Paper n°2022-01, CY Cergy Paris Université.

Gregory, A. W., & Hansen, B. E. (1996). Residual-based tests for cointegration 
in models with regime shifts. Journal of Econometrics, 70(1), 99-126.

MacKinnon, J. G. (1991). Critical values for cointegration tests. In Long-Run 
Economic Relationships: Readings in Cointegration, Chapter 13.

## License

GPL-3

## Author

- **Methodology**: Jérôme Trinh
- **R Package**: Dr. Merwan Roudane - Independent Researcher (merwanroudane920@gmail.com)
- **Python Port**: Based on R package version 0.1.1 by Dr. Merwan Roudane
