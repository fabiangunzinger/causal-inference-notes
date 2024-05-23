---
title: "CUPED"
author: "Fabian Gunzinger"
date: "28 May 2024"
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

2. How does CUPED do it?

3. The road to CUPED at JET


# Why reduce variance?



## Experiment setup

- We randomly sample $N$ units from a larger population (e.g. UK customers) --- the proportion of units we sample is our **audience percentage** on JETFM

- For a two-variant experiment, we then randomly allocate each unit to either the treatment group ($W_i = 1)$ or control group ($W_i = 0$)

- For each unit $i$, we observe an outcome $Y_i$ --- this is $i$'s value for a given outcome metric


## Defining causal effects

- Each unit has an outcome $Y(1)_i$ if they're assigned to treatment and outcome $Y(0)_i$ if they're assigned to control

- We can't observe both, and before the beginning of the experiment, we don't know which one we'll observe --- so they're called **potential outcomes**

- The **unit-level causal effect** of the treatment --- the true effect of our feature on unit $i$ is

$$
Y(1)_i - Y(0)_i
$$

- The **average treatment effect (ATE)** across all units is

$$
\tau = \frac{1}{N}\sum_{i=1}^N \left(Y(1)_i - Y(0)_i \right) = \bar{Y}(1)_t - \bar{Y}(0)_c
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

- One reason $\bar{\tau}$ is a good estimator of $\tau$ is because it is **unbiased**---on average, we get the right answer


## Variance of treatment effect estimator

- Because we randomly draw units from the population and randomly assign them to variants, all the $Y_i$ values we observe are random

- $\bar{Y}_t$ and $\bar{Y}_c$ are constructed from these random values, so they are also random

- $\hat{\tau}$ is thus constructed from random values, and is also random

- For $\hat{\tau}$ to be random means that if we were to rerun the experiment many times, we'd get a different value of $\hat{\tau}$ every time

- That variation is captured by the variance of $\hat{\tau}$, which --- for a typical experiment --- is given by

$$
\mathbb{V}(\hat{\tau}) = \frac{4\sigma^2}{N},
$$

$\qquad$ where $\sigma^2$ is the variance of all the $Y_i$ values in the overall population


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
P(|Z| > z_{\alpha/2} \, |\,\text{$H_A$}) &= \text{Power} \\
P\left(\left|\frac{\hat{\tau} - \tau_{H_0}}{\sqrt{\frac{4\sigma^2}{N}}}\right| > z_{\alpha/2} \, |\,\text{$H_A$}\right) &= \text{Power} \\
\end{align}
$$

- Rearranging this, and doing (lots of!) algebra, we get

$$
N = \frac{(z_{\alpha/2} + z_{1-\beta})^2}{P(1-P)}\frac{\sigma^2}{\tau^2}.
$$


## Why reduce variance (finally!)?

- Experiment duration is determined by how long it takes to reach required sample size

- We can control Type I and Type II error rates by calculating required sample size as

$$
N = \frac{(z_{\alpha/2} + z_{1-\beta})^2}{P(1-P)}\frac{\sigma^2}{\tau^2}.
$$

- Typically, all elements but $\hat{\sigma}^2$ are pre-determined

- Hence: reducing $\hat{\sigma}^2$ is our main lever to reduce sample size and reduce duration 


# How CUPED reduces variance

## The key insight

- Assume that in addition to $Y_i^{obs}$, we also have $X_i^{obs}$, 

- $X_i$ can be any variable that is (i) correlated with $Y_i$ and (ii) independent of treatment allocation

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


## Unbiasedness of the CUPED estimator

- Using our adjusted variable, we have

$$
\begin{align}
\bar{Y}^{cuped}_t 
&= \frac{1}{N_t}\sum_{i:W_i = 1} Y^{cuped}_i
= \frac{1}{N_t}\sum_{i:W_i = 1}\left(Y_i - \theta X_i\right)
= \bar{Y}^{obs}_t - \theta \bar{X}_t \\[5pt]
\bar{Y}^{cuped}_c
&= \frac{1}{N_c}\sum_{i:W_i = 0} Y^{cuped}_i
= \frac{1}{N_c}\sum_{i:W_i = 0}\left(Y_i - \theta X_i\right)
= \bar{Y}^{obs}_c - \theta \bar{X}_c
\end{align}
$$

