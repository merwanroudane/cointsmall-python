# Credits and Attribution

## Cointsmall Python Package

This is a Python implementation of the R package "cointsmall" for cointegration testing with structural breaks in very small samples.

## Contributors

### Original Methodology
**Jérôme Trinh**  
- Affiliation: THEMA, CY Cergy Paris Université
- Email: jerome.trinh@ensae.fr
- Contribution: Developed the statistical methodology and theoretical framework
- Publication: Trinh, J. (2022). Testing for cointegration with structural changes in very small sample. THEMA Working Paper n°2022-01, CY Cergy Paris Université.

### R Package Implementation
**Dr. Merwan Roudane**  
- Status: Independent Researcher
- Email: merwanroudane920@gmail.com
- Contribution: Implemented the original R package "cointsmall" (version 0.1.1)
- Repository: https://github.com/merwanroudane/cointsmall
- Role: Creator and Maintainer of the R package

### Python Port
This Python implementation is based on Dr. Merwan Roudane's R package (version 0.1.1), translating the functionality from R to Python while maintaining full compatibility with the original methodology.

## Citation

### Primary Citation (Methodology)
When using this package for research, please cite the original methodology:

```bibtex
@techreport{trinh2022testing,
  title={Testing for cointegration with structural changes in very small sample},
  author={Trinh, Jérôme},
  year={2022},
  institution={THEMA Working Paper n°2022-01, CY Cergy Paris Université},
  url={http://thema.u-cergy.fr/IMG/pdf/2022-01.pdf}
}
```

### R Package Citation
If you specifically use features from the R implementation, also cite:

```bibtex
@manual{roudane2025cointsmall,
  title={cointsmall: R package for cointegration testing with structural breaks in very small samples},
  author={Roudane, Merwan},
  year={2025},
  note={R package version 0.1.1},
  url={https://github.com/merwanroudane/cointsmall}
}
```

### Python Package Citation
```bibtex
@software{cointsmall_python,
  title={cointsmall: Python implementation},
  year={2025},
  note={Python port of R package by Dr. Merwan Roudane},
  url={https://github.com/yourusername/cointsmall-python}
}
```

## License

This Python package maintains the same GPL-3 license as the original R package.

```
GNU General Public License v3.0

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
```

## Acknowledgments

- **Jérôme Trinh** for developing the statistical methodology
- **Dr. Merwan Roudane** for implementing the R package and making it available
- The R community for the original statistical computing framework
- Contributors to NumPy, SciPy, and statsmodels which made this Python port possible

## Contact

For questions about:
- **Methodology**: Contact Jérôme Trinh (jerome.trinh@ensae.fr)
- **R Package**: Contact Dr. Merwan Roudane (merwanroudane920@gmail.com)
- **Python Port**: Refer to the repository or contact the maintainer

## Version History

- **0.1.0** (2025): Initial Python port based on R package version 0.1.1
- Based on R package version 0.1.1 by Dr. Merwan Roudane
- Based on methodology from Trinh (2022)

## Related Work

### Original Paper
Trinh, J. (2022). Testing for cointegration with structural changes in very small sample. 
THEMA Working Paper n°2022-01, CY Cergy Paris Université.

### R Package
Roudane, M. (2025). cointsmall: R package for cointegration testing with structural 
breaks in very small samples. R package version 0.1.1.

### Foundational References
- Gregory, A. W., & Hansen, B. E. (1996). Residual-based tests for cointegration in models with regime shifts. *Journal of Econometrics*, 70(1), 99-126.
- MacKinnon, J. G. (1991). Critical values for cointegration tests. In *Long-Run Economic Relationships: Readings in Cointegration*, Chapter 13.

---

**Note**: This Python package is an independent implementation that faithfully reproduces the functionality of Dr. Merwan Roudane's R package, which itself implements the methodology developed by Jérôme Trinh. All three contributors deserve credit for making this work available to the research community.
