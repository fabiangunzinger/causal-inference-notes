---
title: "Understanding CUPED"
author: "Fabian Gunzinger"
date: 28 May 2024
date-format: D MMM YYYY
slide-number: true
format:
  revealjs:
    smaller: true  
---

## What CUPED is not...

![*Cupid is the Roman god of love and desire. The bow and arrow represent his source of power; a person who is shot by Cupid's arrow is filled with uncontrollable desire. ([Wikipedia](https://en.wikipedia.org/wiki/Cupid)).*](cupid.png)




## So, what *is* CUPED?

- CUPED stands for **C**ontrolled experiments **U**sing **P**re-**E**xperiment **D**ata

- It is a statistical method to make experiments faster by reducing outcome metric variance

- It was introduced by researchers at Microsoft in 2013 and is now an industry standard

- We've recently deployed it in our experimentation evaluation pipeline


## The plan for the next hour<br><br>

1. How does CUPED reduce variance and speed up experiments?

2. Why reduce variance? -- A brief tour of the statistics of experimentation


## My goals for the session

**For everyone**:

- Understand how and why CUPED works

. . . 

**For those who stay for part II...**

...**and do not have a stats background**

- Demystify experiment concepts ("alpha", "power", "MDE", etc.) by showing what they are, how they hang together, and that there is no mystery to them

- Gain a high-level understanding of the stats that power experimentation

- See that math and stats -- even if unfamiliar -- needn't be confusing or scary

. . . 

**...and do have a stats background**: 

- Gain a deeper understanding of the statistics of experimentation

. . . 

I'd sincerely appreciate if you let me know whether I succeeded!

## Demystifying math notation -- index variables

- We have outcome metric values for $N_c$ customers in our control group (think "**N**umber of **C**ontrol customers")

. . . 

- If we have 231,286 customers in control, then $N_c = 231,286$

. . . 

- We label as $Y_1$ the outcome uf customer 1; $Y_2$ that of customer 2; $Y_{1134}$ that of customer 1134; etc.

. . . 

- We refer to the outcome of an unspecified customer as $Y_i$

. . . 

- $i$ is called the index variable, because it specifies which customer's outcome we're referring to

. . . 

- So, we can say that we have outcome metric values $Y_i$ for $i = 1, 2, ..., N_c$

## index variables (cont.)

- We use the same index variable approach for the variable that tells us whether a certain customer is in the treatment or control group

. . . 

- The treatment status for customer *i* is $T_i$

. . . 

- And we set $T_i = 1$ if customer *i* is in the treatment group and $T_i = 0$ if they're in the control group



## Demystifying math notation -- summation sign

- Sometimes we want to sum all $N_c$ outcomes --- how can we conveniently refer to that sum?

. . . 

- We could write $Y_1 + Y_2 + Y_3 + \ldots$ up to $N_c$ --- but given that $N_c$ is typically in the 1000s, we don't really want to do that

. . . 

- We could write "sum of all $N_c$ outcomes" --- but that still takes some work, can be ambiguous, and is just a "blob" of text we can't do math with

. . . 

- We could use a shorthand --- say $S$ for "sum" --- make use of our index variable $i$, and define the sum of all outcomes for customers 1 to $N_c$ as

$$
\mathop{S}\limits_{i=1}^{N_C} Y_i
$$

. . . 

- That's what mathematicians do. Except, being mathematicians, they use uppercase Sigma, the Greek equivalent to the Roman "S", to give us 

$$
\mathop{\Sigma}\limits_{i=1}^{N_C} Y_i
$$


## Demystifying math notation -- variance

- Sometimes, instead of summing all $N_c$ values, we want to describe how they vary

- One way to describe variation is to measure how far, on average, values are from their average, $\bar{Y}$, so we might try

$$
\frac{1}{N_c}\sum_{i=1}^{N_c} \left(Y_i - \bar{Y}\right) = \frac{1}{N_c}\Bigl[ \left(Y_1 - \bar{Y}\right) +  \left(Y_2 - \bar{Y}\right) + ... + \left(Y_{N_c} - \bar{Y}\right) \Bigr]
$$

- But "- differences" and "+ differences" would cancel out and sum to 0. To remove "- differences" we might try

$$
\frac{1}{N_c}\sum_{i=1}^{N_c} \left|Y_i - \bar{Y}\right| = \frac{1}{N_c}\Bigl[ \left|Y_1 - \bar{Y}\right| +  \left|Y_2 - \bar{Y}\right| + ... + \left|Y_{N_c} - \bar{Y}\right| \Bigr]
$$

- Which would work, but mathematicians don't like much. Instead, they eliminate "- differences" by squaring the differences, which gives us the (empirical) variance

$$
\frac{1}{N_c}\sum_{i=1}^{N_c} \left(Y_i - \bar{Y}\right)^2 = \frac{1}{N_c}\Bigl[ \left(Y_1 - \bar{Y}\right)^2 +  \left(Y_2 - \bar{Y}\right)^2 + ... + \left(Y_{N_c} - \bar{Y}\right)^2 \Bigr]
$$


## Why reduce variance?

- Now we know what the variance is. But why bother reducing it?

- Experiment duration is determined by how long it takes to collect data from the required number of unique units

. . . 

- The required number of unique units (i.e. required sample size) is approximately given by:
$$
N = 32\frac{\mathbb{V}(Y_i)^2}{\text{MDE}^2}.
$$

- MDE is typically pre-determined, so reducing $\mathbb{V}(Y_i)^2$ is our main lever to reduce sample size and reduce experiment duration

. . . 

- (We'll see where the 32 comes from in part 2)


## How does CUPED reduce variance and speed up experiments?

## The key insight

*With suitable extra data, we can **adjust our outcome metric** such that the **treatment estimate remains unchanged** while the variable's **variance is lower**, which reduces experiment duration*


## Adjusting the outcome metric

- Say that in addition to $Y_i$, we also have another variable $X_i$

- $X_i$ can be any variable that is **correlated with $Y_i$** and **independent of treatment** allocation

- In practice, the best and simplest choice for $X_i$ is usually the **pre-experiment period value** of $Y_i$

. . . 

- For example, if $Y_i$ is visit conversion, we could calculate for each customer the visit conversion over the 60 days prior to the experiment start, and use that as $X_i$

. . . 

- We can then define a new, adjusted, variable, $Y_i^{cuped}$, as

$$
Y^{cuped}_i = Y_i - \theta X_i
$$

$\quad$ where $\theta$ is some number we'll come back to

. . . 

- Using $Y^{cuped}_i$ instead of $Y_i$ for experiment evaluation leaves the treatment effect estimate unchanged but reduces its variance


## Treatment effect estimate remains unchanged

- The true causal effect -- the true effect of our feature -- is unobservable (we'll see why in part 2), and we refer to it as $\tau$ (Greek "tau" -- think "treatment effect")

. . .

- In a typical experiment, we use the difference in the average outcomes in the treatment and control groups to estimate it

. . . 

- Using the unadjusted outcome metric, we have:

$$
\hat{\tau} = \bar{Y}_t - \bar{Y}_c
$$

$\quad$ where

$$
\bar{Y}_t = \frac{1}{N_t}\sum_{\text{if }T_i = 1} Y_i \qquad \qquad \bar{Y}_c = \frac{1}{N_c}\sum_{\text{if }T_i = 0} Y_i
$$

. . . 

- We can proof (but won't) that on average, $\hat{\tau}$ equals the true effect, meaning that $\mathbb{E}[\hat{\tau}] = \tau$

. . . 

- Because of this, we say that $\hat{\tau}$ is an unbiased estimator


## Treatment effect estimate remains unchanged (cont.)

- When we use the CUPED-adjusted outcome metric values, a natural way to estimate the true effect is:

$$
\begin{align}
\hat{\tau}^{cuped}
&= \bar{Y}^{cuped}_t - \bar{Y}^{cuped}_c
\end{align}
$$

$\quad$ where, instead of using unadjusted values $Y_i$, we simply use $Y_i^{cuped}$

. . . 

- We'll show next that this approach, too, returns the true effect on average, and is thus also unbiased

. . . 

- Hence, when we say that CUPED doesn't change the treatment effect estimate, what we mean is *not* that the estimate is exactly the same, but that CUPED, too, gives us the correct result on average

. . . 

- In practice, for large sample sizes, this means that the CUPED estimate will be very similar to the unadjusted estimate


## Unbiasedness of the CUPED estimator

- Using our adjusted variable, we can write the average treatment group outcome as (similarly for control group):

$$
\begin{align*}
\bar{Y}^{cuped}_t 
&= \frac{1}{N_t}\sum_{\text{if }T_i = 1} Y^{cuped}_i \\[5pt]
&= \frac{1}{N_t}\sum_{\text{if }T_i = 1}\left(Y_i - \theta X_i\right) \\[5pt]
&= \frac{1}{N_t}\sum_{\text{if }T_i = 1}Y_i - \theta \frac{1}{N_t}\sum_{\text{if }T_i = 1}X_i \\[5pt]
&= \bar{Y}_t - \theta \bar{X}_t
\end{align*}
$$

. . . 

- So we can rewrite the CUPED estimator as

$$
\begin{align}
\hat{\tau}^{cuped}
&= \bar{Y}^{cuped}_t - \bar{Y}^{cuped}_c \\[5pt]
&= \left(\bar{Y}_t - \theta \bar{X}_t\right) 
- \left(\bar{Y}_c - \theta \bar{X}_c\right)
\end{align}
$$


## Unbiasedness of the CUPED estimator (cont.)

- We know (from above), that $\hat{\tau}$ is unbiased, meaning that $\mathbb{E}[\hat{\tau}] = \tau$

. . . 

- A simple way to show that on average, $\hat{\tau}^{cuped}$ equals $\hat{\tau}$, so that $\mathbb{E}[\hat{\tau}^{cuped}] = \mathbb{E}[\hat{\tau}] = \tau$

. . . 

- We can do this as follows

$$
\begin{align}
\mathbb{E}[\hat{\tau}^{cuped}]
&= \bar{Y}^{cuped}_t - \bar{Y}^{cuped}_c \\[5pt]
&= \mathbb{E}\left[\left(\bar{Y}_t - \theta \bar{X}_t\right) 
- \left(\bar{Y}_c - \theta \bar{X}_c\right)\right] \\[5pt]
&= \mathbb{E}[\bar{Y}_t] - \theta \mathbb{E}[\bar{X}_t] 
- \mathbb{E}[\bar{Y}_c] + \theta \mathbb{E}[\bar{X}_c] \\[5pt]
&= \mathbb{E}[\bar{Y}_t] - \mathbb{E}[\bar{Y}_c] - \theta \mathbb{E}[\bar{X}_t] + \theta \mathbb{E}[\bar{X}_c] \\[5pt]
(X_i \text{ independent of treatment}) &= \mathbb{E}[\bar{Y}_t] - \mathbb{E}[\bar{Y}_c] \\[5pt]
&= \mathbb{E}[\bar{Y}_t - \bar{Y}_c] \\[5pt]
&= \mathbb{E}[\hat{\tau}] \\[5pt]
&= \tau
\end{align}
$$


## Outcome metric variance is smaller

## Variance of the CUPED estimator

- We have seen above that the variance of our standard treatment estimator, $\hat{\tau}$, is given by

$$
\mathbb{V}(\hat{\tau}) = \frac{4\sigma^2}{N},
$$

$\qquad$ where $\sigma^2$ is the population variance of the outcome metric values --- the $Y_i$s

- Hence, the variance of the CUPED estimator is given by

$$
\mathbb{V}(\hat{\tau}^{cuped}) = \frac{4\sigma^2_{cuped}}{N},
$$

$\qquad$ where $\sigma^2_{cuped}$ is the population variance of the adjusted outcome metric values --- the $Y_i^{cuped}$s

- To find $\mathbb{V}(\hat{\tau}^{cuped})$, we need to find $\sigma^2_{cuped}$


## Variance of the CUPED estimator (cont.)

- The variance of CUPED-adjusted values is given by

$$
\begin{align}
\mathbb{V}\left(Y^{cuped}_i\right)
&= \mathbb{V}(Y_i - \theta X_i) \\[5pt]
&= \mathbb{V}(Y_i) + \theta^2\mathbb{V}(X_i) - 2\theta Cov(Y_i, X_i)
\end{align}
$$

- This is minimised for

$$
\theta^* = \frac{Cov(Y_i, X_i)}{\mathbb{V}(X_i)}
$$


## Variance of the CUPED estimator (cont.)

- Using $\theta^*$ in the above expression, rearranging and substituting (see appendix for all steps) gives

$$
\sigma^2_{cuped} = \sigma^2(1 - \rho^2) 
$$

$\quad$ where $\rho = \frac{Cov(Y_i, X_i)}{\sqrt{\mathbb{V}(Y_i)\mathbb{V}(X_i)}}$, $\sigma^2 = \mathbb{V}(Y_i)$, and $\sigma^2_{cuped} = \mathbb{V}(Y^{cuped}_i)$

- The correlation coefficient is between -1 and 1

- As long as there is some correlation between $Y_i$ and $X_i$, $\sigma^2_{cuped} < \sigma^2$

- The stronger the correlation, the smaller $\sigma^2_{cuped}$

- If there is no correlation, $\sigma^2_{cuped} = \sigma^2$


## Variance of the CUPED estimator (cont.)

- The CUPED estimator variance is thus

$$
\mathbb{V}(\hat{\tau}^{cuped}) = \frac{4\sigma^2_{cuped}}{N} = \frac{4\sigma^2(1 - \rho^2)}{N} < \frac{4\sigma^2}{N} = \mathbb{V}(\hat{\tau})
$$

$\quad$ as long is there some correlation between $Y_i$ and $X_i$




## Effect on required sample size and experiment duration

- The reduction in required sample size from CUPED is given by

$$
\frac{N^{cuped}}{N}
= \frac{\frac{(z_{\alpha/2} + z_{1-\beta})^2}{P(1-P)}\frac{\sigma^2_{cuped}}{\tau^2}}{\frac{(z_{\alpha/2} + z_{1-\beta})^2}{P(1-P)}\frac{\sigma^2}{\tau^2}}
= \frac{\sigma^2_{cuped}}{\sigma^2}
= \frac{\sigma^2(1 - \rho^2)}{\sigma^2}
= (1 - \rho^2)
$$

- For example, if $\rho = 0.45$, we'd have

$$
\frac{N^{cuped}}{N} = (1 - \rho^2) = (1 - 0.45^2) \approx 0.8 
$$

- CUPED would reduce the required sample size by 20%, about what we get on average at JET



## Why reduce variance? -- A quick tour of the statistics of experimentation

## Experiment setup

- We randomly sample $N$ units from a larger population (e.g. UK customers)

. . . 

- We randomly allocate each unit to either the treatment group ($T_i = 1)$ or control group ($T_i = 0$)

. . . 

- For each unit $i$, we observe an outcome metric value, $Y_i$


## Defining the causal effect

- Each unit has an outcome $\mathbf{Y(1)_i}$ if they're assigned to treatment and outcome $\mathbf{Y(0)_i}$ if they're assigned to control

- We can't observe both, and before the beginning of the experiment, we don't know which one we'll observe --- so they're called **potential outcomes**

. . . 

- The **unit-level causal effect** of the treatment on unit $i$ is:

$$
Y(1)_i - Y(0)_i
$$

. . . 

- The **average treatment effect (ATE)** across all units is:

$$
\tau = \frac{1}{N}\sum_{i=1}^N \biggl(Y(1)_i - Y(0)_i \biggr) = \bar{Y}(1)_t - \bar{Y}(0)_c
$$

- The ATE is simple the average individual-level causal effect

- It's the difference in the average outcome in two different states of the world: one where everybody is given the treatment and one where nobody is

. . . 

- Hence, potential outcomes provide a coherent way to think about causal effects

. . . 

**Key takeaway**: The unobservable true causal effect we care about is the difference in the average outcome between two scenarios: one where everyone is exposed to the treatment and one where nobody is


## Estimating the causal effect

- We've seen that the true effect is unobservable (why?)

. . . 

- We estimate is using the difference in average observed outcomes in the treatment and control groups

$$
\hat{\tau} = \bar{Y}_t - \bar{Y}_c
$$

$\qquad$ where

$$
\bar{Y}_t = \frac{1}{N_t}\sum_{i:T_i = 1} Y_i \qquad \qquad \bar{Y}_c = \frac{1}{N_c}\sum_{i:T_i = 0} Y_i
$$

. . . 

- One reason $\bar{\tau}$ is a good estimator of $\tau$ is because it is **unbiased**---on average, we get the right answer (so $\mathbb{E}[\hat{\tau}] = \tau$)

. . . 

**Key takeaway**: We estimate the unobservable true causal effect as the difference in the average outcomes between the treatment and control groups in our experiment

## Variance of causal effect estimator

- Because we randomly draw units from the population and randomly assign them to variants, all the $Y_i$ values we observe are random

. . . 

- $\bar{Y}_t$ and $\bar{Y}_c$ are constructed from these random values, so they are also random

. . . 

- $\hat{\tau}$ is constructed from $\bar{Y}_t$ and $\bar{Y}_c$ and is thus also random

- For $\hat{\tau}$ to be random means that if we were to rerun the experiment many times, we'd get a different value of $\hat{\tau}$ every time

. . . 

- That variation is captured by the variance of $\hat{\tau}$, which --- for a typical experiment --- is given by

$$
\mathbb{V}(\hat{\tau}) = \frac{4\sigma^2}{N},
$$

$\qquad$ where $\sigma^2$ is the variance of the $Y_i$ values in the population

. . . 

**Key takeaway**: The treatment effect estimate from a single experiment isn't the true effect (which is fixed), but an estimate that varies randomly due to random sampling and treatment assignment, and would differ between repetitions of the same experiment


## Testing for significance

- We have just seen that the treatment effect of our experiment fluctuates randomly because of random sampling and random treatment assignment

- To determine if the estimate in our experiment, $\hat{\tau}$, is due to randomness or a true underlying effect we perform a hypothesis test

. . . 

**Hypothesis test steps**:

1. Define hypotheses:

$$
\begin{align}
H_0: \tau = 0 \qquad H_A: \tau \neq 0
\end{align}
$$

. . . 

2. Define significance level, $\alpha$, and get the associated critical value, $z_{\alpha/2}$

. . . 

3. Calculate the test statistic:

$$
\begin{align}
Z
= \frac{\hat{\tau} - \tau_{H_0}}{\mathbb{V}(\hat{\tau})} 
= \frac{\hat{\tau} - \tau_{H_0}}{\sqrt{\frac{4\sigma^2}{N}}}
\end{align}
$$

. . . 

4. Make a decision --- **reject $\textbf{H_0}$ if $\mathbf{|Z| > z_{\alpha/2}}$**

. . . 

**Key takeaway**: The significance level we choose (usually 5%) provides a critical value. We reject \(H_0\) if our calculated test statistic, which depends on the variance, exceeds that critical value



## Potential errors


|                                 | **$\mathbf{H_0}$** | **$\mathbf{H_A}$** |
| ------------------------------- | ------------------ | ------------------ |
| **$\mathbf{H_0}$ not rejected** | Correct decision   | **Type II error**  |
| **$\mathbf{H_0}$ rejected**     | **Type I error**   | Correct decision   |

: Types of errors

- Commonly, we define

$$
\begin{align}
P(\text{Type I error}) &= P(\text{reject $H_0$} \,|\, \text{$H_0$}) = \alpha \\[5pt]
P(\text{Type II error}) &= P(\text{not reject $H_0$} \,|\, \text{$H_A$}) = \beta\\[5pt]
&\text{and}\\[5pt]
\text{Power} &= P(\text{reject $H_0$} \,|\, \text{$H_A$}) = 1 - \beta
\end{align}
$$

- Setting $\alpha = 0.05$ and $\text{Power} = 0.8$, as we typically do, means that over the long run

  - we reject $H_0$ in 5% of the cases where it is true
  - we fail to reject $H_0$ in 20% of cases where it is false



## Controlling error rates

- How do we control the two error rates?

- We control Type I error rate by rejecting $H_0$ if $|Z| > z_{\alpha/2}$

- Given that $\text{Power} = P(\text{reject $H_0$}  | \text{$H_A$})$ we can control it setting

$$
\begin{align}
P(|Z| > z_{\alpha/2} \, |\,\text{$H_A$}) &= \text{Power} \\[5pt]
P\left(\left|\frac{\hat{\tau} - \tau_{H_0}}{\sqrt{\frac{4\sigma^2}{N}}}\right| > z_{\alpha/2} \, |\,\text{$H_A$}\right) &= \text{Power} \\
\end{align}
$$

- Rearranging this and doing algebra and substitutions we get

$$
N = \frac{(z_{\alpha/2} + z_{1-\beta})^2}{P(1-P)}\frac{\sigma^2}{\tau^2}.
$$


## Why reduce variance (finally!)?

- Experiment duration is determined by how long it takes to reach required sample size

- We can control Type I and Type II error rates by calculating required sample size as

$$
N = \frac{(z_{\alpha/2} + z_{1-\beta})^2}{P(1-P)}\frac{\sigma^2}{\tau^2}.
$$

- Typically, all elements but $\sigma^2$ are pre-determined

- Hence: reducing $\sigma^2$ is our main lever to reduce sample size and reduce duration 



# Useful resources

## Useful resources

- [The original CUPED paper](https://www.exp-platform.com/Documents/2013-02-CUPED-ImprovingSensitivityOfControlledExperiments.pdf) -- the original paper

- [Variance reduction section of Deng's causal inference book](https://alexdeng.github.io/causal/sensitivity.html#vrreg) -- more in-depth discussion of some aspects of CUPED and its link to regression adjustment

- [Improving the Sensitivity of Online Controlled
Experiments: Case Studies at Netflix](https://www.kdd.org/kdd2016/papers/files/adp0945-xieA.pdf)

- [How Booking.com increases the power of online experiments with CUPED](https://booking.ai/how-booking-com-increases-the-power-of-online-experiments-with-cuped-995d186fff1d)

- [You can't spell CUPED without Frisch-Waugh-Lovell](https://www.evanmiller.org/you-cant-spell-cuped-without-frisch-waugh-lovell.html) -- good post exploring link to FWL theorem

- [Understanding CUPED](https://towardsdatascience.com/understanding-cuped-a822523641af) -- good post exploring link to multiple regression (also using FWL theorem) and DiD.

- [Reducing variance in A/B testing with CUPED](https://bytepawn.com/reducing-variance-in-ab-testing-with-cuped.html#reducing-variance-in-ab-testing-with-cuped)

- [CUPED on Statsig](https://blog.statsig.com/cuped-on-statsig-d57f23122d0e)

- [Five ways to reduce variance in A/B testing](https://bytepawn.com/five-ways-to-reduce-variance-in-ab-testing.html#five-ways-to-reduce-variance-in-ab-testing)

- [Online Experiments Tricks — Variance Reduction](https://towardsdatascience.com/online-experiments-tricks-variance-reduction-291b6032dcd7)

- [CUPED, CUPAC, and Other Ways to Reduce Variance in an Experiment](https://j-sephb-lt-n.github.io/exploring_statistics/cuped_cupac_and_other_variance_reduction_techniques.html)

- [Don't use a t-test for A/B testing](https://towardsdatascience.com/dont-use-a-t-test-for-a-b-testing-e4d2ef7ab9b6)

- [Variance Reduction in Experiments — Part 1: Intuition -- see also part 2](https://towardsdatascience.com/variance-reduction-in-experiments-part-1-intuition-68b270a0df71)
