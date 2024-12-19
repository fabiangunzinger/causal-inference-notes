# Different causal estimands

## Causal estimands

We can generalise the standard ATE calculation in a number of ways.

- We can focus only on a subset of the population, which can also happen in different ways.

- We can condition on covariates, such as when we focus only on women:
$$
\tau_{fs, f} = \frac{1}{N_f}\sum_{i: X_i = f} \left(Y_i(1) - Y_i(0)\right), \quad \text{where $X_i = \{m , f\}$ and $N_f = \sum_{i=1}^N \mathbb{1}_{X_i = f}$}
$$

- We can condition on treatment status, such as when we focus only on units that were exposed to the treatment: 

$$
\tau_{fs, t} = \frac{1}{N_t}\sum_{i: W_i = 1} \left(Y_i(1) - Y_i(0)\right), \quad \text{where $W_i = \{0 , 1\}$ and $N_t = \sum_{i=1}^N \mathbb{1}_{W_i = 1}$}
$$

- We can condition on potential outcomes, such as when we focus only on units with positive potential outcomes (e.g. positive earnings) regardless of treatment status:

$$
\tau_{fs, pos} = \frac{1}{N_{pos}}\sum_{i: Y_i(0)>0, Y_i(1)>0} \left(Y_i(1) - Y_i(0)\right), \quad \text{where $N_{post} = \sum_{i=1}^N \mathbb{1}_{Y_i(0)>0, Y_i(1)>0}$}
$$

- We can also generalise the estimand by focusing on more general functions of the potential outcomes (e.g. we may focus on the median outcome of the entire population or a subpopulation).

- In all these cases, we can write the causal estimand as a row-exchangeable function (a function that takes vectors or matrices as arguments and the result of which does not change if the rows in its input are permuted):

$$
\tau = \tau(Y(0), Y(1), X, W)
$$


## Quantile treatment effects

- Diff in quantiles between T and C observed outcome distributions, not quantiles of $Y_i(1) - Y_i(0)$.

- see 4.3 in athey2017econometrics



## Treatment effects

ATE is the average difference in potential outcomes of all subjects. E[y1 - y0]

ATE is a weighted average of ATET and average treatment effect of untreated.

ATE is also a weighted average of the compliers, always-takers, and never-takers.

ATE = ATET if treatment effects are homogenous (if they are not, then experiment measures ATET).

ATE = ITT under homogenous effects or under perfect compliance.


ATET (or TOT) is the average difference in potential outcomes of treated subjects. E[y1 - y0 | D=1] (D is treatment)

ATET = LATE in an experiment with no always-takers. This is relevant because there are many cases of onesided non-compliance (if participants who are randomised to treatment do not take it up but nobody who wasn't randomised to treatment has access).


ITT is the average difference in potential outcomes of those assigned to treatment (a weighted average between those who accepted treatment and those who didn't).

LATE is the average difference in potential outcomes of compliers.

