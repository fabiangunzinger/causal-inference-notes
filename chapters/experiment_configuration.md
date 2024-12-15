# Experiment configuration

Configuring an experiment requires you to make decisions upfront. This section discusses how to make those decisions.

## Minimal detectable effect

The minimal detectable effect size (MDE) is the smallest effect size you are well-powered to detect: if the true effect size is larger than the MDE then your effective power is larger than the $1-\beta$ you set, if the true effect is smaller, your effective power is lower.

What are you balancing here? The size of the effect you are able to identify and the time it takes to do it; all else equal, the smaller a change you want to be able to detect, the longer it will take for the experiment to run because you need more sample size.

The relevant question to ask here is "what counts as a practically relevant change?" To answer that, consider:

  - Maturity of service (the more mature, the smaller a change can be expected)

  - Size of service (the larger, the smaller a change still generates a lot of revenue)

  - Cost of change that need ot be covered

    - Cost of fully building out feature for launch (can be 0 when fully built out for experiment or high if we use painted door)

    - Cost of maintaining new code (new code has higher bugs, may increase code complexity and maintenance)

    - Other costs: e.g. does CPU utilization increase?


## Significance level

The significance level, often denoted $\alpha$, is the probability of concluding that your feature works when it doesn't. 

What are you balancing here? The probabilities of making a type I and type II error; the higher significance level, the less likely we are to implement useless features (to make a Type I error) but the more likely we are to no implement useful features (to make a Type II error).

Hence, gotta balance cost of implementing useless feature and cost of not implementing useful feature. Things that play into this:

  - How long will feature be in effect (less long lowers risk of implementing)?

  - How widely will it be deployed (less widely lowers risk of implementing)?

  - How many users will see it / where in the funnel is it (later in funnel lowers risk of implementation)

- What to do in practice:

    - Start from baseline values ($alpha = 0.05$)

    - Adjust depending on balance of risks

### Power

- What are you balancing here? The risk of making a Type II error and the time you have to wait for your results.

- All else equal, the higher a level or power you want, the longer you'll have to run the experiment to accumulate the requried sample size.

- Factors to consider:

  - How costly is it to not implement a useful feature.



## How to get that info in practice?

- Think about the [Expected Value of Information](https://www.linkedin.com/pulse/concept-evi-expected-value-information-ronny-kohavi/): basically: investing a little bit of research (expert consultation, querying data) reduces uncertainty a lot while costing little.





## Traffic percentage

## Traffic split

## Ramp-up proceedure