# Notes on holland1986statistics

- Wants to make the point that statistics has a lot to say about causal inference and thus needn't limit itself to associational inference.

- Also wants to show fundamental differences between causal and associational inference.

- Overall layout:

    - Introduce associational and causal inference approaches and compare the two.

    - Compare them 





- We have potential outcomes $Y_i(1)$ and $Y_i(0)$.

- The individual-level causal effect is a comparison of the two, usually $Y_i(1) - Y_i(0)$.

- The Fundamental Problem of Causal Inference is that for any individual we can every only observe one of the two potential outcomes. This means that we cannot observe the individual-level causal effect.

- There are two general solutions to the fundamental problem:

    - The scientific solution uses homogeneity or invariance assumptions (e.g. time has no effect on measurements – this is what we informally use in everyday life).

    - The statistical solution is to rely on information from the entire experiment population and focus on the average treatment effect $\mathbb{E}[Y(1) - Y(0)] = \mathbb{E}[Y(1)] - \mathbb{E}[Y(0)]$. The last two terms can be estimated from an experiment where some units are exposed to treatment and others to control. The key insight here is that the statistical approach makes it possible to replace the *impossible to observe* individual-level causal effect with the *possible to estimate* average causal effect over a population of units.