- So we can rewrite the CUPED estimator as

$$
\begin{align}
\hat{\tau}^{cuped}
&= \bar{Y}^{cuped}_t - \bar{Y}^{cuped}_c \\[5pt]
&= \left(\bar{Y}^{obs}_t - \theta \bar{X}_t\right) 
- \left(\bar{Y}^{obs}_c - \theta \bar{X}_c\right)
\end{align}
$$


## Unbiasedness of the CUPED estimator (cont.)

- To show that $\hat{\tau}$ is unbiased, we have to show that 










<!-- 



Calculating the average outcome for the treatment group, we get


Similarly, for the control group, we have

$$
\bar{\y}^{cuped}_c = \bar{Y}^{obs}_c - \theta \bar{X}_c + \theta\E{X_i | \tii = 0}.
$$


We can now define the CUPED treatment effect estimator as

$$
\begin{align}
\hat{\tau}^{cuped} &= \bar{\y}^{cuped}_t - \bar{\y}^{cuped}_c
\end{align}
$$


**Unbiasedness of CUPED estimator**

The CUPED estimator is unbiased because

$$
\begin{align}
\E{\hat{\tau}^{cuped}}
&= \E{\bar{\y}^{cuped}_t - \bar{\y}^{cuped}_c} \vs
&= \E{\lp{\bar{Y}^{obs}_t - \theta \bar{X}_t + \theta\E{X_i | \tii = 1}} - \lp{\bar{Y}^{obs}_c - \theta \bar{X}_c + \theta\E{X_i | \tii = 0}}} \vs
&= \E{\bar{Y}^{obs}_t - \theta \bar{X}_t + \theta\E{X_i | \tii = 1}} - \E{\bar{Y}^{obs}_c - \theta \bar{X}_c + \theta\E{X_i | \tii = 0}} \vs
&= \lp{\E{\bar{Y}^{obs}_t} - \theta \E{\bar{X}_t} + \theta\E{X_i | \tii = 1}} - \lp{\E{\bar{Y}^{obs}_c} - \theta \E{\bar{X}_c} + \theta\E{X_i | \tii = 0}} \vs
&= \E{\bar{Y}^{obs}_t} - \E{\bar{Y}^{obs}_c} \vs
&= \E{\tee},
\end{align}
$$

which we know to be unbiased from @sec-outcomes.

**CUPED estimator variance**

What remains to be shown is that the variance of the CUPED estimator is smaller than the variance of the unadjusted treatment effect estimator, $\tee$. We derived that variance in @sec-standard-error; given our results there, we need to show that:

$$
\V{\tee^{cuped}} < \V{\tee} =\frac{\vt}{\Nt} + \frac{\vc}{\Nc}.
$$

Let's start by applying the variance operator as usual:

$$
\begin{align}
\V{\hat{\tau}^{cuped}}
&= \V{\bar{\y}^{cuped}_t - \bar{\y}^{cuped}_c} \vs
\mc{Independent samples} &= \V{\bar{\y}^{cuped}_t} - \V{\bar{\y}^{cuped}_c} \vs
&= \V{\bar{Y}^{obs}_t - \theta \bar{X}_t + \theta\E{X_i | \tii = 1}} - \V{\bar{Y}^{obs}_c - \theta \bar{X}_c + \theta\E{X_i | \tii = 0}} \vs
&= \V{\bar{Y}^{obs}_t - \theta \bar{X}_t} - \V{\bar{Y}^{obs}_c - \theta \bar{X}_c} \vs
\end{align}
$$

Focusing on the expression on the left-hand side:

