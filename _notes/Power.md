[[_Experimentation]]

## Theory

- lift from causal inference book

## Calculating power in online experiments

- The theory for power calculation was developed for metrics with fixed values such as hight or weight.

- (During an experiment, the treatment will still change the metric values, but in practice we often make the sensible assumption that the treatment effect will be small, so that the variance between treatment and control are the same. This, in turn, then justifies use of pre-experiment data under the assumption that pre-experiment and experiment data will be very similar.)

- In online experiments, we often experiment with metrics that are only defined for a specific period of time (e.g. conversion during a 1-month period starting on 15 March 2024).

- This makes power calculation more complicated.

- When calculating required sample size (and/or experiment duration) for an experiment we want to make sure that a Z-test performed at the end of the experiment with the required number of unique units has a certain pre-specified level of power.

- To calculate that required sample size we input a baseline metric value and the metric standard deviation.

- With metrics defined only for specific periods, how to calculate these two values is not straightforward.

- Let's see what we generally do when a metric value is fixed. 

- Actually, writing this and thinking of an example for the above makes me think that this might be an issue inherent to causal inference analysis. 

- An example where we don't have the problem is if we want to compare the height of Londoners to the height of Berliners. Here, we'd do the following:

	- Draw a random sample of Londoners and measure mean and variance of their heights.
	- Do the same for a random sample of Berliners.
	- Perform a Z-test and calculate its power.

- Writing the above makes me realise that the issue is inherent in ex-ante power calculations:
	- Even in the Londoners and Berliners height example above we'd run into the same problem if we wanted to calculate, before taking any samples, how many samples we'd have to take to have our Z-test be adequately powered.

- The problem arises once we rearrange the power formula from

$$
1 - \beta = f(\sigma^2, \delta, P, z_\alpha, z_{1-\beta})
$$
to
$$
N = \frac{z_\alpha + z_{1-\beta}}{P(1-P)}\frac{\sigma^2}{\delta^2}
$$
- Because we would use the first version at the time we perform the analysis when we have all the required inputs, whereas we perform the second one before the analysis when we have to estimate $\sigma$ and $\delta$.

- The core of the problem is that for many online experiment metrics baseline metric mean and variance change depending on (1) the size of the sample they are calculated from and (2) the period of time and period location they are calculated based on.

- (1) is always the case, even in the Londoners and Berliners example above. It's inherent in performing power calculations.

- (2) is an additional complications in many online experiments. The two components are period length and period location (i.e. do we measure period of length $t$ in January of September).

- Outside of periods that are non-representative because of seasonality reasons, ignoring period location should usually not be a big problem.

- However, period duration might make a difference.

- So, the core problem is that in online experiments, in addition to approximating the sample we calculate metrics based on we also have to approximate the time period.


- How big a difference does calculating means and stds based on different time periods make? The difference can be substantial. The below table shows means and std for order visit conversion for a set of UK users based on different period lengths.

![[order-conversion-visit-different-periods.png|300]]

- Required sample size is directly proportional to the sample variance, which means that using the variance based on one week instead of 1 month of data would increase required sample size by a factor of $\frac{0.36^2}{0.31^2} = 1.35$.

- How hard is it to decently estimate an appropriate time-period? There are two parts we have to estimate: required number of unique units, and how long it takes to gather data from these many units.

- The required number of units is determined by:
	- Metric value mean (for experiment-period-length long period)
	- Metric value variance (for experiment-period-length long period)

- To amount of time it takes us to gather data for the required number of units depends on traffic to the precise point of the user-funnel/app where the bucketing for the experiment takes place.


Solution:
- To ensure that analysis is correctly powered, calculate power every day and stop once adequately powered.
- If you want ex-ante guidance, use sensible approximations.

- First best: to know when analysis is sufficiently powered, calculate power daily and stop experiment when required level of power reached. This ensures that we have both (1) sample we use for analysis and (2) period used for analysis.

- Second best, if we performed power using data from, say, the first 7-days of the experiment period, we would have a subset of (1) and could intelligently estimate (2) because the observed traffic would take into account the bucketing point and we could estimate future traffic based on it (e.g. we can estimate unique user visits based on unique visits during first week, with different traffic being the result of different bucketing points, but we can estimate path for all bucketing points).

- Third best, if we want to perform power calculation before the experiment starts (i.e. because we want to provide duration estimate during experiment config), we could use data from recent history (e.g. calculated monthly), and calculated separately for each metric, market, and based on other relevant dimensions such as different time period. Though, here, taking into account bucketing points might be challenging and hard to scale. So think about good approximations.

## Calculating power at scale




Extensions
- [Power Analysis for Experiments with Clustered Data, Ratio Metrics, and Regression for Covariate Adjustment](https://arxiv.org/abs/2406.06834) -- hesterberg2024power




