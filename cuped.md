---
title: "CUPED"
author: "Fabian Gunzinger"
date: 28 May 2024
date-format: D MMM YYYY
slide-number: true
format:
  revealjs:
    smaller: true  
---

## What is CUPED?

- CUPED stands for **C**ontrolled experiments **U**sing **P**re-**E**xperiment **D**ata

- It is a statistical method to make experiments faster by reducing outcome metric variance

- It was introduced by researchers at Microsoft in 2013 and is an industry standard

- We've recently deployed it in our experimentation evaluation pipeline


## The plan for the next hour

1. Why reduce variance?

2. How does CUPED reduce variance?

3. The road to CUPED at JET

## My goal

Everyone

- Understand how all the formulae and terms (alpha, etc.) hang together

People with stats background 

- get deeper understanding...


People without 

- get good sense of how experimetation works at high-level, how CUPED works, 
- that math needn't be scary


# Why reduce variance?



## Experiment setup

- We randomly sample $N$ units from a larger population (e.g. UK customers) --- the proportion of units we sample is our audience percentage on JETFM

- For a two-variant experiment, we then randomly allocate each unit to either the treatment group ($W_i = 1)$ or control group ($W_i = 0$)

- For each unit $i$, we observe an outcome $Y_i$ --- this is $i$'s value for a given outcome metric


## Defining causal effects

- Each unit has an outcome $Y(1)_i$ if they're assigned to treatment and outcome $Y(0)_i$ if they're assigned to control

- We can't observe both, and before the beginning of the experiment, we don't know which one we'll observe --- so they're called **potential outcomes**

- The **unit-level causal effect** of the treatment on unit $i$ is

$$
Y(1)_i - Y(0)_i
$$

- The **average treatment effect (ATE)** across all units is

$$
\tau = \frac{1}{N}\sum_{i=1}^N \biggl(Y(1)_i - Y(0)_i \biggr) = \bar{Y}(1)_t - \bar{Y}(0)_c
$$

- The ATE is simple the average individual-level causal effect

- Hence, potential outcomes provide a coherent way to think about causal effects


## Estimating the average treatment effect

- That true effect is unobservable (why?)

- We estimate is using the difference in average observed outcomes in the treatment and control groups

$$
\hat{\tau} = \bar{Y}_t - \bar{Y}_c
$$

$\qquad$ where

$$
\bar{Y}_t = \frac{1}{N_t}\sum_{i:W_i = 1} Y_i \qquad \qquad \bar{Y}_c = \frac{1}{N_c}\sum_{i:W_i = 0} Y_i
$$

