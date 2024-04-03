# Statistics of online experiments {#sec-experiment-stats}

The goal of this chapter is to succinctly summarise the statistical theory of randomised experiments.


## Potential outcomes and outcome of interest

We have a population of units $i = 1, \dots, \N$. Each unit in the population can be exposed to one of two treatments, which are identical across units, so that $\mathbb{T}_i = \mathbb{T} = \{0, 1\}$, where $\mathbb{T}_i = 1$ indicates that unit $i$ receives the active treatment and $\mathbb{T}_i = 0$ indicates that they receive the control treatment.

Each unit $i$ has potential outcomes $\ycp$ and $\ytp$ corresponding to each of the two possible treatments. $\ycp$ is the outcome unit $i$ would experience if they were assigned to the control group; $\ytp$, if they were assigned to the active treatment. Given that each unit is either assigned to treatment or control we'll only ever observe one of these outcomes in practice. In fact, what we do observe for each unit is $\yio$, which equals $\ytp$ if the unit was assigned the active treatment and $\ycp$ if they were assigned the control treatment.

But the insight that both of potential outcomes exist at a conceptual level is
the foundation of the potential outcomes approach. The reason these outcomes are
important is that they allow us to coherently think about causal effects -- the
difference in the state of the world under the active and the control treatment.
The individual-level treatment effect is given by

$$
\ytp - \ycp,
$$

and the average treatment effect (ATE) over the entire population is defined as
the average difference in individual outcomes[^alternative_choices]

