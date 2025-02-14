[[_Experimentation]]


- [[Mode of inference]] used throughout is randomisation-based rather than sampling-based: inference is directly justified by randomisation, not by assumption that sample of units in our experiment is a random sample of a larger population.

This section contains a step-by-step version of the derivation covered in Appendix A of chapter 6 in @imbens2015causal. Their derivation is complete but can be hard to follow. This version here fills in the missing steps to make it easier to follow along, but it remains tedious.


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

To evaluate how useful an estimator is we generally have two questions: whether we can expect the right answer on average and how precise that answer is. We tackle these in turn.

To do this, we rewrite the estimator in a form that will be more convenient to work with later.

We start with the difference-in-means estimator as defined above and rewrite it in a form that will be more convenient to work with later

$$
\begin{align}
\hat{\tau}^{\text{dm}}
&= \bar{Y}_t - \bar{Y}_c & \\[5pt]

&= \frac{1}{n_t}\sum_{i:W_i=1} Y_i - \frac{1}{n_c}\sum_{i:W_i=0} Y_i & \\[5pt]

&= \frac{1}{n_\text{t}}\sum_{i=1}^{n}W_iY_i - \frac{1}{n_\text{c}}\sum_{i=1}^{n}(1-W_i)Y_i
&\\[5pt]

&= \frac{1}{n}\sum_{i=1}^{n}\left(\frac{n}{n_\text{t}}W_iY_i - \frac{n}{n_\text{c}}(1-W_i)Y_i\right) 
& \text{multiply by }\frac{n}{n}\\[5pt]

&= \frac{1}{n}\sum_{i=1}^{n}\left(\frac{n}{n_\text{t}}W_iY_i(1) - \frac{n}{n_\text{c}}(1-W_i)Y_i(0)\right) 
& \text{SUTVA}\\[5pt]

\end{align}
$$


Something we'll frequently use:
$$
1 - \frac{n_t}{n} = \frac{n}{n} - \frac{n_t}{n} = \frac{n - n_t}{n} = \frac{n_c}{n}
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

How can we calculate the elements of $P_W$? For the first case where $W_i = W_j = 1$, we know from the definition that $D_i = \frac{n_c}{n}$ and $D_j = \frac{n_c}{n}$, which gives us $d = D_i \times D_j = \frac{n_c^2}{n^2}$. To find the probability, remember that $n_t$ is fixed, so that $P(W_i = 1) = \frac{n_t}{n}$ and $P(W_j = 1|W_i = 1) = \frac{n_t - 1}{n-1}$ (because with $i$ allocated to treatment, there is now one less slot). Multiplying gives us the result.

The expected values of the cross-product distribution are: 

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
&= \frac{n_t(n_t - 1)n_c^2 - 2n_t^2 n_c^2 + n_c(n_c-1) n_t^2}{n^3(n-1)} \\[5pt]
&= \frac{n_t^2 n_c^2 - n_t n_c^2 - 2n_t^2 n_c^2 + n_c^2 n_t^2 - n_c n_t^2}{n^3(n-1)} \\[5pt]
&= \frac{- n_t n_c^2 - n_c n_t^2}{n^3(n-1)} \\[5pt]
&= \frac{- n_t n_c (n_c + n_t)}{n^3(n-1)} \\[5pt]
&= \frac{- n_t n_c n}{n^3(n-1)} \\[5pt]
&= \frac{- n_t n_c}{n^2(n-1)} \\[5pt]
\end{align}
$$


Expressing our difference-in-means estimator in terms of $D_i$ gives us:

$$
\begin{align}
\hat{\tau}^{\text{dm}}

&= \frac{1}{n}\sum_{i=1}^{n}\left(\frac{n}{n_\text{t}}W_iY_i(1) - \frac{n}{n_\text{c}}(1-W_i)Y_i(0)\right) 
& \\[5pt]

&= \frac{1}{n}\sum_{i=1}^{n}\left(\frac{n}{n_\text{t}}\left(D_i + \frac{n_t}{n}\right)Y_i(1) - \frac{n}{n_\text{c}}\left(1 - D_i - \frac{n_t}{n}\right))Y_i(0)\right)
& \text{using } W_i = D_i + \frac{n_t}{n} \\[5pt]

