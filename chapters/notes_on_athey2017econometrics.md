# Notes on athey2017econometrics

## Introduction

- While experiments avoid many issues with observational studies, challenges remain:

  - How to perform inference even in simples case with homogenous and independent subjects when we compare sample means?

  - How to design experiment and account for imbalances if there are observed differences in characteristics between treatment groups?

  - How do results generalise? (E.g. estimate heterogeneous treatment effects or rebalance)

  - How to deal with lack of independence in presence of network effects?


- Authors recommend to rely on randomisation-based rather than sampling-based approach to analyse experiments

  - Sampling based:

      - Also model-based (why?)

      - This is the classical mode of inference in statistics and observational studies 

      - Randomness results from random sampling.

      - We assume that the population at hand is a random subsample of a (much) larger population, so that individual values are random.

      - For instance, in $\bar{X} = \frac{1}{n}\sum_{i=1}^{n}X_i$ we treat each $X_i$ as a random variable.

      - In the context of experimentation, where we can write the treatment group mean as $\bar{Y}_t = \frac{1}{n_t}\sum_{i=1}^{n}W_iY_i$, we treat the $W_i$s as fixed and $Y_i$s as random ("for each reserved slot in the treatment group, what is the value of the unit we randomly selected for that slot?")

  - Randomisation based:

    - Randomness results from random treatment assignment.

    - In the context of experimentation, where we can write the treatment group mean as $\bar{Y}_t = \frac{1}{n_t}\sum_{i=1}^{n}W_iY_i$, we treat the $W_i$s as random and $Y_i$s as fixed ("Out of all $n$ units with fixed potential outcomes that we have in our experiment sample, which ones got randomly allocated to the treatment group?")


## Randomised experiments and validity

- Definition of a randomised experiment: (i) assignment independent of observed and unobserved individual characteristics and (ii) assignment is in the control of the researcher.

- The special role of randomisation:

  - Randomisation is special because it gives the researcher unique control over the assignment mechanisms and thus offers the possibility to eliminate selection bias when comparing treatment and control group (randomisation eliminates selection bias on observables and unobservables).

  - Read about this more in depth. Start with articles cited in athey2017econometrics section 2.1, and then also read Deaton & Cartwright article(s) for opposing perspective.

- Notes on validity are in `threats_to_validity.md`.


## The potential outcomes framework

- The framework has three key features:

  1. Causal effects are associated with potential outcomes
  2. Studying causal effects required multiple units
  3. Central role of the assignment mechanism


- We have a population of $i = 1, \dots, N$ units.

- For each unit, $i$, the binary treatment indicator $W_i \in \{0, 1\}$ indicates whether the individual is in treatment ($W_i = 1$) or control ($W_i = 0$).

- There is a potential outcome for each possible treatment: $Y_i(1)$ is the outcome for $i$ if they are assigned to treatment; $Y_i(0)$, if they are assigned to control.

- The causal effect of the treatment for individual $i$ is a comparison of the two potential outcomes such as the difference $Y_i(1) - Y_i(0)$ or the ration $Y_i(1)/Y_i(0)$.

- Once treatment is assigned, we observe

$$
Y_i^{obs} = Y_i(W_i) = \begin{cases} 
   Y_i(1) & \text{if } W_i = 1 \\
   Y_i(0)       & \text{if } W_i = 0
  \end{cases}
$$


- We can only ever observe one potential outcomes, which means that drawing inferences about the causal effect is impossible without additional assumptions. @holland1986statistics called this the fundamental problem of causal inference.





// I'm here: read holland1986statistics and integrate 

- In the context of all $N$ units, we have an N-vector $\mathbf{W}$ of assignments, with typical element $W_i$.

- In principle, the potential outcomes can depend on the treatments for all units, so that for each unit, we have $2^N$ potential outcomes $Y_i(\mathbf{W})$.










- 
- Each unit in the population can be exposed to one of two treatments, which are identical across units. Each unit $i$ has potential outcomes $\ypc$ and $\ypt$ corresponding to each of the two possible treatments. $\ypc$ is the outcome unit $i$ would experience if they received the control treatment; $\ypt$, the outcome they would experience if they received the active treatment.


Each unit is either assigned to treatment or control, so we'll only ever observe one of their potential outcomes. We denote the observed outcome for unit $i$ as $\yo$. This observed outcome equals $\ypt$ if the unit was assigned to treatment and $\ypc$ if they were assigned control. That is, if we write $\ti_i = 1$ if unit $i$ is allocated to treatment and $\ti_i = 0$ if they are allocated to control, then we can express the **observed outcome** for unit $i$ as

