# Neyman's repeated sampling approach {#sec-neyman}

These are my notes from reading chapter 6 in @imbens2015causal.

## Estimator for the average treatment effect

In a setting with $i = 1, \dots, N$ units with fixed potential outcomes $Y_i(0)$ and $Y_i(1)$, where the only random component is the random assignment, captured by the assignment vector $W$[^setting], Neyman was interested in the population average treatment effect:

$$
\tau_{fs} = \frac{1}{N}\sum_{i=1}^N \left(Y_i(1) - Y_i(0)\right) = \bar{Y}(1) - \bar{Y}(0),
$$ {#eq-neyman-estimand}

where

$$
\bar{Y}(1) = \frac{1}{N}\sum_{i=1}^N Y_i(1) \qquad \bar{Y}(0) = \frac{1}{N}\sum_{i=1}^N Y_i(0).
$$

This is our estimand of interest.

If we have data from a completely randomised experiment in which $N_t = \sum_{i=1}^N W_i$ units are allocated to treatment and the remaining $N_c = \sum_{i=1}^N (1-W_i)$ to control, then a natural estimator for @eq-neyman-estimand is the difference in the averages of the treatment and control units:

$$
\hat{\tau}^{dif} = \bar{Y}_t^{obs} - \bar{Y}_c^{obs}.
$$ {#eq-neyman-estimator}

where

$$
\bar{Y}_t^{obs} = \frac{1}{N_t}\sum_{i:W_i=1} Y_i^{obs} \qquad \bar{Y}_c^{obs} = \frac{1}{N_c}\sum_{i:W_i=0} Y_i^{obs}
$$

This estimator is unbiased (see Proof of Theorem 6.1 in @imbens2015causal for the proof).


## Estimator of the variance of the average treatment effect estimator

Estimating the variance of the average treatment estimator $\hat{\tau}^{dif}$ involves two steps:

1. Derive the sampling variance of the estimator for the average treatment effect (i.e. for the estimator defined in @eq-neyman-estimator).

2. Develop estimators for this sampling variance.

The sampling variance of $\hat{\tau}^{dif}$ is (see Theorem 6.2 in @imbens2015causal):

$$
\mathbb{V}_W \left(\bar{Y}_t^{obs} - \bar{Y}_c^{obs}\right)
= \frac{S_c^2}{N_c} + \frac{S_t^2}{N_t} - \frac{S_{ct}^2}{N},
$$ {#eq-neyman-sampvar}

where:

$$
\begin{align}
S_c^2 &= \frac{1}{N - 1}\sum_{i=1}^{N}\left(Y_i(0) - \bar{Y}(0)\right)^2 \\
S_t^2 &= \frac{1}{N - 1}\sum_{i=1}^{N}\left(Y_i(1) - \bar{Y}(1)\right)^2 \\
S_{ct}^2 &= \frac{1}{N - 1}\sum_{i=1}^{N}\left(Y_i(1) - Y_i(0) - (\bar{Y}(1) - \bar{Y}(0))\right)^2 \\
&= \frac{1}{N - 1}\sum_{i=1}^{N}\left(Y_i(1) - Y_i(0) - \tau_{fs}\right)^2 \\
\end{align}
$$

If the unit level treatment effects $Y_(1) - Y_i(0)$ are constant, then the below is an unbiased estimator for the sampling variance (see Theorem 6.3 in @imbens2015causal):

$$
\hat{\mathbb{V}}^{neyman} = \frac{s_c^2}{N_c} + \frac{s_t^2}{N_t},
$$ {#eq-neyman-sampvar-est}

where:

$$
s_c^2 = \frac{1}{N_c - 1}\sum_{i:W_i=0}\left(Y_i(0) - \bar{Y}_c^{obs}\right)^2 \qquad s_t^2 = \frac{1}{N_t - 1}\sum_{i:W_i=1}\left(Y_i(1) - \bar{Y}_t^{obs}\right)^2
$$

There are other estimators, but $\hat{\mathbb{V}}^{neyman}$ is the most commonly used because:

- It is conservative (because it ignores the last term in @eq-neyman-sampvar)

- It is always an unbiased estimator of @eq-neyman-sampvar under the super-population perspective

## Further notes

- The Neyman approach can incorporate discrete covariates by partitioning sample into subgroups, calculating subgroup treatment effects, and aggregating the subgroup treatment effects using a subgroup-size weighted average.

- However, it cannot handle cases where there are covariate values for which only treatment or control units are observed. In this case, we need to build a model for potential outcomes (e.g. by using regression analysis).


[^setting]: Note that this is the same setting as in [Fisher's approach](fisher.qmd)