$$
\begin{align}
\V{\bar{Y}^{obs}_t - \theta \bar{X}_t}
&= \V{\frac{1}{\Nt}\sot\yoi - \theta \frac{1}{\Nt}\sot X_i} \vs
&= \frac{1}{\Nt^2}\V{\sot\yoi - \theta \sot X_i} \vs
&= \frac{1}{\Nt^2}\V{\sot\lp{\yoi - \theta X_i}} \vs
\mc{i.i.d sampling} &= \frac{1}{\Nt^2}{\sot\V{\yoi - \theta X_i}} \vs
\mc{i.i.d sampling} &= \frac{1}{\Nt^2}\Nt\V{\yoi - \theta X_i | \tii = 1} \vs
&= \frac{1}{\Nt}\V{\yoi - \theta X_i | \tii = 1} \vs
&= \frac{1}{\Nt}\llp{\vt + \theta^2 \sigma_{X, t}^2 - 2\theta Cov_t(\yoi, X_i)},
\end{align}
$$

where, to keep notation ligher, I define $\vt = \V{\yoi | \tii = 1}$, $\sigma_{X, t}^2 = \V{X_i | \tii = 1}$, and $Cov_t(\yoi, X_i) = Cov(\yoi, X_i | \tii = 1)$.

Using this expression and the similar one for the control group, we can write

$$
\begin{align}
\V{\hat{\tau}^{cuped}} = &\frac{1}{\Nt}\llp{\vt + \theta^2 \sigma_{X, t}^2 - 2\theta Cov_t(\yoi, X_i)} \vs
&+ \frac{1}{\Nc}\llp{\vc + \theta^2 \sigma_{X, c}^2 - 2\theta Cov_c(\yoi, X_i)}.
\end{align}
$$

The goal now is to choose $\theta$ such as to minimise that variance. Taking the derivative with respect to $\theta$, setting the result to zero and rearranging we get:

$$
\theta^* = \frac{\frac{1}{\Nt}Cov_t(\yoi, X_i) + \frac{1}{\Nc}Cov_c(\yoi, X_i)}{\frac{1}{\Nt}\sigma_{X, t}^2 + \frac{1}{\Nc}\sigma_{X, c}^2}.
$$

We could calculate that from the data. However, in practice we usually assume that $\Nt = \Nc$, 


in the context of online experiments, where sample sizes are very large and treatment effects usually small, 








- We can then define $\bar{Y}^{cuped} = \bar{Y} - \theta \bar{X} + \theta \mathbb{E}X$ for both treatment and control groups, and compare avearge outcomes in this adjusted metric.

- Our new estimator is: $\hat{\tau}^{cuped} = \bar{Y}^{cuped}_t - \bar{Y}^{cuped}_c$.

- $\hat{\tau}^{cuped}$ is unbiased since $\mathbb{E}\left[\hat{\tau}^{cuped}\right] = \bar{Y}_t - \bar{Y}_c = \tau$ (proof in appendix below).

- If treatment effects are small (which, in practice, they usually are) and for an optimal choice of $\theta$: $\mathbb{V}\left(\hat{\tau}^{cuped}\right) \simeq \left(\frac{s_t}{N_t} + \frac{s_c}{N_c}\right)\left(1 - \rho^2\right)$, where $\rho$ is the correlation coefficient of $Y$ and $X$.

- Hence: $\frac{\mathbb{V}(\hat{\tau}^{cuped})}{\mathbb{V}(\hat{\tau}^{dif})} = 1 - \rho^2$ -- the higher the correlation between $Y$ and $X$, the more CUPED reduces the variance of our treatment estimate.




$$
Y_i^{cuped} = Y_i - \frac{Cov(Y, X)}{Var(X)} X_i
$$


### How does CUPED work?


CUPED supposes that in addition to an outcome metric $y$, we also have access to another variable, $x$, which is correlated with $y$ but uncorrelated with the treatment assignment of our experiment. Pre-experiment data of the outcome metric is a good candidate for $x$ when it is available -- it's what's commonly used, and where the method gets its name from. With that in hand, notice that we can write

 -- the most obvious candidate that has been found to work well is pre-experiment data of the metric of interest.

We can then create a new variable 

$$
\tilde{y} = y - \theta x,
$$

