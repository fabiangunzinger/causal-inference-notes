# Experiment details

## Finite sample perspective

## Super-population perspective



## Modes of inference

Sampling based:

- Also model-based (why?)

- This is the classical mode of inference in statistics and observational studies 

- Randomness results from random sampling.

- We assume that the population at hand is a random subsample of a (much) larger population, so that individual values are random.

- For instance, in $\bar{X} = \frac{1}{n}\sum_{i=1}^{n}X_i$ we treat each $X_i$ as a random variable.

- In the context of experimentation, where we can write the treatment group mean as $\bar{Y}_t = \frac{1}{n_t}\sum_{i=1}^{n}W_iY_i$, we treat the $W_i$s as fixed and $Y_i$s as random ("for each reserved slot in the treatment group, what is the value of the unit we randomly selected for that slot?")


Randomisation based:

- Randomness results from random treatment assignment.

- In the context of experimentation, where we can write the treatment group mean as $\bar{Y}_t = \frac{1}{n_t}\sum_{i=1}^{n}W_iY_i$, we treat the $W_i$s as random and $Y_i$s as fixed ("Out of all $n$ units with fixed potential outcomes that we have in our experiment sample, which ones got randomly allocated to the treatment group?")
