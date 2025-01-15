[[_Experimentation]]

- [[Mode of inference]] used throughout is randomisation-based rather than sampling-based: inference is directly justified by randomisation, not by assumption that sample of units in our experiment is a random sample of a larger population.

## The Rubin Causal Model

## Assignment mechanisms


The individual-level causal effect is defined as:

$\tau_i = Y_i(1)$ - $Y_i(0)$

If we have a (finite) sample of $n$ units in our experiment, then the average treatment effect (ATE) is defined as:

$$
\tau_{\text{fs}} = \frac{1}{n}\sum_{i=1}^{n}\left(Y_i(1) - Y_i(0)\right)
$$
If our experiment sample is a random sample from a larger super population of size $N$, then the average treatment effect for that population is defined as:

$$
\tau_{\text{sp}} = \frac{1}{N}\sum_{i=1}^{N}\left(Y_i(1) - Y_i(0)\right)
$$

## Completely randomised experiment

## Full derivation of unbiasedness and variance of difference-in-means estimator

This section contains a (small) step-by-step version of the derivation covered in Appendix A of chapter 6 in @imbens2015causal. Their derivation is complete but they sometimes take steps that -- at least for me -- took a while to follow. The solution here aims to be easy to follow, though it remains tedious.

## The setup of a completely randomised experiment

- Out of our entire experiment sample of size $n$ we randomly assign a fixed number of units $n_t$ to treatment, and the remaining $n_t = n - n_c$ units to control.

The [[Difference in means estimator]] is

$$
\begin{align}
\hat{\tau}^{\text{dif}}
&= \frac{1}{n_\text{t}}\sum_{i=1}^{n}W_iY_i - \frac{1}{n_\text{c}}\sum_{i=1}^{n}(1-W_i)Y_i \\
&= \frac{1}{n}\sum_{i=1}^{n}\left(\frac{n}{n_\text{t}}W_iY_i - \frac{n}{n_\text{c}}(1-W_i)Y_i\right) \\
\end{align}
$$
Imbens and Rubin suggest working with a centered treatment indicator to simplify the variance calculation:
$$
D_i = W_i - \frac{n_t}{n} = 
\begin{cases}
\frac{n_c}{n}   & \quad \text{if } W_i = 1 \\
-\frac{n_t}{n}  & \quad \text{if } W_i = 0
\end{cases}
$$
Because in a completely randomised experiment $n_t$ and $n$ are fixed and $\mathbb{E}[W_i] = \frac{n_t}{n}$, we have:
$$
\mathbb{E}[D_i]
= \mathbb{E}\left[W_i - \frac{n_t}{n}\right]
= \mathbb{E}[W_i] - \frac{n_t}{n}
= \frac{n_t}{n} - \frac{n_t}{n}
= 0
$$
and
$$
\mathbb{V}(D_i) = \mathbb{E}[D_i - \mathbb[]]
$$






Unbiasedness...

Variance ... (app 6.A)
