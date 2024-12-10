# The stats of online experiments

## What we hope to learn

- The basic motivation behind a standard online experiment is the following ...

- We are generally interested in the effect of a universal policy -- a comparison between a state of the world where everyone is exposed to the treatment and one where nobody is. Also, while we can capture the difference between these two states of the world in many different ways, we typically focus on the difference in average outcomes.



## The potential outcomes framework

- The framework has three key features:

  1. Causal effects are associated with potential outcomes
  2. Studying causal effects required multiple units
  3. Central role of the assignment mechanism

  Their role is somewhat different, however: the first one is axiomatic: it's the starting point for how we think about causal effects and intimately linked to the notion that causal effects are always relative to a different state (see holland1986statistics notes, as well as Rubin interview). The second is a corollary from the first if we are unwilling to take the scientific solution (in Holland's words) to the Fundamental Problem: it's the insight that leads to the statistical solution. The third is a corollary of the second: to make the statistical solution work, the assignment mechanism is central.


- Let's start with a single individual unit, $i$, which is usually a user but could also be a device, geographical district, or something else.

- The binary treatment indicator $W_i \in \{0, 1\}$ indicates whether the individual is in treatment ($W_i = 1$) or control ($W_i = 0$).

- The key notion of causal inference in this framework is the potential for exposing each unit to cause or treatment (regardless of whether it's possible in practice) –– each unit needs to be potentially exposable to any of the causes.

- There is a potential outcome for each possible treatment: $Y_i(1)$ if $i$ is assigned to treatment and $Y_i(0)$ if $i$ is assigned to control.

- The causal effect of the treatment for individual $i$ is a comparison of the two potential outcomes, such as the difference $Y_i(1) - Y_i(0)$ or the ratio $Y_i(1)/Y_i(0)$.

- Once treatment is assigned, we observe

$$
Y_i^{obs} = Y_i(W_i) = \begin{cases} 
   Y_i(1) & \text{if } W_i = 1 \\
   Y_i(0)       & \text{if } W_i = 0
  \end{cases}
$$


- We can only ever observe one potential outcomes, which means that drawing inferences about the causal effect is impossible without additional assumptions. @holland1986statistics called this the fundamental problem of causal inference.

- An experiment is one way to solve the fundamental problem.


## Experiment setup

- The statistical solution to the Fundamental Problem is to rely on information from the entire experiment population and focus on the average treatment effect $\tau = \mathbb{E}[Y(1) - Y(0)] = \mathbb{E}[Y(1)] - \mathbb{E}[Y(0)]$.[^scientific_solution].

- The last two terms can be estimated from an experiment where some units are exposed to treatment and others to control. The key insight here is that the statistical approach makes it possible to replace the *impossible to observe* individual-level causal effect with the *possible to estimate* average causal effect over a population of units.

- We have a population of $i = 1, \dots, n$ units.

- The assignment indicator is now an $n$-vector $\mathbf{W}$ of assignments, with typical element $W_i$.

- In principle, the potential outcomes can depend on the treatments for all units, so that for each unit, we have $2^n$ potential outcomes $Y_i(\mathbf{W})$.

- Without further assumptions, an experiment would tell us the difference in the average outcomes of units in treatment and control, *given that precise assignment of the experiment*, which not help us estimate the effect of our universal policy.

- To make progress, we need the Stable Unit Treatment Value Assumption. SUTVA has two components: no interference, and no hidden variations of treatments.

  - The no interference assumption states that a unit's potential outcomes are independent of the treatment assignment of all other units.

  - The no hidden treatment variation states that a unit receiving a specific treatment level cannot receive different forms of that treatment level. This does *not* mean that the form of the treatment level has to be the same for each unit, but only that a given treatment level is well specified for a given unit. To use Imbens and Rubin's aspirin example: suppose we test the effect of aspirin on reducing headaches but have old and new aspirins which vary in strength, so that we effectively have three possible treatment statuses: no aspirin (control), weak aspirin, and strong aspirin. SUTVA does *not* require that all treatment units either get the weak or the strong aspirin, but requires that each unit can only receive one or the other in case they are treated, so that there is no ambiguity what form of the treatment a given unit will receive in case it is treated. (It would be permissible to have the treatment be randomly weak or strong, but this is not relevant in my world.) Remembering that what we want is the effect of a universal policy makes clear why this is important: we want to know what happened if we rolled out our policy to everyone compared to if we didn't roll it out to anyone. To have any hope of estimating this we can't have treatment level's vary over time or depending on circumstances, but need them to be pinned down for each unit. (In the context of Tech, this would mean that the experience of a feature for a given user is pinned down by, say, the size of their phone screen and the app version they use, which, by and large, is plausible.)

- Both parts of SUTVA ensure that the potential outcomes, $Y_i(W_i)$, are well defined for each individual (the "treatment value" in SUTVA refers to "potential outcomes"). The no interference part ensures that these outcomes do not depend on the assignment of other units, while the no hidden treatment variation ensures that the precise form of each treatment level that any given unit receives is clear, which then ensures that the potential outcome for that treatment is also well defined (in the aspirin example: if it weren't clear whether treatment meant weak or strong aspirin for unit $i$, then the value for $Y_i(1)$ may vary depending on which aspirin $i$ ends up receiving, which means that potential outcome isn't well defined).

- SUTVA is a strong assumption and can be violated in a number of ways. I'll discuss these, together with solutions, in @sec-threats-to-validity.

- If SUTVA holds, however, then instead of $Y_i(\mathbf{W})$ we have $Y_i(W_i)$, which allows us to write:

$$ Y_i^{obs} = W_iY_i(1) + (1 - W_i)Y_i(0)
$$ {#eq-yi}

- This is progress because now each unit's potential outcome is a function only of the unit's treatment assignment. As a result, the outcome we observe once the unit has been assigned, too, is a function of that unit's treatment assignment only.

- This is the precondition that allows us to compare outcomes of treated and untreated units to estimate the two quantities needed for the statistical solution to the Fundamental Problem: $\mathbb{E}[Y(1)] - \mathbb{E}[Y(0)]$.

- In order for these estimates to be valid estimates of the two quantities we need, it is critically important how units receive the treatment they receive.

- This is the role of the assignment mechanism: the mechanism that determines how units are allocated into different treatment conditions.

- **I'm here: chapt 3 and 4 in Imbens and Rubin**




**Estimand**

- We are generally interested in the effect of a universal policy -- a comparison between a state of the world where everyone is exposed to the treatment and one where nobody is. Also, while we can capture the difference between these two states of the world in many different ways, we typically focus on the difference in average outcomes.

- Hence, the estimand of interest (the theoretical quantity we try to estimate) is:

$$
\tau = \bar{Y}(1) - \bar{Y}(0),
$$

  where ...



**Identification**

- See Wagner notes for 4 assumptions: https://web.stanford.edu/~swager/stats361.pdf 

- ... Randomisation solves selection bias problem and allows us to identify treatment effect

- Use content from outcomes (expectations and show how randomisation eliminates selection bias)

- Randomisation

- SUTVA
  - No interference
  - Consistency
  - See deng2023first for reference to Rubin 1980 original article on precise assumption and other great Rubin references

- Solely and itself (excludability and non-interference)

- Ignorability

Check:
- duflo2006randomizationd
- Mostly harmless metrics
- Field experiments book
- Kohavi papers/book
- Imbens and Rubins

Question:
- You randomise at customer level. For analysis, you do the following: you calculate metrics at a restaurant level, then calculate variant level averages from the restaurant-level averages. Is there a problem? What is it? What assumptions are being violated? 


## Excludability

- Another key assumption, related to no hidden treatment variation, is that *assignment* to treatment affects outcomes only through the effect of the *administration* of the treatment -- being part of the treatment group does not have an effect on outcomes other than through the treatment itself.

- This could be violated if treatment units were somehow treated differently from control units (e.g. data collection was different)

- The assumption is called "excludability" because it assumes that we can exclude from the potential outcome definition separate indicators for treatment assignment and administration. Instead, throughout, we use the indicator $w_i$, which captures whether unit $i$ was allocated to treatment, and assume that this perfectly corresponds to having been administered the treatment.****




**Estimator**

- A natural estimator is ...

- We can write our treatment effect estimator, $\hat{\tau}$ in terms of the super-population as

$$
\hat{\tau} = \frac{1}{n_t}\sum_{i=1}^{N} R_i W_i Y_i - \frac{1}{n_c}\sum_{i=1}^{N} R_i (1 - W_i) Y_i
$$


**Unbiasedness of $\hat{\tau}$**

- First, note that using @eq-yi we can write:

$$
\begin{align}#
\frac{1}{n_t}\sum_{i=1}^{N} R_i W_i Y_i &= \frac{1}{n_t}\sum_{i=1}^{N} R_i W_i Y_i(1) \\
\frac{1}{n_c}\sum_{i=1}^{N} R_i (1 - W_i) Y_i &= \frac{1}{n_t}\sum_{i=1}^{N} R_i(1 - W_i) Y_i(0)
\end{align}
$$


::: {.callout-note collapse=true}

## Derivation

$$
\begin{align}
\frac{1}{n_t}\sum_{i=1}^{N} R_i W_i Y_i
&= \frac{1}{n_t}\sum_{i=1}^{N} R_i W_i \Bigl(W_i Y_i(1) + (1 - W_i) Y_i(0)\Bigr) \\
&= \frac{1}{n_t}\sum_{i=1}^{N} \Bigl(R_i W_i W_i Y_i(1) + R_i W_i (1 - W_i) Y_i(0)\Bigr) \\ 
&= \frac{1}{n_t}\sum_{i=1}^{N} R_i W_i W_i Y_i(1) \\ 
&= \frac{1}{n_t}\sum_{i=1}^{N} R_i W_i Y_i(1) \\ 
\frac{1}{n_c}\sum_{i=1}^{N} R_i (1 - W_i) Y_i
&= \frac{1}{n_t}\sum_{i=1}^{N} R_i (1 - W_i) \Bigl(W_i Y_i(1) + (1 - W_i) Y_i(0)\Bigr) \\
&= \frac{1}{n_t}\sum_{i=1}^{N} \Bigl(R_i(1 - W_i) W_i Y_i(1) + R_i(1 - W_i) (1 - W_i) Y_i(0)\Bigr) \\
&= \frac{1}{n_t}\sum_{i=1}^{N} R_i(1 - W_i) (1 - W_i) Y_i(0) \\
&= \frac{1}{n_t}\sum_{i=1}^{N} R_i(1 - W_i) Y_i(0)
\end{align}
$$

:::

- We can now show that $\hat{\tau}$ in unbiased, that $\E{\hat{\tau}} = \tau$.

- We have two sources of randomness, one due to random sampling and one due to random allocation to treatment. Using the law of iterated expectations, we can write:

$$
\E{\hat{\tau}} = \Esp{\EW{\hat{\tau}|R}}.
$$

::: {.callout-note collapse=true}
## Law of iterated expectations

- That is, we can first take the expectation over the randomisation distribution while talking the vector of sampling allocation indicators, $R$, as given, and then take the expectation over the sampling distribution.

$$
\begin{align}
...
\end{align}
$$

:::

- In both of these steps, we implicitly also condition on the vectors of potential outcomes in the super population, $Y_{sp}(0), Y_{sp}(1)$, which we consider fixed and take as given. I don't condition on these explicitly to keep the notation light.[^condition_on_pot_outcomes]

- TODO: condition on $Y$, as a shorthand. Adapt notation below. Also, consider using bf for vectors and matrices for clarity. Probably do it!

- The inner expectation is equal to:

$$
\begin{align}
\EW{\hat{\tau} | R}
&= \EW{\frac{1}{n_t}\sum_{i=1}^{N} R_i W_i Y_i - \frac{1}{n_c}\sum_{i=1}^{N} R_i (1 - W_i) Y_i \>\Bigg|\> R} \vs
&= \EW{\frac{1}{n_t}\sum_{i=1}^{N} R_i W_i Y_i(1) - \frac{1}{n_c}\sum_{i=1}^{N} R_i (1 - W_i) Y_i(0) \>\Bigg|\> R} \vs
&= \EW{\sum_{i=1}^{N} R_i \Biggl(\frac{W_i Y_i(1)}{n_t} - \frac{(1 - W_i) Y_i(0)}{n_c}\Biggr)\>\Bigg|\> R} \vs
&= \sum_{i=1}^{N} R_i \EW{\frac{W_i Y_i(1)}{n_t} - \frac{(1 - W_i) Y_i(0)}{n_c}} \vs
&= \sum_{i=1}^{N} R_i \Biggl(\frac{\EW{W_i} Y_i(1)}{\EW{n_t}} - \frac{(1 - \EW{W_i}) Y_i(0)}{\EW{n_c}}\Biggr) \vs
&= \sum_{i=1}^{N} R_i \Biggl(\frac{q Y_i(1)}{Nq} - \frac{(1 - q) Y_i(0)}{N(1-q)}\Biggr) \vs
&= \sum_{i=1}^{N} R_i \Biggl(\frac{Y_i(1)}{N} - \frac{Y_i(0)}{N}\Biggr) \vs
&= \frac{1}{N}\sum_{i=1}^{N} R_i \bigl(Y_i(1) - Y_i(0)\bigr) \vs
&= \tau_{fs}
\end{align}
$$

- The outer expectation is equal to:

$$
\begin{align}
\E{\hat{\tau}} 
&= \Esp{\EW{\hat{\tau}|R}} \\
&= \Esp{\tau_{fs}} \\
&= \Esp{\frac{1}{N}\sum_{i=1}^{N} R_i \bigl(Y_i(1) - Y_i(0)\bigr)} \\
&= \frac{1}{\Esp{N}}\sum_{i=1}^{N} \Esp{R_i} \bigl(Y_i(1) - Y_i(0)\bigr) \\
&= \frac{1}{Np}\sum_{i=1}^{N} p \bigl(Y_i(1) - Y_i(0)\bigr) \\
&= \frac{1}{N}\sum_{i=1}^{N}\bigl(Y_i(1) - Y_i(0)\bigr) \\
&= \tau
\end{align}
$$


**Variance of $\hat{\tau}$**

- Using the law of total variance[^law_of_total_variance], we can write $\V{\hat{\tau}}$ as

$$
\begin{align}
\V{\hat{\tau}}
&= \Esp{\VW{\hat{\tau} | R}} + \Vsp{\EW{\hat{\tau} | R}}
\end{align}
$$


## Super-population perspective

- So far, we have focused on the case where the $n$ units in the experiment sample are the population of interest.

- In online experiments, we might start with a ramp-up of 1%. Does this mean we have to consider a super-population perspective for these cases? As in, do we have to adjust the standard error? How much do SEs differ in practice?

- How to go about this: 1) establish whether or not super-population approach is required, 2) is so, compare FS and SP standard errors to check whether it makes a difference. Write up regardless to have a good theoretical foundation. But if I'm lucky then using SP SEs makes a material difference in practice, in which case this would be interesting to publish and use at work.


