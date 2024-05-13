# Outcomes {#sec-outcomes}

## Potential outcomes

We have a population of units $i = 1, \dots, \N$. Each unit in the population can be exposed to one of two treatments, which are identical across units. Each unit $i$ has potential outcomes $\ycp$ and $\ytp$ corresponding to each of the two possible treatments. $\ycp$ is the outcome unit $i$ would experience if they received the control treatment; $\ytp$, the outcome they would experience if they received the active treatment.


Each unit is either assigned to treatment or control, so we'll only ever observe one of their potential outcomes. We denote the observed outcome for unit $i$ as $\yio$. This observed outcome equals $\ytp$ if the unit was assigned to treatment and $\ycp$ if they were assigned control. That is, if we write $\ti_i = 1$ if unit $i$ is allocated to treatment and $\ti_i = 0$ if they are allocated to control, then we can express the **observed outcome** for unit $i$ as

$$
\yio = \ti_i \ytp + (1 - \ti_i) \ycp.
$$ {#eq-yio}


## Effect of interest

What's the use of potential outcomes we can only partially observe? They provide
us with a simple and coherent way to think about the causal effect of the
treatment; for unit $i$, the **individual causal effect** is given by

$$
\ytp - \ycp,
$$

which tells us how the outcome for that unit is different when given the
active treatment compared to the counterfactual state of the world where they
were given the control treatment. This is what we mean by the causal effect of
the treatment.

We are usually interested in the average causal effect of the treatment across
all units, which is given by the **average treatment effect (ATE)**

$$
\te = \tefs = \tef
$$ {#eq-ate}

This is the quantity we're trying to estimate in a typical experiment (the estimand), though
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

