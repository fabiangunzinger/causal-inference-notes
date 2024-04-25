# Statistics of online experiments {#sec-experiment-stats}

The goal of this chapter is to succinctly summarise the statistical theory of randomised experiments.

Most online experiments appear very simple; we split traffic into two groups with
different experiences and compare outcomes between groups. So how much
statistical theory could we possibly need?

Well, to experiment effectively, you do want to make sure you have

1. a coherent definition of the causal effect effect you want to measure and a
   good way of estimating it,

2. a way to differentiate signals from noise,

3. a way to ensure your experiment has a good chance of picking up signals.

First two are covered here. The third, which relates to the power of your
experiment, is covered in @sec-power.


## Potential outcomes and outcome of interest

We have a population of units $i = 1, \dots, \N$. Each unit in the population can be exposed to one of two treatments, which are identical across units. Each unit $i$ has potential outcomes $\ycp$ and $\ytp$ corresponding to each of the two possible treatments. $\ycp$ is the outcome unit $i$ would experience if they received the control treatment; $\ytp$, the outcome they would experience if they received the active treatment. Given that each unit is either assigned to treatment or control we'll only ever observe one of these outcomes in practice. In fact, what we do observe for each unit is $\yio$, which equals $\ytp$ if the unit was assigned the active treatment and $\ycp$ if they were assigned the control treatment. That is, if we write $\ti_i = 1$ if unit $i$ is allocated to treatment and $\ti_i = 0$ if they are allocated to control, then we can express $\yio$ as