where -- it turns out -- the optimal choice for $\theta$ is $\frac{cov(y, x)}{var(x)}$, which we can easily calculate from the available data.

This is useful because it can be shown that if we now evaluate our experiment using $\tilde{y}$ instead of $y$, the treatment estimate will be the same but it's standard error will be lower, which will increase power. The standard error of the treatment effect estimate is lower because the variance of $\tilde{y}$ is lower than that of $y$ whenever $cov(y, x) \neq 0$, that is, whenever $x$ and $y$ are indeed correlated. To be precise, we have:

$$
var(\tilde{y}) = var(y)(1 - \rho^2),
$$

where $\rho$ is the Pearson correlation between $x$ and $y$:

$$
\rho = \frac{cov(y, x)}{var(x)var(y)}.
$$



Presentation notes:


$\hat{\tau}^{cuped}$ is unbiased:

$$
\begin{align*}
\mathbb{E}\left[\hat{\tau}^{cuped}\right] &= \mathbb{E}\left[\bar{Y}^{cuped}_t - \bar{Y}^{cuped}_c\right] \\
&= \mathbb{E}\left[\left(\bar{Y}_t - \theta \bar{X}_t + \theta \mathbb{E}X\right) - \left(\bar{Y}_c - \theta \bar{X}_c + \theta \mathbb{E}X\right)\right] \\
&= \mathbb{E}\left[\left(\bar{Y}_t - \theta \bar{X}_t\right) - \left(\bar{Y}_c - \theta \bar{X}_c\right)\right] \\
&= \mathbb{E}\left[\bar{Y}_t - \bar{Y}_c\right] \\
&= \mathbb{E}\left[\frac{1}{N_t}\sum_{\text{i:T=1}}Y_i- \frac{1}{N_c}\sum_{\text{i:T=0}}Y_i\right] \\
&= \frac{1}{N_t} N_t \mathbb{E}Y_t - \frac{1}{N_c} N_c \mathbb{E}Y_c \\
&= \mathbb{E}Y_t - \mathbb{E}Y_c \\
&= \bar{Y}_t - \bar{Y}_c \\
&= \tau
\end{align*}
$$


$\hat{\tau}^{cuped}$ has variance:

$$
\begin{align*}
\mathbb{V}\left(\hat{\tau}^{cuped}\right)
&= \mathbb{V}\left(\bar{Y}^{cuped}_t - \bar{Y}^{cuped}_c\right) \\
&= \mathbb{V}\left(\bar{Y}^{cuped}_t\right) + \mathbb{V}\left(\bar{Y}^{cuped}_c\right) \\
&= \mathbb{V}\left(\bar{Y}_t - \theta \bar{X}_t + \theta \mathbb{E}X\right) + \mathbb{V}\left(\bar{Y}_c - \theta \bar{X}_c + \theta
\mathbb{E}X\right) \\
&= \mathbb{V}\left(\bar{Y}_t - \theta \bar{X}_t\right) + \mathbb{V}\left(\bar{Y}_c - \theta \bar{X}_c\right) \\
&= \frac{1}{N_t}\mathbb{V}\left(Y_t - \theta X_t\right) + \frac{1}{N_c}\mathbb{V}\left(Y_c - \theta X_c\right) \\
&= \frac{1}{N_t}\left[\mathbb{V}(Y_t) + \theta^2 \mathbb{V}(X_t) - 2\theta Cov(Y_t, X_t)\right] + \frac{1}{N_c}\left[\mathbb{V}(Y_c) + \theta^2 \mathbb{V}(X_c) - 2\theta Cov(Y_c, X_c)\right]
\end{align*}
$$

This is minimised for:

$$
\theta^* = \frac{Cov(Y_t, X_t) + Cov(Y_c, X_c)}{\mathbb{V}(X_t) + \mathbb{V}(X_c)}
$$

In practice, a common approach is to pool the data to get:

$$
\begin{align*}
\theta^*_p &= \frac{Cov(Y, X) + Cov(Y, X)}{\mathbb{V}(X) + \mathbb{V}(X)}\\
&= \frac{Cov(Y, X)}{\mathbb{V}(X)},
\end{align*}
$$

