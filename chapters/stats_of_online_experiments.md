# The stats of online experiments

## The potential outcomes framework and the fundamental problem of causal inference

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

- If SUTVA holds, however, then instead of $Y_i = Y_i(\mathbf{W})$ we have $Y_i = Y_i(W_i)$, which allows us to write:

$$ Y_i^{obs} = W_iY_i(1) + (1 - W_i)Y_i(0)
$$ {#eq-yi}

- This is progress because now each unit's potential outcome is a function only of the unit's treatment assignment. As a result, the outcome we observe once the unit has been assigned, too, is a function of that unit's treatment assignment only.

- This is the precondition that allows us to compare outcomes of treated and untreated units to estimate the two quantities needed for the statistical solution to the Fundamental Problem: $\mathbb{E}[Y(1)] - \mathbb{E}[Y(0)]$.

- In order for these estimates to be valid estimates of the two quantities we need, it is critically important how units receive the treatment they receive.

- This is the role of the assignment mechanism: the mechanism that determines how units are allocated into different treatment conditions.

## Assignment in online experiments


### Bernoulli randomised experiment (BRE)

- The assignment mechanism of a BRE is individualistic, probabilistic, and unconfounded. In the simplest case without stratification, it is also independent of covariates. In all cases, the assignment mechanism is fully under our control. For probability of treatment assignment $q$, we thus have:

$$
P(\mathbf{W} | \mathbf{X}, \mathbf{Y}(1), \mathbf{Y}(0)) = P(\mathbf{W}) = q^{n_t} (1-q)^{n_c}
$$

****I'm here****

- Reading Wager, it seems there are two relevant factors for inference: he just conditions on n to get a CRE, and then there is the question of whether to take a finite sample or super-population perspective. 

- The additional assumption (discussed in population asymptotics) of random sampling from super population holds for online experiments.

- He does use Bernoulli sampling, which is what I need for online experiments. I just don'f fully understand how his perspective fits into the Imbens Rubin book / Athey Imbens one. 

- Also, use my notes in Obsidian. There is a lot there.


## Assumptions

- SUTVA

- Then we also require randomised assignments. In online experiments, as least, this is not an assumption if we properly test the randomisation proceedure (see discussion of SRM in @sec-threats-to-validity)

Other related assumptions (not needed in online experiments, but discuss briefly)
- Ignorability
- Excludability
	- Another key assumption, related to no hidden treatment variation, is that *assignment* to treatment affects outcomes only through the effect of the *administration* of the treatment -- being part of the treatment group does not have an effect on outcomes other than through the treatment itself.
	
	- This could be violated if treatment units were somehow treated differently from control units (e.g. data collection was different)
	
	- The assumption is called "excludability" because it assumes that we can exclude from the potential outcome definition separate indicators for treatment assignment and administration. Instead, throughout, we use the indicator $w_i$, which captures whether unit $i$ was allocated to treatment, and assume that this perfectly corresponds to having been administered the treatment.

Check:
- See Wagner notes for 4 assumptions: https://web.stanford.edu/~swager/stats361.pdf 
- duflo2006randomizationd
- Mostly harmless metrics
- Field experiments book
- Kohavi papers/book
- Imbens and Rubins

Question:
- You randomise at customer level. For analysis, you do the following: you calculate metrics at a restaurant level, then calculate variant level averages from the restaurant-level averages. Is there a problem? What is it? What assumptions are being violated? 


## Estimand

- We are generally interested in the effect of a universal policy -- a comparison between a state of the world where everyone is exposed to the treatment and one where nobody is. Also, while we can capture the difference between these two states of the world in many different ways, we typically focus on the difference in average outcomes.

- Hence, the estimand of interest (the theoretical quantity we try to estimate) is:

$$
\tau = \bar{Y}(1) - \bar{Y}(0),
$$

  where ...



# Neyman's repeated sampling approach

See separate note



****


## References


## Footnotes

[^scientific_solution]: @holland1986statistics discusses two solutions to the Fundamental Problem: one is the statistical solution described in the main text, the other is the scientific solution, which uses homogeneity or invariance assumptions. Say we measure a unit's outcome under treatment now, and have measured their outcome under control beforehand. If we're prepared to assume that control measurements are homogenous and invariant to time -- that the earlier control measurement equals the control measurement we would have taken now had we not exposed the unit to treatment -- then we can calculate the individual level causal effect by comparing the two measurements taken at different points in time. Our assumption is untestable, of course, but in lab experiments it is sometimes possible to make a strong case that it is plausible. It is also the approach we informally use in daily life, whenever we conclude that taking Paracetamol helps against headaches or that going to sleep early makes us feel better the next morning.



