# Super population perspective




**Setup**

- We have a (super) population of $N_{sp}$ units.

- Each of these $N_{sp}$ units is being sampled into the experiment with probability $p$ and we write, for each unit $i$, $R_i = 1$ if the unit part of the experiment sample and $R_i = 0$ if they aren't.

- The total number of units in the sample is $N = \sum_{i = 1}^{N_{sp}}R_i$.

- Each of the $N$ units in our sample is allocated to the treatment condition with probability $q$, and we write, for each unit $i$, $W_i = 1$ if the unit is in the treatment group and $W_i = 0$ if they are in the control group.

- The total number of units in the treatment group is $N_t = \sum_{i = 1}^{N_{sp}} W_i$, and the total number of units in the control group is $N_c = \sum_{i = 1}^{N_{sp}} (1 - W_i)$.


**Potential outcomes**

- ...

$$
Y_i = W_iY_i(1) + (1 - W_i)Y_i(0)
$$ {#eq-yi}



**Estimand**

- ...


**Estimator**

- ... 

- We can write our treatment effect estimator, $\hat{\tau}$ in terms of the super-population as

$$
\hat{\tau} = \frac{1}{N_t}\sum_{i=1}^{N_{sp}} R_i W_i Y_i - \frac{1}{N_c}\sum_{i=1}^{N_{sp}} R_i (1 - W_i) Y_i
$$


**Unbiasedness of $\hat{\tau}$**

- Given our setup above, we have:

$$
\begin{align}
R_i \sim Bin(1, p) \quad &\text{with} \quad \E{R_i} = p \\
W_i \sim Bin(1, q) \quad &\text{with} \quad \E{W_i} = q
\end{align}
$$

- Also, we have:

$$
\begin{align}
N \sim Bin(N_{sp}, p) \quad &\text{with} \quad \E{N} = \E{\sum_{i = 1}^{N_{sp}}R_i} = N_{sp}\E{R_i} = N_{sp}p \\
N_t \sim Bin(N, q) \quad &\text{with} \quad \E{N_t} = \E{\sum_{i = 1}^{N}W_i} = N\E{W_i} = Nq \\
N_c \sim Bin(N, 1-q) \quad &\text{with} \quad \E{N_c} = \E{\sum_{i = 1}^{N}(1 - W_i)} = N(1 - \E{W_i}) = N(1 - q) \\
\end{align}
$$

- Finally, note that using @eq-yi we can write:

$$
\begin{align}
\frac{1}{N_t}\sum_{i=1}^{N_{sp}} R_i W_i Y_i &= \frac{1}{N_t}\sum_{i=1}^{N_{sp}} R_i W_i Y_i(1) \\
\frac{1}{N_c}\sum_{i=1}^{N_{sp}} R_i (1 - W_i) Y_i &= \frac{1}{N_t}\sum_{i=1}^{N_{sp}} R_i(1 - W_i) Y_i(0)
\end{align}
$$


::: {.callout-note collapse=true}

## Derivation

$$
\begin{align}
\frac{1}{N_t}\sum_{i=1}^{N_{sp}} R_i W_i Y_i
&= \frac{1}{N_t}\sum_{i=1}^{N_{sp}} R_i W_i \Bigl(W_i Y_i(1) + (1 - W_i) Y_i(0)\Bigr) \\
&= \frac{1}{N_t}\sum_{i=1}^{N_{sp}} \Bigl(R_i W_i W_i Y_i(1) + R_i W_i (1 - W_i) Y_i(0)\Bigr) \\ 
&= \frac{1}{N_t}\sum_{i=1}^{N_{sp}} R_i W_i W_i Y_i(1) \\ 
&= \frac{1}{N_t}\sum_{i=1}^{N_{sp}} R_i W_i Y_i(1) \\ 
\frac{1}{N_c}\sum_{i=1}^{N_{sp}} R_i (1 - W_i) Y_i
&= \frac{1}{N_t}\sum_{i=1}^{N_{sp}} R_i (1 - W_i) \Bigl(W_i Y_i(1) + (1 - W_i) Y_i(0)\Bigr) \\
&= \frac{1}{N_t}\sum_{i=1}^{N_{sp}} \Bigl(R_i(1 - W_i) W_i Y_i(1) + R_i(1 - W_i) (1 - W_i) Y_i(0)\Bigr) \\
&= \frac{1}{N_t}\sum_{i=1}^{N_{sp}} R_i(1 - W_i) (1 - W_i) Y_i(0) \\
&= \frac{1}{N_t}\sum_{i=1}^{N_{sp}} R_i(1 - W_i) Y_i(0)
\end{align}
$$

:::

- Using all of this, we can show that $\hat{\tau}$ in unbiased, that $\E{\hat{\tau}} = \tau$.

- We have two sources of randomness, one due to random sampling and one due to random allocation to treatment. Using the law of iterated expectations, we can write:

$$
\E{\hat{\tau}} = \Esp{\EW{\hat{\tau}|R}}.
$$

- That is, we can first take the expectation over the randomisation distribution while talking the vector of sampling allocation indicators, $R$, as given, and then take the expectation over the sampling distribution.

::: {.callout-note collapse=true}

## Law of iterated expectations

$$
\begin{align}
...
\end{align}
$$

:::

- In both of these steps, we implicitly also condition on the vectors of potential outcomes in the super population, $Y_{sp}(0), Y_{sp}(1)$, which we consider fixed and take as given. I don't condition on these explicitly to keep the notation light.

::: {.callout-note collapse=true}

## Explicitly conditioning on potential outcomes

- If we were to explicitly condition on potential outcomes, we'd get:

$$
\begin{align}
\E{\hat{\tau}}
&=\Esp{\EW{\hat{\tau}|R, Y_{sp}(0), Y_{sp}(1)} | Y_{sp}(0), Y_{sp}(1)}
\end{align}
$$

:::

- The first step gives us

$$
\begin{align}
\EW{\hat{\tau} | R}
&= \EW{\frac{1}{N_t}\sum_{i=1}^{N_{sp}} R_i W_i Y_i - \frac{1}{N_c}\sum_{i=1}^{N_{sp}} R_i (1 - W_i) Y_i} \\
&= \EW{\frac{1}{N_t}\sum_{i=1}^{N_{sp}} R_i W_i Y_i(1) - \frac{1}{N_c}\sum_{i=1}^{N_{sp}} R_i (1 - W_i) Y_i(0)} \\
&= \EW{\frac{1}{N_t}\sum_{i=1}^{N_{sp}} R_i W_i Y_i(1)} - \EW{\frac{1}{N_c}\sum_{i=1}^{N_{sp}} R_i (1 - W_i) Y_i(0)} \\
&= \frac{1}{\EW{N_t}}\sum_{i=1}^{N_{sp}} R_i \EW{W_i} Y_i(1) - \frac{1}{\EW{N_c}}\sum_{i=1}^{N_{sp}} R_i (1 - \EW{W_i}) Y_i(0) \\
&= \frac{1}{Nq}\sum_{i=1}^{N_{sp}} R_i (q) Y_i(1) - \frac{1}{N(1-q)}\sum_{i=1}^{N_{sp}} R_i (1-q) Y_i(0) \\
&= \frac{1}{N}\sum_{i=1}^{N_{sp}} R_i Y_i(1) - \frac{1}{N}\sum_{i=1}^{N_{sp}} R_i Y_i(0) \\
&= \frac{1}{N}\sum_{i=1}^{N_{sp}} R_i \Bigl(Y_i(1) - Y_i(0)\Bigr) \\
&= \tau_{fs}
\end{align}
$$

- The second step gives us:

$$
\begin{align}
\E{\hat{\tau}} 
&= \Esp{\EW{\hat{\tau}|R}} \\
&= \Esp{\tau_{fs}} \\
&= \Esp{\frac{1}{N}\sum_{i=1}^{N_{sp}} R_i \Bigl(Y_i(1) - Y_i(0)\Bigr)} \\
&= \frac{1}{\Esp{N}}\sum_{i=1}^{N_{sp}} \Esp{R_i} \Bigl(Y_i(1) - Y_i(0)\Bigr) \\
&= \frac{1}{N_{sp}p}\sum_{i=1}^{N_{sp}} (p) \Bigl(Y_i(1) - Y_i(0)\Bigr) \\
&= \frac{1}{N_{sp}}\sum_{i=1}^{N_{sp}}\Bigl(Y_i(1) - Y_i(0)\Bigr) \\
&= \tau_{sp}
\end{align}
$$



**Variance of \hat{\tau}**

