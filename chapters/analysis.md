# Analysis {#sec-analysis}

todo
- Neyman approach
- Fisher sharp null
- Regression
- ML approaches

- Consider producing table for each major case of a 3 x 3 table: method of analysis (Fisher, Neyman, Regression), and source of uncertainty (Sampling, Randomisation, Both)


## Regression for experiment evaluation
- Start with abadie2020sampling
- See @athey2017econometrics
- See also Friedman critique, Lin response, and Imbens Rubin book response

Why would we want to include covariates in a randomised experiment analysis?

1) If assignment to treatment is random within groups but not across groups (e.g. students in rural schools were a bit more likely to be assigned to small classes in the STAR experiment), then we need to check whether including school id changes the result.

2) Including controls that have explanatory power for our outcome of interest helps us estimate the causal effect with more precision (and thus increases power) because it lowers the residual variance of the outcome variable, which in turn reduces the standard error of the causal effect.


## Machine learning approaches

- There are a number of supervised-learning approaches to improve ATE estimation in observational studies, in particular in scenarios where we have a large number of potential covariates. @athey2017state mention three approaches.

- Double selection approach: use LASSO regression to select covariates that are correlated with outcome and one to select covariates correlated with treatment indicator. Then control for the union of them in the final regression of outcome on treatment indicator. This improves ATE estimator properties compared to a simple regularized regression of outcome on treatment and covariates.

- Balance covariates: there are a number of approaches for both large and small covariate cases to use ML models to find weights that balance covariates such that they mimic the data of a randomised experiment.

- Doubly robust estimators (two models: outcome model relating outcome to treatment and covariates, treatment model relating treatment to covariates. Doubly robust estimator remains consistent if at least one of the two models is correctly specified)
