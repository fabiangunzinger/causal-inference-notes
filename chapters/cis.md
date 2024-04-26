# Confidence intervals {#sec-cis}

## Hypothesis testing

To test whether the observed treatment effect is significantly different from zero, we test:

$$
H_0: \bar{Y}^{obs}_t = \bar{Y}^{obs}_c
H_A: \bar{Y}^{obs}_t \neq \bar{Y}^{obs}_c.
$$

We calculate the test-statistic

$$
T = \frac{\hat{\tau}}{\sqrt{Var(\hat{\tau})}} \sim t_{(N_t + N_c - 2)},
$$

where $N_t + N_c - 2$ is number of degrees of freedom[^tdetails].

todo:

- See Rice 6.2 on why this follows t distribution
- For complete treatment and derivation of sampling distributions (incl. discussion of all the approximations and sample corrections), see Rice sampling chapter and my ipad notes.

