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