$$
\yio = \ti_i \ytp + (1 - \ti_i) \ycp.
$$ {#eq-yio}

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
\boxed{\te = \tefs = \tef}
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
available data. In particular, the above suggests the following
estimation approach:

$$
\boxed{\tee = \ytob - \ycob}
$$ {#eq-ate-est}

where

$$
\ytob = \ytobf \qquad \ycob = \ycobf.
$$

We can show that this is an unbiased estimator of $\te$:[^alternative_proof]

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


## Standard error of treatment effect estimate

In this section, we'll derive the standard error of our treatment effect
stimator $\tee$.

Our treatment effect estimate, $\tee$, is a random variable because sampling and
treatment assignment are random. This means that if we were to repeat the sampe
experiment many times we'd get a slightly different value for $\tee$ each time.
The distribution of all these values is called the sampling distribution of
$\tee$. We know a few things about that distribution. From the central limit
theorem we know that its shape is Normal (see @sec-stats-foundations). Above we
have shown above that the distribution has mean $\te$, which means our estimator
is unbiased. Naturally, the distribution also has a standard deviation. Because it
is a sampling distribution, that standard deviation is called the standard
error. But it is still a standard deviation, and is thus defined as the square
root of the variance. We'll thus find the standard error as follows: we first
derive the variance of the treatment estimate, then find a way to estimate that
variance, and then take the square root of that estimate to get the standard
error.


### Treatment effect estimate variance

The way we sample units into our experiment and assign them to treatment groups
has important implications for the variance. For the estimation of the treatment
effect above, the main implication of the simple random sample proceedure
commonly used for online experiments (see chapter @sec-treatment-assignment) was
that the expectation of potential ourcomes for treatment and control groups were
identical. For the derivation of the variance and the standard error, the main
implication is that sampling and treatment assignment between units are
independent in the sense that one unit being sampled or assigned to a treatment
condition doesn't affect other units' sampling or assignment
probabilities.[^dependence_case]

Given this independence property, let's think about the standard error for a typical online experiment from
first principles.

$$
\begin{align}
V\left(\tee\right) &= V\left(\ytob - \ycob\right) \\
&=V\left(\ytob\right) + V\left(\ycob\right) \\
&=V\left(\ytobf\right) + V\left(\ycobf\right) \\
&=\frac{1}{\Nt^2}\sum_{i:\ti_i=1} V\left(\yto\right)
+ \frac{1}{\Nc^2}\sum_{i:\ti_i=0} V\left(\yco\right) \\
&=\frac{\Nt}{\Nt^2}V\left(\yto\right) + \frac{\Nc}{\Nc^2}V\left(\yco\right) \\
&=\frac{1}{\Nt}V\left(\yio | \ti_i = 1\right) + \frac{1}{\Nc}V\left(\yio | \ti_i = 0\right) \\
&=\frac{1}{\Nt}V\left(\ytp\right) + \frac{1}{\Nc}V\left(\ycp\right) \\
&=\frac{1}{\Nt}V\left(\ytp\right) + \frac{1}{\Nc}V\left(\ycp\right) \\
&=\frac{\vt}{\Nt} + \frac{\vc}{\Nc},
\end{align}
$$

where

$$
\vt ≡ V\left(\ytp\right) \quad \vc ≡ V\left(\ycp\right),
$$

is the (true) population variance in the treatment and control group,
respectively.

### Estimating the treatment effect estimate variance

In practice, we don't know these variances, so we estimate them
using 

$$
\vte = \vtef \quad \vce = \vcef,
$$

from which we get

$$
\sve = \svefu.
$$

This is the variance of our treatment effect estimate. For statistical testing,
the construction of confidence intervals, and for power analysis we work with
the standard errors. We'll derive these next.

### Standard error of treatment effect estimate

As discussed above, the standard error is simply the standard deviation of the
sampling distribution of $\tee$, defined as the square root of the sampling variance, and is thus defined as:

$$
\boxed{\se = \seefu}
$${#eq-se}

We could work with this, and sometimes do. But in the context of online
experiments, because sample sizes are so large and treatment effects are usually
small, people often assume equal sample sizes and variances, so that we have
$\Nt = \Nc = N/2$ and $\vte = \vce = \vpe$. The common variance $\vpe$ is
estimated by "pooling" $\vte$ and $\vce$ to create a degrees-of-freedom-weighted
estimator of the form:

$$
\vpe = \vpef.
$$

Substituting all of the above in @eq-se results in 

$$
\se = \sqrt{\frac{\vpe + \vpe}{\N/2}} = \sqrt{\frac{4\vpe}{\N}} = \seefe
$$

For most of the text, I'll use this expression for the standard error. In some
cases, though, it is useful to express the standard error in terms of the
proportion of units allocated to the treatment group. Hence, instead of assuming
equal sample sizes, we use $P$ to denote that proportion and $\N$ to denote
total sample size, while maintaining the assumption of equal variance. After a little algebraic manipulation we then get:

$$
\se = \sqrt{\frac{\vpe}{P\N} + \frac{\vpe}{(1-P)\N}} = \seefp.
$$

Notice that for equal sample sizes, when $P=0.5$, this formulation is equivalent
to the one above as expected.


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
    individual level treatment effect as the ratio of active and control
    treatment, and we can create different summary statistics of the
    individual-level treatment effects other than the average treatment effect
    over the entire population (see, for instance, Chapter 1 in
    @imbens2015causal).

[^alternative_proof]: For an alternative proof, see the proof of Theorem 6.1 in
    @imbens2015causal.

[^dependence_case]: When we sample units without replacement and use a
    completely randomised experiment as the assignment mechanism, this is not
    true. As a result, the derivation of the standard error is more complicated
    though it turns out that formula we derive here is still commonly used. The reason is twofold: if treatment errors are constant, then the estimator is unbiased even in the more complex case. If not, then the estimator is conservative compared to one that takes the interaction from the complete randomisation into account. Furthermore, the expression is valid approximately ....

    still holds approximately,
    since the interdependence is small if the population from which experiment
    units are sampled is much larger than the experiment sample. For more
    details, See @imbens2015causal Section 6.7 and Appendix B of Chapter 6. 

[^additive-effects]: For homogenous additive treatment effects, variances are approximately equal regardless of the effect size. 

[^tdetails]: Note that the test statistic follows a t-distribution because we
    have to estimate the variance (that is, if we replace the true variance
    with its estimate when standardising a normal variable, the result follows
    a Student's t-distribution). So, this has nothing to do with the CLT.
    However, for the test statistic to follow a student distribution, the
    numerator has to follow a normal distribution. Often, though, the
    underlying data is not normal, so that its approximately normal only for
    large enough samples, due to the CLT. At the same time, the t-distribution
    also converges to normal as the sample size increases. Hence, one we have a
    sample size large enough to justify using the t-distribution, we might as
    well use a z-test. As pointed out in Chapter 9 in @rice2006mathematical,
    the test statistic above only follows a t-distribution if we use the pooled
    variance, but for large sample sizes, the distribution is still
    approximately t or normal.


