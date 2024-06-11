# Standard error {#sec-standard-error}

- In this section, we'll derive the standard error of our treatment effect estimator $\tee$.

- Our treatment effect estimate, $\hat{\tau}$, is a random variable because sampling and
treatment assignment are random.

- This means that if we were to repeat the same experiment many times we'd get a slightly different value for $\hat{\tau}$ each time.

- The distribution of all these values is called the sampling distribution of $\tee$. 

- We know a few things about that distribution. From the central limit theorem we know that its shape is Normal (see @sec-stats-foundations). Above we have shown above that the distribution has mean $\te$, which means our estimator is unbiased. Naturally, the distribution also has a standard deviation. Because it is a sampling distribution, that standard deviation is called the standard error. But it is still a standard deviation, and is thus defined as the square root of the variance. 

- We'll thus find the standard error as follows: we first derive the variance of the treatment estimate, then find a way to estimate that variance, and then take the square root of that estimate to get the standard error.


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
V\left(\tee\right) &= V\left(\teef\right) \\
&=V\left(\yotb\right) + V\left(\yocb\right) \\
&=V\left(\yotbf\right) + V\left(\yocbf\right) \\
&=\frac{1}{\Nt^2}\sum_{i:\tii=1} V\left(\yoi\right)
+ \frac{1}{\Nc^2}\sum_{i:\tii=0} V\left(\yoi\right) \\
&=\frac{\Nt}{\Nt^2}V\left(\yoi | \tii = 1\right) + \frac{\Nc}{\Nc^2}V\left(\yoi | \tii = 0\right) \\
&=\frac{1}{\Nt}V\left(\yoi | \tii = 1\right) + \frac{1}{\Nc}V\left(\yoi | \tii = 0\right) \\
&=\frac{1}{\Nt}V\left(\ypt\right) + \frac{1}{\Nc}V\left(\ypc\right) \\
&=\frac{\vt}{\Nt} + \frac{\vc}{\Nc},
\end{align}
$$

where

$$
\vt ≡ V\left(\ypt\right) \quad \vc ≡ V\left(\ypc\right),
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
\boxed{\se = \sefu}
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
\se = \sqrt{\frac{\vpe + \vpe}{\N/2}} = \sqrt{\frac{4\vpe}{\N}} = \sefe
$$

For most of the text, I'll use this expression for the standard error. In some
cases, though, it is useful to express the standard error in terms of the
proportion of units allocated to the treatment group. Hence, instead of assuming
equal sample sizes, we use $P$ to denote that proportion and $\N$ to denote
total sample size, while maintaining the assumption of equal variance. After a little algebraic manipulation we then get:

$$
\se = \sqrt{\frac{\vpe}{P\N} + \frac{\vpe}{(1-P)\N}} = \sefep.
$$

Notice that for equal sample sizes, when $P=0.5$, this formulation is equivalent
to the one above as expected.



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


