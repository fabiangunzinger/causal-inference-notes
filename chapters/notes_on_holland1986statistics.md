# Notes on holland1986statistics


## Introduction

- Wants to make the point that statistics has a lot to say about causal inference and thus needn't limit itself to associational inference.

- Also wants to show fundamental differences between causal and associational inference.

- Overall layout:

    - Introduce associational and causal inference approaches and compare the two.

    - Apply them to various ideas and philosophies about causal inference


## Model for associational inference

- A population $U$ of units with individual unit $i$

- A variable is a real-valued function defined on every $i$

- The value of a variable for $i$ is the number assigned by some measurement process to $i$

- $Y$ is the response variable of interest, and there is a value $Y_i$ associated with each $i$

- Define $X$ as another variable defined on $U$, and call $X$ an attribute of the units, with a value $X_i$ associated with each $i$

- Logically, however, $Y$ and $X$ are on equal footing: they are both variables defined on $U$

- For associational inference, we are satisfied to understand *how* $Y$ varies with $X$

- A probability is a proportion of units in $U$

- The expected value the average over $U$

- Conditional expected values the average over a subset of $U$ where subsets are defined on the value of a variable

- It's in the above senses that the model described in the paper is a population model

- The role of time, in associational inference, is merely to define the population of units and to specify the operational meaning of the particular variables (for causal inference, time will be more important)

- The *joint distribution* of $Y$ and $A$ over $U$ is specified by $P(Y = y, X = x)$, which is the proportion of units in $U$ for which $Y_i = y$ and $X_i = x$.

- The *associational parameters* are described by this joint distribution. As an example, the conditional distribution of $Y$ given $A$ is specified as $P(Y = y | X = x)$, which equals $P(Y = y, X = x) / P(X = x)$. This conditional distribution describes how the distribution of $Y$ over $U$ changes as $X$ varies.

- Another typical associational value is the regression of $Y$ on $X$, which calculates the conditional expectation $\mathbb{E}[Y | X = x]$.

- "Associational inference consists of making statistical inferences (estimates, tests, posterior distributions) about associational parameters relating $Y$ and $X$ on the basis of data gathers about $Y$ and $X$ from units in $U$. In this sense, associational statistics is simply descriptive statistics."


## Rubin's Model for causal inference


- We have potential outcomes $Y_i(1)$ and $Y_i(0)$.

- The individual-level causal effect is a comparison of the two, usually $Y_i(1) - Y_i(0)$.

- The Fundamental Problem of Causal Inference is that for any individual we can every only observe one of the two potential outcomes. This means that we cannot observe the individual-level causal effect.

- There are two general solutions to the fundamental problem:

    - The scientific solution uses homogeneity or invariance assumptions (e.g. time has no effect on measurements – this is what we informally use in everyday life).

    - The statistical solution is to rely on information from the entire experiment population and focus on the average treatment effect $\mathbb{E}[Y(1) - Y(0)] = \mathbb{E}[Y(1)] - \mathbb{E}[Y(0)]$. The last two terms can be estimated from an experiment where some units are exposed to treatment and others to control. The key insight here is that the statistical approach makes it possible to replace the *impossible to observe* individual-level causal effect with the *possible to estimate* average causal effect over a population of units.