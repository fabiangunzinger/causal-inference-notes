# Analysis {#sec-analysis}

- Discuss analysis for each major case of a 3 x 3 table: method of analysis (Fisher, Neyman, Regression), and source of uncertainty (Sampling, Randomisation, Both)


Why would we want to include covariates in a randomised experiment analysis?

1) If assignment to treatment is random within groups but not across groups (e.g. students in rural schools were a bit more likely to be assigned to small classes in the STAR experiment), then we need to check whether including school id changes the result.

2) Including controls that have explanatory power for our outcome of interest helps us estimate the causal effect with more precision (and thus increases power) because it lowers the residual variance of the outcome variable, which in turn reduces the standard error of the causal effect.
