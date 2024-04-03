# Variance of the treatment effect estimate 

Here I want to write down carefully everything converning variance.

- Simplest case with variance known, equal, and independent assignments

- Relax known assumption

- Relax equal variance assumption

- Relax independent assignment assumption






[^vardetails] 

We gloss over a few details here. Depending on the treatment assignment mechanism, units are not independently assigned. In online experiments, we often use hash functions for treatment assignment, in which case assignment is independent. But f

If, instead of using a Bernoulli trial assignment mechanism we use a *completely randomised experiment*, where we perfectly balance the number of units assigned to each treatment, then the variance estimator above is not necessarily unbiased. In such an experiment, assignments are not independent because each unit being assigned to one unit lowers the probability of all other units of being assigned to that same variant. 

, each unit being assigned to one variant lowers the probability of all other units being assigned to that same variant. In that case, the above variance estimator is unbiased only if the treatment effect is constant. However, it is usually used in practice even in cases where constant treatment effects are unlikely because it is conservative (i.e. at least as large as the true variance) and because it is always unbiased if the ATE is an estimate of the infinite super-population ATE.

