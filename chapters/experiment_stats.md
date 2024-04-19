# Statistics of online experiments {#sec-experiment-stats}

The goal of this chapter is to succinctly summarise the statistical theory of randomised experiments.


## Potential outcomes and outcome of interest

We have a population of units $i = 1, \dots, \N$. Each unit in the population can be exposed to one of two treatments, which are identical across units. Each unit $i$ has potential outcomes $\ycp$ and $\ytp$ corresponding to each of the two possible treatments. $\ycp$ is the outcome unit $i$ would experience if they received the control treatment; $\ytp$, the outcome they would experience if they received the active treatment. Given that each unit is either assigned to treatment or control we'll only ever observe one of these outcomes in practice. In fact, what we do observe for each unit is $\yio$, which equals $\ytp$ if the unit was assigned the active treatment and $\ycp$ if they were assigned the control treatment. That is, if we write $\ti_i = 1$ if unit $i$ is allocated to treatment and $\ti_i = 0$ if they are allocated to control, then we can express $\yio$ as

$$
\yio = \ti_i \ytp + (1 - \ti_i) \ycp.
$$

What's the use of potential outcomes we can only partially observe? They provide
us with a simple and coherent way to think about the causal effect of the
treatment; for unit $i$, that causal effect is given by

$$
\ytp - \ycp,
$$

which tells us how the outcome for that unit is different when given the
active treatment compared to the counterfactual state of the world where they
were given the control treatment. This is what we mean by the causal effect of
the treatment.

We are usually interested in the average causal effect of the treatment across
all units, which is given by the Average Treatment Effect (ATE)

$$
\te = \tefs = \tef.
$$ {#eq-ate}

This is the quantity we're trying to estimate in a typical experiment, though
other choices are possible.[^alternative_choices]


## Estimating the outcome of interest

Given that we only observe one potential outcome per unit, how can we estimate
@eq-ate?

In online experiments, we typically use simple random assignment to allocate
units to the expeirment sample and treatment variants (see
@sec-treatment-assignment for details). Random assignment to treatment implies
that

$$
\begin{align}
E[\ytp | \ti_i = 1] &= E[\ytp]\\
E[\ytp | \ti_i = 0] &= E[\ytp]
\end{align}
$$

That is: given that assignment is random, the expected outcome under treatment
is the same for units in the treatment and control group, and simply equals the
expected outcome under treatment across the entire population. The same is true
for expected outcomes under control, so that we have

$$
\begin{align}
E[\ycp | \ti_i = 1] &= E[\ycp]\\
E[\ycp | \ti_i = 0] &= E[\ycp]
\end{align}
$$

Now, expanding @eq-ate and using the above expressions we have:

$$
\begin{align}
\te &= \tef \\ 
&= E[\ytp] - E[\ycp] \\
&= E[\ytp | \ti_i = 1] - E[\ycp | \ti_i = 0],
\end{align}
$$

which says that we can express the true effect as the difference between the
expected outcomes of treated and untreated untis -- we have identified a way for
expressing the treatment effect in quantities we can actually estimate based on
the data we have available. In particular, the above suggests the following
estimation approach:

$$
\tee = \ytob - \ycob,
$$ {#eq-ate-est}

where

$$
\ytob = \ytobf \qquad \ycob = \ycobf.
$$

We can show that this is unbiased estimator of $\te$:[^alternative_proof]

$$
\begin{align}
E\left[\tee\right] &= E\left[\ytob - \ycob\right] \\
&=E\left[\ytob\right]- E\left[\ycob\right] \\
&=E\left[\ytobf\right] - E\left[\ycobf\right] \\
&=\frac{1}{\Nt}\sum_{i:\ti_i=1} E\left[\yto\right]
-\frac{1}{\Nc}\sum_{i:\ti_i=0} E\left[\yco\right] \\
&=\frac{\Nt}{\Nt}E\left[\yto\right] -\frac{\Nc}{\Nc}E\left[\yco\right] \\
&=E\left[\yto\right] - E\left[\yco\right] \\
&=E\left[\yio | \ti_i = 1\right] - E\left[\yio | \ti_i = 0\right] \\
&=E\left[\ytp\right] - E\left[\ycp\right] \\
&=\ytpb - \ycpb \\
&=\te
\end{align}
$$


## Variance of treatment effect estimates

Discussion in {#sec-treatment-assignment} important also for standard error. 

In
field experiments, we have dependence. As a result of this dependence, the derivation of the standard error is more complicated though it turns out that
formula we will derive below still holds approximately, since the
interdependence is small if the population from which experiment units are
sampled is much larger than the experiment sample.[^imbens-ref]

So let's think about the standard error for a typical online experiment from
first principles.

$$
\begin{align}
V\left[\tee\right] &= V\left[\ytob - \ycob\right] \\
&=V\left[\ytob\right] + V\left[\ycob\right] \\
&=V\left[\ytobf\right] + V\left[\ycobf\right] \\
&=\frac{1}{\Nt^2}\sum_{i:\ti_i=1} V\left[\yto\right]
+ \frac{1}{\Nc^2}\sum_{i:\ti_i=0} V\left[\yco\right] \\
&=\frac{\Nt}{\Nt^2}V\left[\yto\right] + \frac{\Nc}{\Nc^2}V\left[\yco\right] \\
&=\frac{1}{\Nt}V\left[\yio | \ti_i = 1\right] + \frac{1}{\Nc}V\left[\yio | \ti_i = 0\right] \\
&=\frac{1}{\Nt}V\left[\ytp\right] + \frac{1}{\Nc}V\left[\ycp\right] \\
&=\frac{1}{\Nt}V\left[\ytp\right] + \frac{1}{\Nc}V\left[\ycp\right] \\
&=\frac{\vt}{\Nt} + \frac{\vc}{\Nc} \\
\end{align}
$$


- In practice, we don't know variances. So need to estimate. We do this using
... (box with derivation). Which gives us...

- There are usually different representations of this

- Common assumption: same variance. Holds only if treatment effect is homogenous
  (box with proof) gives ...

- Often made assumption: same sample size gives ...

- We can also integrate treatment allocation proportion, which is very useful.
Gives us ...

...

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

[^imbens-ref]: See @imbens2015causal Section 6.7 and Appendix B of Chapter 6 for details.

[^alternative_choices]: Other choices are possible. We could define the
individual level treatment effect as the ratio of active and control treatment,
and we can create different summary statistics of the individual-level treatment
effects other than the average treatment effect over the entire population (see,
for instance, Chapter 1 in @imbens2015causal).

[^alternative_proof]: For an alternative proof, see the proof of Theorem 6.1 in @imbens2015causal.


[^tdetails]: Note that the test statistic follows a t-distribution because we have to estimate the variance (that is, if we replace the true variance with its estimate when standardising a normal variable, the result follows a Student's t-distribution). So, this has nothing to do with the CLT. However, for the test statistic to follow a student distribution, the numerator has to follow a normal distribution. Often, though, the underlying data is not normal, so that its approximately normal only for large enough samples, due to the CLT. At the same time, the t-distribution also converges to normal as the sample size increases. Hence, one we have a sample size large enough to justify using the t-distribution, we might as well use a z-test. As pointed out in Chapter 9 in @rice2006mathematical, the test statistic above only follows a t-distribution if we use the pooled variance, but for large sample sizes, the distribution is still approximately t or normal.


