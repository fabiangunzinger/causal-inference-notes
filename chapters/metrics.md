# Metrics

The choice of metrics to consider when evaluating an experiment is not trivial. In field experiments, collecting data can be very costly, which puts an automatic limit to the number of metrics collected. In online experiments, the number of metrics we could look at is vast.

## Types of metrics

- Primary

- Secondary

- Guardrail


## How to select metrics

- Look at BIT bluebook for overall framework for how to think about metrics (specificity etc)

- Primary metric something that directly captures what you wanna improve? Guardrails general health metrics you don't want to go down (e.g. revenue, conversion)? Based on Kohavi anecdote below

## Misc issues

- Selecting the wrong metric can lead to misleading results. @kohavi2012trusworthy provide a memorable example from an experiment at Bing: the experiment increased revenue by user because search results were poorer, leading users to make more searches and lead them to click on more adds. This is good in the short-term. But in the long term, users will surely get frustrated by the poorer search results. A better metric would have been one that directly captures the quality of the search results, such as sessions per user. Lesson: have a primary metric that directly captures the thing you want to improve. Use higher level-metrics such as revenue as guardrails.