&= \frac{1}{n}\sum_{i=1}^{n}\left(\frac{n}{n_\text{t}}\left(D_i + \frac{n_t}{n}\right)Y_i(1) - \frac{n}{n_\text{c}}\left(\frac{n_c}{n} - D_i\right)Y_i(0)\right)
& \\[5pt]

&= \frac{1}{n}\sum_{i=1}^{n}\left(\left[Y_i(1) + \frac{n}{n_t}D_iY_i(1)\right] - \left[Y_i(0) - \frac{n}{n_c}D_iY_i(0)\right]\right)
& \\[5pt]

&= \frac{1}{n}\sum_{i=1}^{n}\left(Y_i(1) + \frac{n}{n_t}D_iY_i(1) - Y_i(0) + \frac{n}{n_c}D_iY_i(0)\right)
& \\[5pt]

&= \frac{1}{n}\sum_{i=1}^{n}\left(Y_i(1) - Y_i(0) + \frac{n}{n_t}D_iY_i(1)  + \frac{n}{n_c}D_iY_i(0)\right)
& \\[5pt]

&= \frac{1}{n}\sum_{i=1}^{n}\left(Y_i(1) - Y_i(0)\right) + \frac{1}{n}\sum_{i=1}^{n}D_i\left(\frac{n}{n_t}Y_i(1)  + \frac{n}{n_c}Y_i(0)\right)
& \\[5pt]

&= \tau + \frac{1}{n}\sum_{i=1}^{n}D_i\left(\frac{n}{n_t}Y_i(1)  + \frac{n}{n_c}Y_i(0)\right)
& \\[5pt]

\end{align}
$$

