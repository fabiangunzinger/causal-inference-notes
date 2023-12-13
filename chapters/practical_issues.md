# Practical issues

There are a lot of things that can make life hard for online experimenters.


## Budget effects in Ads

## Feedback loops from personalisation

## Cannibalisation and crossover

## Seasonality

- Seasonality comes in many forms: day of week effects, week of year effects, season effects, holiday effects, etc.

- The challenge is that, potentially, user behaviour might differ on certain days or over certain time periods. Whether it is really a problem depends on the context. One aspect that is often forgotten here is that seasonality, first and foremost, is about a shift in levels -- activity on LinkedIn might go down during the summer months. What we usually want to measure, however, is the difference between treatment and control units. Hence, if you don't have reason to believe that the effect of the treatment is different during a particular season (e.g. because you think it's additive), then seasonality might not be a problem for you.

- Solution: design your experiment so as to take seasonality into account. E.g. run your experiment for at least one week to account for day of week effects (that's generally a good idea), don't run crucial experiments during the holiday season or on major holidays or discard data from such periods, etc. 

- What to take into account depends on your context. So understand the relevant seasonality for you (if you're a travel app, consider seasonality of travel demand, if you're an e-commerce site, consider seasonality of shopping behaviour)


## Differences in time-to-action between users

- Some users may engage with a new features immediately, others might take a while and then react differently to it.

- When running experiments for a very short time, we might thus get a biased picture of the overall effect of the feature.


## Novelty and learning effects

Challenge: behaviour might change abruptly and temporarily in response to a new feature (novelty effect) or it might take a while for behaviour fully adapt to a new feature (learning effects). In both cases, the results from a relatively short experiment will not provide a representative picture of the long-run effects of a feature.

Solution: measure long-term effects (by running experiments for longer) or, at least, estimate dynamic treatment effects to see the evolution of the treatment effect. 

Examples:

- Increasing number of adds shows on Google led to increase in add revenue initially but then decrease of clicks in the long term because it increased add blindness @hohnhold2015focusing


## Non-representative users in experiment

Possible scenarios:

- Our marketing department launches an add campaign and attracts a lot of unusual users to the site temporarily.

- A competitor does the same and temporarily takes a ways users from our site.

- Heavy-user bias: heavy users are more likely to be bucketed in an experiment, biasing the results relative to the overall effect of a feature. Depending on the context, this can be an issue.


## Interaction effects

- Users can be simultaneously part of multiple experiments, so that what we measure for reach of them is really the effect of the interaction of all of them. This means that, if only some features are implemented, the results after roll out could be different from those observed during the experiment period.

- However, with large sample sizes, this should not generally be a problem because effects of different experiments average out between treatment and control group.


## General solutions

- Running experiments for longer (thought this comes with opportunity costs, and will increase cookie churn)


## Resources

- [Forbes article on when not to trust your A/B tests](https://www.forbes.com/sites/quora/2015/06/19/when-should-ab-testing-not-be-trusted-to-make-decisions/)

- [Dennis Meisner discussing threats to external validity](https://towardsdatascience.com/ab-testing-when-external-validity-messes-with-your-results-888197b6bc7b)