**Old notes on super-population**

- Online experiments typically go through a ramp-up phase: they include only a small fraction of users at the start and all users at the end.

- Statistically, this means we have to consider two different cases. In the first case, during the early stages of an experiment, we use a sample of the entire user population to learn something about that population as a whole; in this case, the sample we work with and the sample we want to learn something about are different. In the second case, when the entire user population is part of the experiment, the sample we work with and the sample we want to learn something about are the same. Following @imbens2015causal, I refer to the first approach as the super-population perspective and the second case the finite sample perspective. 

- We have a (super) population of $N$ users. In the example I'm going to use throughout, these are all of our iOS-app users in the UK.

- From this super population, we sample $n$ users to be part of the experiment, and then allocate $n_t$ users to treatment and $n_c$ users to control.

- The way we sample users into the experiment and allocate them to treatment has implications for our statistical analysis, so let's have a look at the details.

- Online experiments usually use the following **sampling** approach to determine whether a user is part of an experiment:

  1. Create a hash string unique to each user such as `<user_id><experiment_id><market>`.

  2. Feed the hash string into a hash algorithm (often MD5) and receive a hash value.

  3. Use the hash value to determine whether a user is part of the experiment. Say we allocate 10% of traffic to the experiment. We then include the user only if their hash value falls within the bottom (or top) 10% of possible hash values.

