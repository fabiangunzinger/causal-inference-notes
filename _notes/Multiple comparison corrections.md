[[_Experimentation]]

TOC
- [[#Approaches|Approaches]]
- [[#Industry approaches|Industry approaches]]

--- 
## Approaches

### Bonferroni Correction

**Key Idea**: The Bonferroni method controls the family-wise error rate (FWER) by dividing the significance level (α) by the number of hypotheses (m). This ensures that the chance of making one or more Type I errors is minimized across all tests.

- **Formula**: Adjusted p-value = original p-value * m
- **Advantages**: Simple, robust, and widely applicable.
- **Disadvantages**: Highly conservative, especially with large numbers of hypotheses, leading to a loss of statistical power (more false negatives).

**Key Paper**: Dunn, O. J. (1961). Multiple Comparisons Among Means. _Journal of the American Statistical Association_.

---
### Holm-Bonferroni Method

**Key Idea**: A sequentially rejective version of the Bonferroni method, which adjusts p-values stepwise, starting with the smallest.

- **Advantages**: Less conservative than Bonferroni while still controlling FWER.
- **Disadvantages**: Still conservative with a large number of hypotheses, though less so than Bonferroni.

**Key Paper**: Holm, S. (1979). A Simple Sequentially Rejective Multiple Test Procedure. _Scandinavian Journal of Statistics_.

---

### Benjamini-Hochberg (BH) Procedure

**Key Idea**: Controls the expected proportion of false discoveries (false positives) among rejected hypotheses. It’s more relaxed than controlling the FWER, making it less conservative and better suited for large-scale testing.

- **Advantages**: Increased statistical power compared to Bonferroni, suitable for large datasets.
- **Disadvantages**: Less strict control of Type I errors, may allow for more false positives.

**Key Paper**: Benjamini, Y., & Hochberg, Y. (1995). Controlling the False Discovery Rate: A Practical and Powerful Approach to Multiple Testing. _Journal of the Royal Statistical Society_.

---

#### Benjamini-Yekutieli (BY) Procedure

**Key Idea**: An extension of the BH procedure that controls the FDR in scenarios with correlated tests, offering a more conservative approach than BH.

- **Advantages**: Suitable for dependent tests, as it accounts for correlations.
- **Disadvantages**: More conservative than the BH method, leading to reduced power in highly correlated tests.

**Key Paper**: Benjamini, Y., & Yekutieli, D. (2001). The Control of the False Discovery Rate in Multiple Testing under Dependency. _The Annals of Statistics_.

---

### More advanced methods

- Westfall-Young Permutation Method:
	- **Key Idea**: Uses resampling techniques to empirically calculate adjusted p-values. This non-parametric approach is ideal for complex datasets where traditional assumptions may not hold.
	- **Advantages**: Provides exact control over error rates, especially effective with small sample sizes.
	- **Disadvantages**: Computationally expensive, especially with large datasets or numerous hypotheses.
	- **Key Paper**: Westfall, P. H., & Young, S. S. (1993). Resampling-Based Multiple Testing: Examples and Methods for p-Value Adjustment. _Wiley_.
- Hierarchical Hypothesis Testing
	- **Key Idea**: Focuses on groups of hypotheses, adjusting for MHT within hierarchically structured families of tests. It starts with a global null hypothesis and proceeds to test smaller clusters of hypotheses based on the outcome.
	- **Advantages**: Balances FWER control with increased power in some specific areas of interest.
	- **Disadvantages**: Complex to design and interpret, depends heavily on correct hypothesis clustering.
	- **Key Paper**: Goeman, J. J., & Solari, A. (2011). Multiple testing for exploratory research. _Statistical Science_.


## Industry approaches

- Statsig provides optional MHT correction. For each experiment, users can apply either [Bonferroni](https://docs.statsig.com/stats-engine/methodologies/bonferroni-correction) or [Benjamini-Hochberg](https://docs.statsig.com/stats-engine/methodologies/benjamini%E2%80%93hochberg-procedure) corrections either per group or metric or both

![[Screenshot 2024-09-16 at 11.08.21.png|400]]
