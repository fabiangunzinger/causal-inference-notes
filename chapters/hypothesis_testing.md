# Hypothesis testing

Suppose you have an idea for a new app feature, or algorithm, or design that you think will improve user experience. In this chapter we'll discuss different approaches for how to test whether your idea works.


## Hypothesis testing

### P-values

::: {.callout-note collapse=true}

### History of the P-value

- There are two schools of thought in statistical significance testing.

- R.A. Fisher thought of the p-value as a useful metric to determine how surprising a given set of data was.

- Jerzy Neyman and Egon Pearson realised that while it is not possible to eliminate false positives and negatives, it is possible to set up a process that guarantees that false positives occur only at a pre-defined rate, which they called $\alpha$.

- Unlike in Fisher's approach, the p-value in the Neyman-Pearson approach doesn't tell us anything about the strength of the evidence in any particular experiment besides whether or not to reject the null hypothesis, but guarantees that in the long run (over the course of many experiments), our false positive rate is not larger than $\alpha$. 
:::


### Types of errors

- The p-value is the probability of observing a test result at least as large as the one we observed under the assumption that the null hypothesis is true.

- A Type I error is when we reject the null hypothesis when it is true (a false positive). It's probability is usually denoted by $\alpha$.

- A Type II error is when we fail to reject the null  hypothesis when it is false (a false negative). It's probability is usually denoted by $\beta$.

- The statistical power of a binary hypothesis test is the probability of a true positive: the probability that we reject the hull hypothesis if it is false (and hence, if the alternative hypothesis is true). The probability of this is $1-\beta$.


### The base-rate fallacy

Suppose you test 100 features out of which 10 have a true effect. If you have 80
percent power and use a 5 percent significance level. You can expect to
get a significant result for 8 of the 10 working features, but you also have a
false positive rate of 5%, so you'll also get a significant result for about 5
non-working features. You thus end up with 13 treatments that appear to work.
But we know that only 8 of these 13, or 62% of them work, while the remaining
5 are false discoveries. Thus, you have a false discovery rate of 38%.

You commit the base-rate fallacy when you confuse your p-value with your false
discovery rate. This would lead you to make statements such as "My p-value is
0.002, so there is only a 2 in a 1000 chance that I found my result by
chance!"

This confuses

$$
P(significant result | H_0),
$$

the p-value, with

$$
P(H_A | significant result)
$$



### Limitations of hypothesis testing

- p-values do not tell you anything about whether the result has any practical significance.

- Any intervention usually has *some* effect, you will always find a significant result with enough data. The question is whether the range of plausible effect sizes (captured by the confidence interval) is relevant.



## Confidence intervals

- Rely on confidence intervals: they provide the same information as a p-value (if they include the value of the null hypothesis then we cannot reject it) but the width of the interval also provides additional information on the uncertainty of the effect and its practical significance. (See [In Praise of Confidence Intervals](https://www.aeaweb.org/articles?id=10.1257/pandp.20201059) by David Romer and [Statistical Significance, p-Values, and the Reporting of Uncertainty](https://www.aeaweb.org/articles?id=10.1257/jep.35.3.157) by Guido Imbens for more).


### Testing and CI duality




## Q&A

Questions

**1.**

a) A student is asked 12 true-or-false questions and gets 3 of them wrong. What is the probability that the student guessed randomly?

b) The student above would actually have been asked questions until they got 3 wrong. What is the probability that they guessed randomly?

c)What do you conclude from a) and b)?


**2.**

Consider the outcome of a large sample size (e.g. 10K subjects) A/B test that yielded tiny (e.g. odds ratio of 1.0008) but statistically significant (e.g. p < 0.001) results. Would you deploy the change to production. Why or why not?

**3.**

A researcher runs an experiment, gets a p-value of 0.033, and concludes that his false positive rate is 3.3 percent. Is that correct? Why or why not?

**4.**

Why don't we include MDE in our hypothesis statement (i.e. "a will increase b by at least MDE for target population")? Wouldn't that be a good idea in a business context where we strongly care about an MDE? Don't we just not do that because academics, who developed the methods, don't usually care about an effect being of a certain size but only about learning what the effect is?


Answers

**1** 

a) Calculate p-value for getting no more than observed number of errors

```{python}
p = stats.binom.cdf(k=3, n=12, p=0.5)
print(f"p-value is: {p:.3f}")
```

**2**

**3**

No. An individual experiment doesn't have a false positive rate. The false positive rate is determined by the proceedure used for experiments over the long run. For example, if you consistently use a p-value of 0.05, then you are guaranteed to have a false positive rate of 5 percent in the long run. This is the main insight underlying the Neyman-Pearson hypothesis testing framework.

**4.**

Including the MDE's in the hypothesis would be incorrect. Why? Because what we formulate is the alternative hypothesis. Without altering the null hypothesis, which traditionally states the effect is zero, our two hypotheses would not be complete (H0 testing effect different from 0, HA asserting that effect is at least MDE means rejecting H0 would not imply support of HA). So why not adapt H0, too? Because the hypothesis is the thing we test when we calculate our test statistic (duh!), and so if included the MDE in the hypothesis formulation, then we'd have to include it in the calculation of the test statistic (subtract it from the observed difference), which would be incorrect. Why? The question confused the MDE with the effect size under the Null hypothesis, which are conceptually different things: the MDE is the smallest effect size we want to detect -- we are interested in effects that are as large or larger than the MDES, we're not testing whether the observed difference is significantly different from it, which is what the null hypothesis value is.