- One reason $\bar{\tau}$ is a good estimator of $\tau$ is because it is **unbiased**---on average, we get the right answer (so $\mathbb{E}[\hat{\tau}] = \tau$, but we won't show this here)


## Variance of treatment effect estimator

- Because we randomly draw units from the population and randomly assign them to variants, all the $Y_i$ values we observe are random

- $\bar{Y}_t$ and $\bar{Y}_c$ are constructed from these random values, so they are also random

- $\hat{\tau}$ is thus constructed from random values, and is also random

- For $\hat{\tau}$ to be random means that if we were to rerun the experiment many times, we'd get a different value of $\hat{\tau}$ every time

- That variation is captured by the variance of $\hat{\tau}$, which --- for a typical experiment --- is given by

$$
\mathbb{V}(\hat{\tau}) = \frac{4\sigma^2}{N},
$$

$\qquad$ where $\sigma^2$ is the variance of the $Y_i$ values in the population


## Testing for significance

- To determine if the $\hat{\tau}$ value from our experiment is due to randomness or a true underlying effect, we perform an hypothesis test

- We define our hypotheses

$$
\begin{align}
H_0: \tau = 0 \qquad H_A: \tau \neq 0
\end{align}
$$

- We define our significance level, $\alpha$, and get the associated critical value, $z_{\alpha/2}$

- We calculate the test statistic

$$
Z = \frac{\hat{\tau} - \tau_{H_0}}{\sqrt{\frac{4\sigma^2}{N}}}
$$

- We reject $H_0$ if $|Z| > z_{\alpha/2}$


## Errors


|                                 | **$\mathbf{H_0}$** | **$\mathbf{H_A}$**  |
| -                               | -                       | -                         |
| **$\mathbf{H_0}$ not rejected** | Correct decision        | **Type II error**         |
| **$\mathbf{H_0}$ rejected**     | **Type I error**        | Correct decision          |

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


# How CUPED reduces variance

## The key insight

- Say that in addition to $Y_i$, we also have another variable $X_i$

- $X_i$ can be any variable that is correlated with $Y_i$ and independent of treatment allocation

- In practice, the best and simplest choice for $X_i$ is usually the pre-experiment period value of $Y_i$

- We can then define a new adjusted variable, $Y_i^{cuped}$, as

$$
Y^{cuped}_i = Y_i - \theta X_i
$$

- Using $Y^{cuped}_i$ instead of $Y_i$ for experiment evaluation leaves $\hat{\tau}$ unbiased but reduces its variance


## The CUPED estimator

- The estimator using the unadjusted data was

$$
\hat{\tau} = \bar{Y}_t - \bar{Y}_c
$$

- Naturally, the CUPED estimator is

$$
\begin{align}
\hat{\tau}^{cuped}
&= \bar{Y}^{cuped}_t - \bar{Y}^{cuped}_c
\end{align}
$$

- We'll now see that it's indeed unbiased and has lower variance than the standard estimator

## Unbiasedness of the CUPED estimator

- Using our adjusted variable, we have

$$
\begin{align}
\bar{Y}^{cuped}_t 
&= \frac{1}{N_t}\sum_{i:W_i = 1} Y^{cuped}_i
= \frac{1}{N_t}\sum_{i:W_i = 1}\left(Y_i - \theta X_i\right)
= \bar{Y}_t - \theta \bar{X}_t \\[5pt]
\bar{Y}^{cuped}_c
&= \frac{1}{N_c}\sum_{i:W_i = 0} Y^{cuped}_i
= \frac{1}{N_c}\sum_{i:W_i = 0}\left(Y_i - \theta X_i\right)
= \bar{Y}_c - \theta \bar{X}_c
\end{align}
$$

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

- To show that $\hat{\tau}$ is unbiased, we have to show that on average $\hat{\tau}$ equals $\tau$---that $\mathbb{E}[\hat{\tau}^{cuped}] = \tau$

- We can do this as follows

$$
\begin{align}
\mathbb{E}[\hat{\tau}^{cuped}]
&= \bar{Y}^{cuped}_t - \bar{Y}^{cuped}_c \\[5pt]
&= \mathbb{E}\left[\left(\bar{Y}_t - \theta \bar{X}_t\right) 
- \left(\bar{Y}_c - \theta \bar{X}_c\right)\right] \\[5pt]
&= \mathbb{E}[\bar{Y}_t] - \theta \mathbb{E}[\bar{X}_t] 
- \mathbb{E}[\bar{Y}_c] + \theta \mathbb{E}[\bar{X}_c] \\[5pt]
\text{\scriptsize($X_i$ independent of treatment assignment)} &= \mathbb{E}[\bar{Y}_t] - \mathbb{E}[\bar{Y}_c] \\[5pt]
&= \mathbb{E}[\bar{Y}_t - \bar{Y}_c] \\[5pt]
&= \mathbb{E}[\hat{\tau}] \\[5pt]
\text{\scriptsize(stated above)} &= \tau
\end{align}
$$


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


## Sample size with CUPED

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


# The road to CUPED at JET

## The road to CUPED at JET

1. Pilot: OneWeb Ireland (H1 2023)

2. Change in metric computation pipeline (Q3 2023)

3. Option appraisal (Q4 2023)

4. Implementation (Q1 2024)


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
