[[_Experimentation]]


- [[Mode of inference]] used throughout is randomisation-based rather than sampling-based: inference is directly justified by randomisation, not by assumption that sample of units in our experiment is a random sample of a larger population.


## Estimand

Individual-level causal effect is defined as:

$\tau_i = Y_i(1)$ - $Y_i(0)$

In a setting with $i = 1, \dots, n$ units with fixed potential outcomes $Y_i(0)$ and $Y_i(1)$, where the only random component is the random assignment, captured by the assignment vector $W$, Neyman was interested in the population average treatment effect:

$$
\tau = \frac{1}{n}\sum_{i=1}^n \left(Y_i(1) - Y_i(0)\right) = \bar{Y}(1) - \bar{Y}(0),
$$

where

$$
\bar{Y}(1) = \frac{1}{n}\sum_{i=1}^n Y_i(1) \qquad \bar{Y}(0) = \frac{1}{n}\sum_{i=1}^n Y_i(0).
$$
{#eq-neyman-estimand}

This is our estimand of interest.

## Estimator

If we have data from a completely randomised experiment (CRE) in which a fixed number of $n_t = \sum_{i=1}^n W_i$ units are allocated to treatment and the remaining $n_c = \sum_{i=1}^n (1-W_i)$ to control, then a natural estimator for @eq-neyman-estimand is the difference in the means of the treatment and control units:

$$
\hat{\tau}^{\text{dm}} = \bar{Y}_t - \bar{Y}_c.
$$ {#eq-neyman-estimator}

where

$$
\bar{Y}_t = \frac{1}{n_t}\sum_{i:W_i=1} Y_i \qquad \bar{Y}_c = \frac{1}{n_c}\sum_{i:W_i=0} Y_i
$$


## Unbiasedness

This section contains a step-by-step version of the derivation covered in Appendix A of chapter 6 in @imbens2015causal. Their derivation is complete but can be hard to follow. The derivation here remains tedious but should be easy to follow.

We start with the difference-in-means estimator as defined above
$$
\hat{\tau}^{\text{dm}} 
= \bar{Y}_t - \bar{Y}_c 
= \frac{1}{n_t}\sum_{i:W_i=1} Y_i - \frac{1}{n_c}\sum_{i:W_i=0} Y_i.
$$
Using the definitions of $n_t$ and $n_c$ in terms of $W_i$ from above, we can rewrite this as

$$
\begin{align}
\hat{\tau}^{\text{dm}}
&= \frac{1}{n_\text{t}}\sum_{i=1}^{n}W_iY_i - \frac{1}{n_\text{c}}\sum_{i=1}^{n}(1-W_i)Y_i \\
&= \frac{1}{n}\sum_{i=1}^{n}\left(\frac{n}{n_\text{t}}W_iY_i - \frac{n}{n_\text{c}}(1-W_i)Y_i\right) \\
\end{align}
$$
Imbens and Rubin suggest working with a centered treatment indicator to simplify the variance calculation. So let's define
$$
D_i = W_i - \frac{n_t}{n} = 
\begin{cases}
\frac{n_c}{n}   & \quad \text{if } W_i = 1 \\
-\frac{n_t}{n}  & \quad \text{if } W_i = 0
\end{cases}
$$
Because in a completely randomised experiment $n_t$, $n_c$, and $n$ are fixed and $\mathbb{E}[W_i] = \frac{n_t}{n}$, we have:
$$
\mathbb{E}[D_i]
= \mathbb{E}\left[W_i - \frac{n_t}{n}\right]
= \mathbb{E}[W_i] - \frac{n_t}{n}
= \frac{n_t}{n} - \frac{n_t}{n}
= 0
$$
and
$$
\begin{align}
\mathbb{V}(D_i) 
&= \mathbb{E}\left[D_i - \mathbb{E}[D_i]\right]^2 \\[5pt]
&= \mathbb{E}[D_i - 0]^2 \\[5pt]
&= \mathbb{E}[D_i]^2 \\[5pt]
&= \mathbb{E}\left[W_i^2 - 2W_i\frac{n_t}{n} + \frac{n_t^2}{n^2}\right] \\[5pt]
&= \mathbb{E}[W_i^2] - 2\mathbb{E}[W_i]\frac{n_t}{n} + \frac{n_t^2}{n^2} \\[5pt]
&= \frac{n_t}{n} - 2\frac{n_t^2}{n^2} + \frac{n_t^2}{n^2} \\[5pt]
&= \frac{n_t}{n} - \frac{n_t^2}{n^2} \\[5pt]
&= \frac{n_t n - n_t^2}{n^2} \\[5pt]
&= \frac{n_t(n - n_t)}{n^2} \\[5pt]
&= \frac{n_t n_c}{n^2} \\[5pt]
\end{align}
$$

The cross-product distribution is:

$$
P_{W} = (D_{i} \times D_{j}) =
\begin{cases} 
\frac{n_t (n_t - 1)}{n(n-1)} & 
\text{if } d = \frac{n_c^2}{n^2} \Leftrightarrow W_i = W_j = 1\\[5pt]
2\frac{n_t n_c}{n(n-1)} & 
\text{if } d = -\frac{n_t n_c}{n^2} \Leftrightarrow W_i = 1, W_j = 0\\[5pt]
\frac{n_c (n_c - 1)}{n(n-1)} & 
\text{if } d = \frac{n_t^2}{n^2} \Leftrightarrow W_i = W_j = 0\\[5pt]
0 & 
\text{otherwise,}
\end{cases}
$$

leading to:

$$ 
E_W[D_i \times D_j] = 
\begin{cases} 
\frac{n_t n_c}{n^2} & \text{if } i = j\\[5pt]
-\frac{n_t n_c}{n^2 (n-1)} & \text{if } i \neq j\\[5pt]
\end{cases}
$$

We can derive these expected values as follows:

For $i = j$ we have:
$$
\begin{array}{rl}
E_W[D_i \times D_i]
&= E_W[D_i^2] & \\[5pt]
&= V(D_i) & \text{since $\mathbb{E}[D_i] = 0$} \\[5pt]
&= \frac{n_t n_c}{n^2} & \text{from derivation of $\mathbb{V}(D_i)
$}
\end{array}
$$


For $i \neq j$ we have:

$$
\begin{align}
E_W[D_i \times D_j]
&= P(d_{W_i = W_j = 1}) d_{W_i = W_j = 1}
+ P(d_{W_i = 1, W_j = 0}) d_{W_i =1,  W_j = 0}
+ P(d_{W_i = W_j = 0}) d_{W_i = W_j = 0} \\[5pt]
&= \frac{n_t (n_t - 1)}{n(n-1)} \frac{n_c^2}{n^2}
- 2\frac{n_t n_c}{n(n-1)} \frac{n_t n_c}{n^2}
+ \frac{n_c (n_c - 1)}{n(n-1)} \frac{n_t^2}{n^2}\\[5pt]
\end{align}
$$

** == I'm here == **




Unbiasedness...

Variance ... (app 6.A)