and to assume that $\mathbb{V}(X_t) \simeq \mathbb{V}(X_t)$, and $Cov(Y_t, X_t) \simeq Cov(Y_c, X_c)$, which is reasonable as long as the treatment effect is not too large (see discussion towards the end [here](https://alexdeng.github.io/causal/sensitivity.html#vrreg)). If, in addition, we let $\rho = Cor(X, Y)$, then we have

$$
\begin{align*}
\mathbb{V}\left(\hat{\tau}^{cuped}\right) &\simeq \frac{1}{N_t}\left[\mathbb{V}(Y_t) + (\theta^*_p)^2 \mathbb{V}(X) - 2 \theta^*_p Cov(Y, X)\right] + \frac{1}{N_c}\left[\mathbb{V}(Y_c) + (\theta^*_p)^2 \mathbb{V}(X) - 2 \theta^*_p Cov(Y, X)\right]\\
&= \frac{1}{N_t}\left[\mathbb{V}(Y_t) + \left(\frac{Cov(Y, X)}{\mathbb{V}(X)}\right)^2 \mathbb{V}(X) - 2 \left(\frac{Cov(Y, X)}{\mathbb{V}(X)}\right) Cov(Y, X)\right] + \frac{1}{N_c}\left[\mathbb{V}(Y_c) + \left(\frac{Cov(Y, X)}{\mathbb{V}(X)}\right)^2 \mathbb{V}(X) - 2 \left(\frac{Cov(Y, X)}{\mathbb{V}(X)}\right) Cov(Y, X)\right]\\
&= \frac{1}{N_t}\left[\mathbb{V}(Y_t) - \frac{Cov(Y, X)^2}{\mathbb{V}(X)}\right] + \frac{1}{N_c}\left[\mathbb{V}(Y_c) - \frac{Cov(Y, X)^2}{\mathbb{V}(X)}\right]\\
&= \frac{1}{N_t}\left[\mathbb{V}(Y_t) - \frac{\left(\rho\sqrt{\mathbb{V}(X)}\sqrt{\mathbb{V}(Y)}\right)^2}{\mathbb{V}(X)}\right] + \frac{1}{N_c}\left[\mathbb{V}(Y_c) - \frac{\left(\rho\sqrt{\mathbb{V}(X)}\sqrt{\mathbb{V}(Y)}\right)^2}{\mathbb{V}(X)}\right]\\
&= \frac{1}{N_t}\left[\mathbb{V}(Y_t) - \rho^2\mathbb{V}(Y)\right] + \frac{1}{N_c}\left[\mathbb{V}(Y_c) - \rho^2\mathbb{V}(Y)\right]\\
&= \frac{\mathbb{V}(Y_t)}{N_t}(1 - \rho^2) + \frac{\mathbb{V}(Y_c)}{N_c}(1 - \rho^2)\\
&= \left[\frac{\mathbb{V}(Y_t)}{N_t} + \frac{\mathbb{V}(Y_c)}{N_c}\right]\left(1 - \rho^2\right)
\end{align*}
$$


In practice, we use the sample variances $s_t = \frac{1}{N_t - 1}\sum_{\text{i:T=1}}\left(Y_i - \bar{Y}_t^{obs}\right)^2$ and $s_c = \frac{1}{N_c - 1}\sum_{\text{i:T=0}}\left(Y_i - \bar{Y}_c^{obs}\right)^2$ as unbiased estimators for the variances of treatment and control outcomes, and a sample estimate of the correlation coefficient, $\rho$.


**Things to notice**

- The main "trick" CUPED relies on for unbiasedness is the fact that we don't actually have to know $\mathbb{E}X$ to obtain an unbiased estimator since it cancels out when we take the difference of two CUPED-adjusted variables.

- Any fixed value of $\theta$ will give us an unbiased estimator of $\tau$, so pooling the data and assuming equal variances and covariances in the treatment and control groups, as we did to calculate the variance, effect the degree of variance reduction only. If we didn't make these assumptions, the factor by which CUPED reduces variance would be a more complicated term than $\left(1 - \rho^2\right)$, involving separte variances and covariances from the treatment and control groups.


### What does effect of CUPED depend on?


### Features

- Also permits non-linear adjustments (i.e. not reliant on linearity assumptions in OLS)

- Reduces biase (see statsic post)


### Questions

Questions:

- [ ] Why does fillna(y) not increase variance
- [ ] What happens if pre and post perfectly correlated
- [ ] How much do actual metric values change due to adjustment


### Implementation challenges

### Is CUPED regression adjustment?

todo:
- Incorporate Rice content on prediction and MSE (chapter 4.4 and ipad notes), which exactly gets us the CUPED result, again showing that CUPED is a re-invention of linear regression and standard stats 

- Is CUPED regression adjustment? Identical to regression only in simple case (show FWL link -- have separate post on understanding FWL with relevant regression examples)

- Take inclusion of constant into accound (centering variables, but doesn't change correlations)

- Show that in multiple regression, var(Y_adjusted) = var(y_unadjusted)(1 - R^2) -- so, CUPED result is just a specieal case where k = 1, in which case R^2 = rho. 

- I think it really is. CUPED can be extended to (make notation consistent with CUPED)

$$
y' = y - \theta \bar{f(X)} + \theta E(f(X))
$$

- In above, it can be shown that optimal $f(X) = E(Y|X)$ (show this). CUPED uses best linear predictor. CUPAC extends this to non-linear predictors, generating $\hat{y} = g(X) = E(Y|X)$. This is an example of using a non-linear function of X as Deng points out is possible. But if you do this, theta is still the OLS coefficient, so it's still equivalent to just sticking g(X) into the regression as a covariate.

- The motivation for CUPED seems to be a bit of a strawman: that regression adjustment relies on assumption that expectation of Y conditional on X is linear. Imbens and Rubin in 7.5 show that this is not required. Neither is homoskedasticity, or, rather, this should hold anyways given randomisation. Study chapter 7.

- As pointed out in @tang2000control, the Deng argument that you don't need linear assumptions in CUPED seems to be inspired by the Friedman critique of OLS for experiments. 

- So the CUPED motivation might not be a strawem as much as a result of the debate in statistics about whether you should use OLS for experiment analysis or not. This is probs the way I want to frame the entire issue -- review debate (key point of Friedman critique, Lin's repsonse, Imbens and Rubin's take, and then discuss cuped and regression adjustment in that light). Basically, if you follow Lin, then cuped is just regression adjustment. If you follow Friedman, then you shouldn't do regression adjustment and use cuped. But then do practical comparisons and show that you get the same results in practice, which seems to show that using linear regression clearly works.


It turns out that in the simple cases discussed above, it doesn't -- the two approaches are identical! Seeing why requires a few steps.

First, we know (from the Frisch-Waugh-Lowell [theorem](https://en.wikipedia.org/wiki/Frisch%E2%80%93Waugh%E2%80%93Lovell_theorem)) that if we were to estimate the alternative model 

$$
\tilde{y}_i = \alpha + \beta_1^* \tilde{d}_i + \epsilon_i,
$$

where $\tilde{y}_i$ is the residual from regressing $y$ on $x$, and $\tilde{d}_i$ the residual from regressing $d$ on $x$, we would find that $\beta_1^* = \beta_1$. That is, the two models are identical.

Second, to obtain $\tilde{y}$, we first estimate

$$
y = \alpha + \delta x_i + u_i,
$$

and then calculate $\tilde{y} = y - \delta x$ (the calculation of $\tilde{d}_i$ works analogously). Given that this is a simple regression model, we know that $\delta = \frac{cov(y, x)}{var(x)}$ so that 

$$
\tilde{y} = y - \frac{cov(y, x)}{var(x)}x.
$$

Finally, above in our discussion of CUPED we have seen that the CUPED-adjusted outcome metric $\tilde{y}$ is defined in exactly the same way. Hence, to evaluate an experiment with a CUPED-adjusted outcome, we would estimate the model:

$$
\tilde{y}_i = \alpha + \beta^* d_i + \epsilon_i^*,
$$

Notice that the only difference to model (2) is that we don't adjust the treatment assignment -- we use $d_i$ instead of $\tilde{d}_i$. But if the treatment assignment is random, then $cov(d, x) = 0$ so that the adjustment has no effect and we have $\tilde{d}_i = d_i$. Hence, the two approaches are the same.

In general, regression adjustment and CUPED are identical if two conditions hold: (1) the treatment indicator is independent of $x$, and (2) we use a linear CUPED adjustment. In the context of experimentation, where treatment is random, and with the classical (linear) CUPED adjustment discussed above, this is always the case.

The reason why in practice we get a don't get the exact same result is that the covariance of $d$ and $x$ is only approximately 0, hence providing very similar, but not identical results.



### Is CUPED DiD?

- Is CUPED DiD? (based on Courthoud) -- same if theta = 1


### Non-linear extensions


### Blog post notes

CUPED is a re-invention of multiple linear regression. Evan Miller ([here](https://www.evanmiller.org/you-cant-spell-cuped-without-frisch-waugh-lovell.html)) and Matteo Courthoud ([here](https://towardsdatascience.com/understanding-cuped-a822523641af)) make similar points in their excellent posts on the topic, but -- given my starting point -- neither quite helped me fully understand what is going on. This post is my attempt to do that.

In particular, I think that to really understand the connection between multiple linear regression and CUPED, you have to understand the linear algebra of the Frisch-Waugh-Lowell theorem (FWL) rather than just knowing that that theorem says, and to understand that, you have to understand the concept of a projection.




### Useful resources

- [The original CUPED paper](https://www.exp-platform.com/Documents/2013-02-CUPED-ImprovingSensitivityOfControlledExperiments.pdf) -- the original paper

- [Variance reduction section of Deng's causal inference book](https://alexdeng.github.io/causal/sensitivity.html#vrreg) -- more in-depth discussion of some aspects of CUPED and its link to regression adjustment

- [Improving the Sensitivity of Online Controlled
Experiments: Case Studies at Netflix](https://www.kdd.org/kdd2016/papers/files/adp0945-xieA.pdf)

- [How Booking.com increases the power of online experiments with CUPED](https://booking.ai/how-booking-com-increases-the-power-of-online-experiments-with-cuped-995d186fff1d)

- [You can't spell CUPED without Frisch-Waugh-Lovell](https://www.evanmiller.org/you-cant-spell-cuped-without-frisch-waugh-lovell.html) -- good post exploring link to FWL theorem

- [Understanding CUPED](https://towardsdatascience.com/understanding-cuped-a822523641af) -- good post exploring link to multiple regression (also using FWL theorem) and DiD.

- [Reducing variance in A/B testing with CUPED](https://bytepawn.com/reducing-variance-in-ab-testing-with-cuped.html#reducing-variance-in-ab-testing-with-cuped)

- [CUPED on Statsig](https://blog.statsig.com/cuped-on-statsig-d57f23122d0e)






## Stratification

TODO

### Useful resources

- [Deng et al. 2013 -- original CUPED paper](https://www.exp-platform.com/Documents/2013-02-CUPED-ImprovingSensitivityOfControlledExperiments.pdf) -- the original paper

- [Five ways to reduce variance in A/B testing](https://bytepawn.com/five-ways-to-reduce-variance-in-ab-testing.html#five-ways-to-reduce-variance-in-ab-testing)



## Regression adjustment

Regression adjustment reduces variance by adding additional regressors to the regression model used to evaluate an experiment in order to reduce residual variance.

**How it works**

To evaluate an experiment where we have, for each unit $i$, an outcome metric $y_i$ and a treatment assignment indicator $d_i$ we would estimate the following linear regression model using OLS:

$$
y_i = \alpha + \beta d_i + \epsilon_i,
$$

where $\epsilon_i$ is the error term, and where the estimate of $\beta$ is the estimate of our average treatment effect. If we have an additional variable, $x_i$, that is correlated with $y_i$ but uncorrelated with $d_i$, we can add that to the right hand side of our regression model and estimate:

$$
y_i = \alpha + \beta_1 d_i + \beta_2 x_i + \mu_i.
$$

If $x$ is uncorrelated with the treatment assignment then $\beta = \beta_1$, so the average treatment effect estimate will remain unchanged, which is good. And if $x$ is correlated with $y$, then the standard error of the average treatment effect estimate will again be lower, which increases power.

### Useful resources

- Imbens & Rubin, Causal Inference for Statistics, Social, and Biomedical Sciences, Chapter 7 [link](https://www.cambridge.org/core/books/causal-inference-for-statistics-social-and-biomedical-sciences/71126BE90C58F1A431FE9B2DD07938AB)


## CUPAC

- CUPED was designed by folks at Doordash [@tang2000control] to reduce the duration of their switchback experiments, which -- according to their paper -- it did by about 25 percent.

- CUPED can be extended to (make notation consistent with CUPED)

$$
y' = y - \theta \bar{f(X)} + \theta E(f(X))
$$

- In above, it can be shown that optimal $f(X) = E(Y|X)$ (show this).

- CUPED, which is effectively regression adjustment, uses best linear predictor.

- CUPAC extends this to non-linear predictors, generating $\hat{y} = g(X) = E(Y|X)$.

### Advantages

- Can be used for metrics that have no pre-experiment data (if you have variables that correlate with the metric and are unaffected by the treatment)

### Thoughts

- There are two approaches: predict the experiment-time outcome or predict the pre-experiment value.

- If you do the former, then you need features that are unaffected by the treatment. This means that for reach metric and each experiment, you need to collect features that meet this requirement. This will be different for each metric and experiment because for many features, whether or not the feature is impacted by the treatment depends on the specific experiment (i.e. where in the funnel the feature is active). This could be solved by finding, for each metric of interest, a set of features that are always independent of the treatment (such as distance between restaurant and customer, or the type of browser used by a customer), but it's not at all clear that finding a set of features with good predictive properties is possible for all our metrics. Hence, building this into a pipeline in an automated way would be an enormous endeavour, if it's possible at all.

- This approach is thus really only viable in a very specialised setting where you keep running the same type of experiment, and thus have to build and train the model manually and only once (this is how it's being used for courier experiments).

- To ensure that features really are independent of treatment condition, they actively monitor correlations for each running experiment.

- @tang2000control gives the example of reducing average daily delivery time, where a delivery-level covariate that is unaffected by treatment is distance between restaurant and customer. 


### Useful resources

- [Control Using Predictions as Covariates in Switchback Experiments]([file:///Users/fabian.gunzinger/Downloads/code_final_draft1.pdf](https://www.researchgate.net/publication/345698207_Control_Using_Predictions_as_Covariates_in_Switchback_Experiments))


## Other methods

- [Variance Reduction Using In-Experiment Data: Efficient and Targeted Online Measurement for Sparse and Delayed Outcomes](https://alexdeng.github.io/public/files/kdd2023-inexp.pdf)


## Useful resources

- [Five ways to reduce variance in A/B testing](https://bytepawn.com/five-ways-to-reduce-variance-in-ab-testing.html#five-ways-to-reduce-variance-in-ab-testing)

- [Online Experiments Tricks — Variance Reduction](https://towardsdatascience.com/online-experiments-tricks-variance-reduction-291b6032dcd7)

- [CUPED, CUPAC, and Other Ways to Reduce Variance in an Experiment](https://j-sephb-lt-n.github.io/exploring_statistics/cuped_cupac_and_other_variance_reduction_techniques.html)

- [Don't use a t-test for A/B testing](https://towardsdatascience.com/dont-use-a-t-test-for-a-b-testing-e4d2ef7ab9b6)

- [Variance Reduction in Experiments — Part 1: Intuition -- see also part 2](https://towardsdatascience.com/variance-reduction-in-experiments-part-1-intuition-68b270a0df71)



 -->


