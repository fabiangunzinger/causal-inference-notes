# Outcomes {#sec-outcomes}

## Potential outcomes

We have a population of units $i = 1, \dots, \N$. Each unit in the population can be exposed to one of two treatments, which are identical across units. Each unit $i$ has potential outcomes $\ypc$ and $\ypt$ corresponding to each of the two possible treatments. $\ypc$ is the outcome unit $i$ would experience if they received the control treatment; $\ypt$, the outcome they would experience if they received the active treatment.


Each unit is either assigned to treatment or control, so we'll only ever observe one of their potential outcomes. We denote the observed outcome for unit $i$ as $\yo$. This observed outcome equals $\ypt$ if the unit was assigned to treatment and $\ypc$ if they were assigned control. That is, if we write $\ti_i = 1$ if unit $i$ is allocated to treatment and $\ti_i = 0$ if they are allocated to control, then we can express the **observed outcome** for unit $i$ as

$$
\yo = \ti_i \ypt + (1 - \ti_i) \ypc.
$$ {#eq-yo}


## Effect of interest

What's the use of potential outcomes we can only partially observe? They provide
us with a simple and coherent way to think about the causal effect of the
treatment; for unit $i$, the **individual causal effect** is given by

$$
\ypt - \ypc,
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
E[\ypt | \ti_i = 1] &= E[\ypt]\\
E[\ypt | \ti_i = 0] &= E[\ypt]
\end{align}
$$

That is: given that assignment is random, the expected outcome under treatment
is the same for units in the treatment and control group, and simply equals the
expected outcome under treatment across the entire population. The same is true
for expected outcomes under control, so that we have

$$
\begin{align}
E[\ypc | \ti_i = 1] &= E[\ypc]\\
E[\ypc | \ti_i = 0] &= E[\ypc]
\end{align}
$$

Now, expanding @eq-ate and using the above expressions we have:

$$
\begin{align}
\te &= \tef \\ 
&= E[\ypt] - E[\ypc] \\
&= E[\ypt | \ti_i = 1] - E[\ypc | \ti_i = 0],
\end{align}
$$

which says that we can express the true effect as the difference between the
expected outcomes of treated and untreated untis -- we have identified a way for
expressing the treatment effect in quantities we can actually estimate based on
available data. In particular, the above suggests the following
estimation approach:

$$
\tee = \teef
$$ {#eq-ate-est}

where

$$
\yotb= \yotbf \qquad \yocb = \yocbf.
$$

We can show that this is an unbiased estimator of $\te$:[^alternative_proof]

$$
\begin{align}
E\left[\tee\right] &= E\left[\yotb - \yocb\right] \\
&=E\left[\yotb\right]- E\left[\yocb\right] \\
&=E\left[\yotbf\right] - E\left[\yocbf\right] \\
&=\frac{1}{\Nt}\sum_{i:\ti_i=1} E\left[\yoi\right]
-\frac{1}{\Nc}\sum_{i:\ti_i=0} E\left[\yoi\right] \\
&=\frac{\Nt}{\Nt}E\left[\yoi|\tii=1\right]
-\frac{\Nc}{\Nc}E\left[\yoi|\tii=0\right] \\
&=E\left[\yoi|\tii=1\right] - E\left[\yoi|\tii=0\right] \\
&=E\left[\ypt\right] - E\left[\ypc\right] \\
&=\yptb - \ypcb \\
&=\te
\end{align}
$$



## Assumptions

## Stable unit treatment value assumption (SUTVA)

- SUTVA has two components: no interference, and no hidden variations of treatments.

 **No interference**

- The no interference assumption states that a unit's potential outcumes are independent of the treatment assignment of all other units.

- This will be violated if there are network effects: if the behaviour of units is mutually dependent. For instance: if my wife and I both use an online photo-sharing service and my wife sees a new feature that we both like while I'm in the control group, we might stil share the same number of family photos but start sharing them all on her account instead of mine. This creates an artificial treatment effect because if I had also had access to the new feature, we might not have changed our behaviour at all, while, during the experiment, her sharing volume went up while mine went down, suggesting the existent of a positive effect.

- Another case where the no interference assumption can be violated is in the form of general equilibrium effects. A classic example is the effect of further education: the effect of my doing a PhD in statistics on my earnings while nobody else changes their behaviour (the partial-equilibrium effect) is surely different from the outcome of my earnings if suddenly everyone decided to do a PhD in statistics (the general-equilibrium effect).

- The two violations capture the two different ways interference can lead to incorrect results: interference can happen and bias our results either during the experiment (threat to internal validity) or once the feature is fully rolled out (threat to external validity). In either case, the treatment of some unit has an externality on other units.

**No hidden treatment variations**

- The second component, no hidden treatment variation, states that a unit receiving a specific treatment level cannot receive different forms of that treatment level. This does *not* mean that the form of the treatment level has to be the same for each unit, but only that a given treatment level is well specified for a given unit. To use Imbens and Rubin's aspirin example: suppose we test the effect of aspirin on reducing headaches but have old and new aspirins which vary in strength, so that we effectively have three possible treatment statuses: no aspirin (control), weak aspirin, and strong aspirin. SUTVA does *not* require that all treatment units either get the weak or the strong aspirin, but requires that each unit can only receive one or the other in case they are treated, so that there is no ambiguity what form of the treatment a given unit will receive in case it is treated. (It would be permissible to have the treatment be randomly weak or strong, but this is not relevant in my world.)

- Another way in which this aspect of SUTVA can be violated is when treatments are administered in different ways, e.g. by either giving patients medication or asking them to take the medication themselves.

- Essentially, both parts of SUTVA ensure the same thing: that $Y_i(w)$ is well defined: that it does not depend on the treatment status of other units, and that, for each possible treatment level, $w$, the precise form of that treatment level is well specified.


## Excludability

- Another key assumption, related to no hidden treatment variation, is that *assignment* to treatment affects outcomes only through the effect of the *administration* of the treatment -- being part of the treatment group does not have an effect on outcomes other than through the treatment itself.

- This could be violated if treatment units were somehow treated differently from control units (e.g. data collection was different)

- The assumption is called "excludability" because it assumes that we can exclude from the potential outcome definition separate indicators for treatment assignment and administration. Instead, throughout, we use the indicator $w_i$, which captures whether unit $i$ was allocated to treatment, and assume that this perfectly corresponds to having been administered the treatment.