{#eq-neyman-two-parts}

## Unbiasedness

An estimator is unbiased if, in expectation, it equals the estimand of interest. To show that  $\hat{\tau}^{\text{dm}}$ is unbiased we thus need to show that  $\hat{\tau}^{\text{dm}} = \tau$.  Given that the potential outcomes are fixed (see @sec-modeofinference) and given that $E[D_i] = 0$ (as shown above), taking the expectation of @eq-neyman-two-parts is all we need to do for this:[^fixed_values]

$$
\begin{align}
\mathbb{E}\left[\hat{\tau}^{\text{dm}}\right]
&= \mathbb{E}\left[\tau + \frac{1}{n}\sum_{i=1}^{n}D_i\left(\frac{n}{n_t}Y_i(1)  + \frac{n}{n_c}Y_i(0)\right)\right]\\[5pt]
&= \mathbb{E}\left[\tau\right] + \mathbb{E}\left[\frac{1}{n}\sum_{i=1}^{n}D_i\left(\frac{n}{n_t}Y_i(1)  + \frac{n}{n_c}Y_i(0)\right)\right]
& \text{Linearity of } \mathbb{E}\\[5pt]
&= \tau + \mathbb{E}[D_i]\left[\frac{1}{n}\sum_{i=1}^{n}\left(\frac{n}{n_t}Y_i(1)  + \frac{n}{n_c}Y_i(0)\right)\right]
& \tau, n, n_t, n_c, Y_i(1), Y_i(0) \text{ are fixed} \\[5pt]
&= \tau
& \mathbb{E}[D_i] = 0
\end{align}
$$
{#eq-neyman-unbiased}

The above result reassures us that we get the right result on average, and that our estimates will not be systematically wrong (or *biased*).

The next question is how precise our estimate it.

## Variance

We again start from @eq-neyman-two-parts:

$$
\begin{align}
\hat{\tau}^{\text{dm}} 
&= \tau + \frac{1}{n}\sum_{i=1}^{n}D_i\left(\frac{n}{n_t}Y_i(1)  + \frac{n}{n_c}Y_i(0)\right)
\end{align}
$$
The only random element is $D_i$, the variance is equal to the second term. To simplify the notation, we define:

$$
Y_i^+ = \frac{n}{n_t}Y_i(1)  + \frac{n}{n_c}Y_i(0) 
$$
So that we can write:

$$
\begin{align}
\mathbb{V}\left(\hat{\tau}^{\text{dm}}\right)
&= \mathbb{V}\left(\tau + \frac{1}{n}\sum_{i=1}^{n}D_i\left(\frac{n}{n_t}Y_i(1)  + \frac{n}{n_c}Y_i(0)\right)\right)\\[5pt]
&= \mathbb{V}\left(\frac{1}{n}\sum_{i=1}^{n}D_i\left(\frac{n}{n_t}Y_i(1)  + \frac{n}{n_c}Y_i(0)\right)\right)\\[5pt]
&= \mathbb{V}\left(\frac{1}{n}\sum_{i=1}^{n}D_iY_i^+\right)\\[5pt]
&= \frac{1}{n^2}\mathbb{V}\left(\sum_{i=1}^{n}D_iY_i^+\right)\\[5pt]
&= \frac{1}{n^2}\mathbb{E}\left[\left(\sum_{i=1}^{n}D_iY_i^+ - \mathbb{E}\left[\sum_{i=1}^{n}D_iY_i^+\right]\right)^2\right] & \mathbb{V}(X) = E[(X - E[X])^2]\\[5pt]
&= \frac{1}{n^2}\mathbb{E}\left[\left(\sum_{i=1}^{n}D_iY_i^+\right)^2\right] & \mathbb{E}\left[\sum_{i=1}^{n}D_iY_i^+\right]=0 \\[5pt]
\end{align}
$$


This is our starting point. Expanding the expression and doing a lot of algebra, we get:

$$
\begin{align}
\mathbb{V}\left(\hat{\tau}^{\text{dm}}\right)

&= \frac{1}{n^2}\mathbb{E}\left[\left(\sum_{i=1}^{n}D_iY_i^+\right)^2\right] \\[5pt]

&= \frac{1}{n^2}\mathbb{E}\left[\left(\sum_{i=1}^{n}D_iY_i^+\right)\left(\sum_{j=1}^{n}D_jY_j^+\right)\right] \\[5pt]

&= \frac{1}{n^2}\mathbb{E}\left[\sum_{i=1}^{n}\sum_{j=1}^{n}D_iY_i^+D_jY_j^+\right] & \text{distributive property of sum}\\[5pt]

&= \frac{1}{n^2}\mathbb{E}\left[\sum_{i=1}^{n}D_i^2(Y_i^+)^2\right]
+ \frac{1}{n^2}\mathbb{E}\left[\sum_{i=1}^{n}\sum_{i\neq j}D_iY_i^+D_jY_j^+\right] \\[5pt]

&= \frac{1}{n^2}\sum_{i=1}^{n}(Y_i^+)^2\mathbb{E}\left[D_i^2\right]
+ \frac{1}{n^2}\sum_{i=1}^{n}\sum_{i\neq j}Y_i^+Y_j^+\mathbb{E}\left[D_iD_j\right] \\[5pt]

&= \frac{1}{n^2}\sum_{i=1}^{n}(Y_i^+)^2\left(\frac{n_t n_c}{n^2}\right)
+ \frac{1}{n^2}\sum_{i=1}^{n}\sum_{i\neq j}Y_i^+Y_j^+
\left( -\frac{n_t n_c}{n^2 (n-1)}\right) & \text{properties of } D_i\\[5pt]

&= \frac{n_t n_c}{n^4}\sum_{i=1}^{n}(Y_i^+)^2
- \frac{n_t n_c}{n^4 (n-1)}\sum_{i=1}^{n}\sum_{i\neq j}Y_i^+Y_j^+
\end{align}
$$

The next step requires some involved manipulation of both terms on the right hand side, which we're going to do step-by-step, focusing on one term at a time.

We start with the first of those terms. The complement of the second term on the right is $\left(\frac{n_t n_c}{n^4 (n-1)}\sum_{i=1}^{n}\sum_{i=j}Y_i^+Y_j^+\right)$, which we now add and subtract to get

$$
\begin{align}
\mathbb{V}\left(\hat{\tau}^{\text{dm}}\right)
&= \underbrace{\frac{n_t n_c}{n^4}\sum_{i=1}^{n}(Y_i^+)^2}_\text{A}
- \underbrace{\frac{n_t n_c}{n^4 (n-1)}\sum_{i=1}^{n}\sum_{i\neq j}Y_i^+Y_j^+}_\text{B}  \\[5pt]
&\qquad 
+\underbrace{\left(\frac{n_t n_c}{n^4 (n-1)}\sum_{i=1}^{n}\sum_{i=j}Y_i^+Y_j^+\right)}_\text{C}
- \underbrace{\left(\frac{n_t n_c}{n^4 (n-1)}\sum_{i=1}^{n}\sum_{i=j}Y_i^+Y_j^+\right)}_\text{D}.
\end{align}
$$


Now, using the fact that
$$
\sum_{i=1}^{n}\sum_{i=j}Y_i^+Y_j^+ = \sum_{i=1}^{n}(Y_i^+)^2,
$$
we replace $C$ we artificially added above, add it to $A$, and bring the fractions to a common denominator to get:

$$
\begin{align}
\mathbb{V}\left(\hat{\tau}^{\text{dm}}\right)
&= \underbrace{\frac{n_t n_c}{n^4}\sum_{i=1}^{n}(Y_i^+)^2}_\text{A}
+\underbrace{\left(\frac{n_t n_c}{n^4 (n-1)}\sum_{i=1}^{n}\sum_{i=j}Y_i^+Y_j^+\right)}_\text{C}
- \text{B} - \text{D} \\[5pt]

&= \underbrace{\frac{n_t n_c}{n^4}\sum_{i=1}^{n}(Y_i^+)^2}_\text{A}
+\underbrace{\left(\frac{n_t n_c}{n^4 (n-1)}\sum_{i=1}^{n}(Y_i^+)^2\right)}_\text{C}
- \text{B} - \text{D} \\[5pt]

&= \left(\frac{n_t n_c}{n^4} + \frac{n_t n_c}{n^4 (n-1)}\right)\sum_{i=1}^{n}(Y_i^+)^2
- \text{B} - \text{D} \\[5pt]

&= \left(\frac{(n-1) n_t n_c + n_t n_c}{n^4 (n-1)}\right)\sum_{i=1}^{n}(Y_i^+)^2
- \text{B} - \text{D} \\[5pt]

&= \left(\frac{n_t n_c}{n^3 (n-1)}\right)\sum_{i=1}^{n}(Y_i^+)^2
- \text{B} - \text{D} \\[5pt]
\end{align}
$$


That gives us the new version of the first term we need.

**Next, the second term, B above -- I'm here**


Finally, using the fact that 

$$
\sum_{i=1}^{n}\sum_{i\neq j}Y_i^+Y_j^+ 
+ \sum_{i=1}^{n}\sum_{i=j}Y_i^+Y_j^+
= \sum_{i=1}^{n}\sum_{j=1}^{n}Y_i^+Y_j^+,
$$
we rewrite combine the last two terms to get:





$$
\begin{align}
\mathbb{V}\left(\hat{\tau}^{\text{dm}}\right)



&= \left(\frac{n_t n_c}{n^4} + \frac{n_t n_c}{n^4 (n-1)}\right)\sum_{i=1}^{n}(Y_i^+)^2
- \frac{n_t n_c}{n^4 (n-1)}\sum_{i=1}^{n}\sum_{j=1}^{n}Y_i^+Y_j^+  \\[5pt]

&=\frac{(n-1)n_t n_c + n_t n_c}{n^4 (n-1)}\sum_{i=1}^{n}(Y_i^+)^2
- \frac{n_t n_c}{n^4 (n-1)}\sum_{i=1}^{n}\sum_{j=1}^{n}Y_i^+Y_j^+  \\[5pt]

&=\frac{n_t n_c}{n^3 (n-1)}\sum_{i=1}^{n}(Y_i^+)^2
- \frac{n_t n_c}{n^4 (n-1)}\sum_{i=1}^{n}\sum_{j=1}^{n}Y_i^+Y_j^+  \\[5pt]
\end{align}
$$



[^fixed_values]: We need sample sized and potential outcomes to be fixed so that $\mathbb{E}[D_i n] = \mathbb{E}[D_i]\mathbb{E}[n]$, which is not true in general. It is true if $D_i$ and $n$ are independent, and one way to ensure they are independent is for $n$ and all other variables within the sum to be constants.