- With this approach, the probability that a user is sampled into the experiment is independent of the sampling decisions of all other users. Each of our $N$ users is part of the experiment experiment with probability $n/N$ and we write $R_i = 1$ if user $i$ is part of the experiment sample and $R_i = 0$ if they aren't.[^conditioning_on_n]


[^conditioning_on_n]: For each user in the super population, being part of the experiment sample is a [Bernoulli trial](https://en.wikipedia.org/wiki/Bernoulli_trial) with $R_i \sim \text{Bernoulli}(n/N)$ and, hence, $\E{R_i} = n/N$ and $\V{R_i} = n/N(1-n/N)$. I assume here that we know $n$. The reason for doing so is twofold. First, it makes the math easier as it spares us from modeling $n$ as a Binomial random variable. Second, by the time we analyse the data, we do know $n$.


[^dependent_sampling]: This is easiest to see in contrast to experiments where neither of these
decisions are independent, as is often the case in lab and field experiments in
social science, but also medical experiments. There, we typically recruit a
pre-determined number of units into our experiment, so that the inclusion of any
given unit lowers the probability of inclusion for all others. Similarly, for
treatment assignment, we would often use a completely randomised assignment, whereby we ensure that exactly $N_t$ units end up in the treatment group. This, again means that assigning any given unit to treatment lowers the probability of receiving the treatment for all other units.


- The total number of users in the sample is $n = \sum_{i = 1}^{N}R_i$.

- Each of the $n$ users in our sample is allocated to the treatment condition with probability $q$, and we write $W_i = 1$ if user $i$ is in the treatment group and $W_i = 0$ if they are in the control group.

- The total number of users in the treatment group is $n_t = \sum_{i = 1}^{N} W_i$, and the total number of users in the control group is $n_c = \sum_{i = 1}^{N} (1 - W_i)$.

- Given this setup, we have:
$$
\begin{align}
\E{R_i} &= p \\
\E{W_i} &= q \\
\E{n} &= Np \\
\E{n_t} &= nq \\
\E{n_c} &= n(1 - q) \\
\end{align}
$$

  (we will use this in the unbiasedness proof below)

::: {.callout-note collapse=true}
## Details

- For each user in the super population, being part of the experiment sample is a [Bernoulli trial](https://en.wikipedia.org/wiki/Bernoulli_trial), as is being part of the treatment group for each user in the experiment sample.

$$
\begin{align}
R_i \sim \text{Bernoulli}(p) \quad &\text{with} \quad \E{R_i} = p \\
W_i \sim \text{Bernoulli}(q) \quad &\text{with} \quad \E{W_i} = q
\end{align}
$$

:::




## References


[^scientific_solution]: @holland1986statistics discusses two solutions to the Fundamental Problem: one is the scientific solution described in the main text, the other is the scientific solution, which uses homogeneity or invariance assumptions. Say we measure a unit's outcome under treatment now, and have measured their outcome under control beforehand. If we're prepared to assume that the earlier control measurement equals the control measurement we would have taken now had we not exposed the unit to treatment – that earlier and later control measurements are homogenous and invariant to time – then we can calculate the individual level causal effect by comparing the two measurements taken at different points in time. Our assumption is untestable, of course, but in lab experiments it is sometimes possible to make a strong case that it is plausible. It is also the approach we informally use in daily life, whenever we conclude that taking Paracetamol helps against headaches or that going to sleep early makes us feel better the next morning.



[^condition_on_pot_outcomes]: If we were to explicitly condition on potential outcomes, we'd get:
  $$
  \begin{align}
  \E{\hat{\tau}}
  &=\Esp{\EW{\hat{\tau}|R, Y_{sp}(0), Y_{sp}(1)} | Y_{sp}(0), Y_{sp}(1)}
  \end{align}
  $$


[^law_of_total_variance]: In general, the [Law of total variance](https://en.wikipedia.org/wiki/Law_of_total_variance) states that:
  $$
  \begin{align}
  \V{Y} = \E{\V{Y|X}} + \V{\E{Y|X}}
  \end{align}
  $$
  In our case here, conditioning on $R$ means that we take the expectation or variance over the randomisation distribution, which I make explicit with the subscript $W$. The unconditional expectation or variance is taken over the randomisation distribution, which I make explicit using the subscript $sp$. As in the unbiasedness proof above, we are also implicitly conditioning on potential outcomes and I omit making this explicit to keep the notation lighter. Making the conditioning explicit would mean we apply the law to a conditional variance, for which the logic would still hold, and we'd write:
  $$
  \begin{align}
  \V{\hat{\tau} | Y_{sp}(0), Y_{sp}(1)}
  &= \Esp{\VW{\hat{\tau} | R, Y_{sp}(0), Y_{sp}(1)} | Y_{sp}(0), Y_{sp}(1)} \\
  &+ \Vsp{\EW{\hat{\tau} | R, Y_{sp}(0), Y_{sp}(1)} | Y_{sp}(0), Y_{sp}(1)}
  \end{align}
  $$