$$
\te = \tefs = \tef.
$$ {#eq-ate}

This is the outcome we usually care about in an online experiment.


## Treatment effect estimates

We don't observe potential outcomes, so we can't estimate Equation @eq-ate
directly. 

Our estimate of the average treatment effect is

$$
\hat{\tau} = \bar{Y}^{obs}_t - \bar{Y}^{obs}_c,
$$

where

$$
\bar{Y}_t^{obs} = \frac{1}{N_t}\sum_{i:W_i=1} Y_i^{obs} \qquad \bar{Y}_c^{obs} = \frac{1}{N_c}\sum_{i:W_i=0} Y_i^{obs}.
$$

This is an unbiased estimate of $\tau = \bar{Y(1)} - \bar{Y(0)}$ (see Proof of Theorem 6.1 in @imbens2015causal).

## Assignment mechanism

In online experiments, units usually get allocated to treatment variants based
on a hash function <!-- (see @sec-treatment-assignment) -->. The basic proceedure is
simple: we concatenace information such as the unit and experiment ID, hash it,
and check where the resulting hash value lies on the range of possible hash
values. We might then allocate the unit into control if the hash value falls
below the midpoint and into treatment otherwise.

The assignment mechanism for each unit is thus akin to a Bernoulli trial, with
probability of treatment equal to $p$. 


## Variance of treatment effect estimates

Cases to discuss: 


- Simplest case with variance known, equal, and independent assignments (derive
  from first principles)

- Relax known assumption

- Relax equal variance assumption

- Relax independent assignment assumption

- Discuss population vs sample perspective

- Show derivation for using treatment proportion


For most of the text, I'll rely on the assumption of equal variance because it
simplifies notation and is justified in the context of online experiments
because of randomisation, large sample sizes, and (generally) small treatment effects. 

Hence, my standard sampling variance is:

$$
\sve = \svefe
$$

and the standard error is:

$$
\see = \seefe
$$



Notes to integrate:


Because our Bernoulli assignment mechanism allocates treatment and control units independently and randomly, an unbiased estimate of the sampling variance of $\hat{\tau}$ is given by:

$$
\vtees = \vtee
$$

where

$$
s_c^2 = \frac{1}{N_c - 1}\sum_{i:W_i=0}\left(Y_i(0) - \bar{Y}_c^{obs}\right)^2 \qquad s_t^2 = \frac{1}{N_t - 1}\sum_{i:W_i=1}\left(Y_i(1) - \bar{Y}_t^{obs}\right)^2.
$$


[^vardetails] 

We gloss over a few details here. Depending on the treatment assignment mechanism, units are not independently assigned. In online experiments, we often use hash functions for treatment assignment, in which case assignment is independent. But f

If, instead of using a Bernoulli trial assignment mechanism we use a *completely randomised experiment*, where we perfectly balance the number of units assigned to each treatment, then the variance estimator above is not necessarily unbiased. In such an experiment, assignments are not independent because each unit being assigned to one unit lowers the probability of all other units of being assigned to that same variant. 

, each unit being assigned to one variant lowers the probability of all other units being assigned to that same variant. In that case, the above variance estimator is unbiased only if the treatment effect is constant. However, it is usually used in practice even in cases where constant treatment effects are unlikely because it is conservative (i.e. at least as large as the true variance) and because it is always unbiased if the ATE is an estimate of the infinite super-population ATE.




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

## Assumptions 

### Stable unit treatment value assumption (SUTVA)

- SUTVA has two components: no interference, and no hidden variations of treatments.

 **No interference**

- The no interference assumption states that a unit's potential outcumes are independent of the treatment assignment of all other units.

- This will be violated if there are network effects: if the behaviour of units is mutually dependent. For instance: if my wife and I both use an online photo-sharing service and my wife sees a new feature that we both like while I'm in the control group, we might stil share the same number of family photos but start sharing them all on her account instead of mine. This creates an artificial treatment effect because if I had also had access to the new feature, we might not have changed our behaviour at all, while, during the experiment, her sharing volume went up while mine went down, suggesting the existent of a positive effect.

- Another case where the no interference assumption can be violated is in the form of general equilibrium effects. A classic example is the effect of further education: the effect of my doing a PhD in statistics on my earnings while nobody else changes their behaviour (the partial-equilibrium effect) is surely different from the outcome of my earnings if suddenly everyone decided to do a PhD in statistics (the general-equilibrium effect).

- The two violations capture the two different ways interference can lead to incorrect results: interference can happen and bias our results either during the experiment or once the feature is fully rolled out. In either case, the treatment of some unit has an externality on other units.

**No hidden treatment variations**

- The second component, no hidden treatment variation, states that a unit receiving a specific treatment level cannot receive different forms of that treatment level. This does *not* mean that the form of the treatment level has to be the same for each unit, but only that a given treatment level is well specified for a given unit. To use Imbens and Rubin's aspirin example: suppose we test the effect of aspirin on reducing headaches but have old and new aspirins which vary in strength, so that we effectively have three possible treatment statuses: no aspirin (control), weak aspirin, and strong aspirin. SUTVA does *not* require that all treatment units either get the weak or the strong aspirin, but requires that each unit can only receive one or the other in case they are treated, so that there is no ambiguity what form of the treatment a given unit will receive in case it is treated. (It would be permissible to have the treatment be randomly weak or strong, but this is not relevant in my world.)

- Essentially, both parts of SUTVA ensure the same thing: that $Y_i(w)$ is well defined: that it does not depend on the treatment status of other units, and that, for each possible treatment level, $w$, the precise form of that treatment level is well specified.

## How does randomisation help us estimate ATEs?

By ensuring that the treatment - the causal variable of interest - is independent of potential outcomes, so that control and treatment group are comparable.

More technically, it ensures that expected outcomes are the same in both groups, which means that the selection bias - the difference of expected potential outcomes without treatment - disappears. When using regression, this is equivalent to the error term being uncorrelated with treatment status.


## Finite sample vs super-population perspective

There are two ways to perform inference:

- When using the finite sample perspective, the $N$ units in the experiment sample are treated as the entire population of interest. Hence, there is no notion of randomisation due to sampling from a larger population, and all the randomness in the outcomes is due to randomness generates by the assignment mechanism.

- When treating the $N$ units in the sample as a random sample from a larger super-population, then in addition to randomness from the randomisation, we also have randomness from the sampling.


[^alternative_choices]: Other choices are possible. We could define the
individual level treatment effect as the ratio of active and control treatment,
and we can create different summary statistics of the individual-level treatment
effects other than the average treatment effect over the entire population (see,
for instance, Chapter 1 in @imbens2015causal).


[^tdetails]: Note that the test statistic follows a t-distribution because we have to estimate the variance (that is, if we replace the true variance with its estimate when standardising a normal variable, the result follows a Student's t-distribution). So, this has nothing to do with the CLT. However, for the test statistic to follow a student distribution, the numerator has to follow a normal distribution. Often, though, the underlying data is not normal, so that its approximately normal only for large enough samples, due to the CLT. At the same time, the t-distribution also converges to normal as the sample size increases. Hence, one we have a sample size large enough to justify using the t-distribution, we might as well use a z-test. As pointed out in Chapter 9 in @rice2006mathematical, the test statistic above only follows a t-distribution if we use the pooled variance, but for large sample sizes, the distribution is still approximately t or normal.


