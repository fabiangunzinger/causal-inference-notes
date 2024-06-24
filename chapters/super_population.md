# Super population perspective

**Setup**

- We have a (super) population of $N_{sp}$ units.

- Each of these $N_{sp}$ units is being sampled into the experiment with probability $p$ and we write $R_i = 1$ if unit $i$ is part of the experiment sample and $R_i = 0$ otherwise.

- The total number of units in the sample is $N = \sum_{i = 1}^{N_{sp}}R_i$.

- Each of the $N$ units in our sample is allocated to the treatment condition with probability $q$, and we write $W_i = 1$ if unit $i$ is in the treatment group and $W_i = 0$ if they are in the control group.

- The total number of units in the treatment group is $N_t = \sum_{i = 1}^{N_{sp}} W_i$, and the total number of units in the control group is $N_c = \sum_{i = 1}^{N_{sp}} (1 - W_i)$.

- Given this setup, we have:
$$
\begin{align}
\E{R_i} &= p \\
\E{W_i} &= q \\
\E{N} &= N_{sp}p \\
\E{N_t} &= Nq \\
\E{N_c} &= N(1 - q) \\
\end{align}
$$

  (we will use this in the unbiasedness proof below)

::: {.callout-note collapse=true}
## Details

- For each unit in the super population, being part of the experiment sample is a [Bernoulli trial](https://en.wikipedia.org/wiki/Bernoulli_trial), as is being part of the treatment group for each unit in the experiment sample.

$$
\begin{align}
R_i \sim \text{Bernoulli}(p) \quad &\text{with} \quad \E{R_i} = p \\
W_i \sim \text{Bernoulli}(q) \quad &\text{with} \quad \E{W_i} = q
\end{align}
$$

- Each of the sample sizes is defined as the sum of independent Bernoulli trials and thus follows a [Binomial distribution](https://en.wikipedia.org/wiki/Binomial_distribution).

$$
\begin{align}
N \sim Bin(N_{sp}, p) \quad &\text{with} \quad \E{N} = \E{\sum_{i = 1}^{N_{sp}}R_i} = N_{sp}\E{R_i} = N_{sp}p \\
N_t \sim Bin(N, q) \quad &\text{with} \quad \E{N_t} = \E{\sum_{i = 1}^{N}W_i} = N\E{W_i} = Nq \\
N_c \sim Bin(N, 1-q) \quad &\text{with} \quad \E{N_c} = \E{\sum_{i = 1}^{N}(1 - W_i)} = N(1 - \E{W_i}) = N(1 - q) \\
\end{align}
$$
:::

**Potential outcomes**

- ...

$$
Y_i = W_iY_i(1) + (1 - W_i)Y_i(0)
$$ {#eq-yi}


**Estimand**

- ... Randomisation solves selection bias problem and allows us to identify treatment effect



**Identification**

- Randomisation
- SUTVA
- Solely and itself (excludability and non-interference)
- Ignorability

Check:
- duflo2006randomization
- Mostly harmless metrics
- Field experiments book
- Kohavi papers/book
- Imbens and Rubins

Question:
- You randomise at customer level. For analysis, you do the following: you calculate metrics at a restaurant level, then calculate variant level averages from the restaurant-level averages. Is there a problem? What is it? What assumptions are being violated? 



**Estimator**

- ... 

- We can write our treatment effect estimator, $\hat{\tau}$ in terms of the super-population as

$$
\hat{\tau} = \frac{1}{N_t}\sum_{i=1}^{N_{sp}} R_i W_i Y_i - \frac{1}{N_c}\sum_{i=1}^{N_{sp}} R_i (1 - W_i) Y_i
$$


**Unbiasedness of $\hat{\tau}$**

- First, note that using @eq-yi we can write:

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

- We can now show that $\hat{\tau}$ in unbiased, that $\E{\hat{\tau}} = \tau$.

- We have two sources of randomness, one due to random sampling and one due to random allocation to treatment. Using the law of iterated expectations, we can write:

$$
\E{\hat{\tau}} = \Esp{\EW{\hat{\tau}|R}}.
$$

::: {.callout-note collapse=true}
## Law of iterated expectations

- That is, we can first take the expectation over the randomisation distribution while talking the vector of sampling allocation indicators, $R$, as given, and then take the expectation over the sampling distribution.

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
&= \EW{\frac{1}{N_t}\sum_{i=1}^{N_{sp}} R_i W_i Y_i - \frac{1}{N_c}\sum_{i=1}^{N_{sp}} R_i (1 - W_i) Y_i \>\Bigg|\> R} \vs
&= \EW{\frac{1}{N_t}\sum_{i=1}^{N_{sp}} R_i W_i Y_i(1) - \frac{1}{N_c}\sum_{i=1}^{N_{sp}} R_i (1 - W_i) Y_i(0) \>\Bigg|\> R} \vs
&= \EW{\sum_{i=1}^{N_{sp}} R_i \Biggl(\frac{W_i Y_i(1)}{N_t} - \frac{(1 - W_i) Y_i(0)}{N_c}\Biggr)\>\Bigg|\> R} \vs
&= \sum_{i=1}^{N_{sp}} R_i \EW{\frac{W_i Y_i(1)}{N_t} - \frac{(1 - W_i) Y_i(0)}{N_c}} \vs
&= \sum_{i=1}^{N_{sp}} R_i \Biggl(\frac{\EW{W_i} Y_i(1)}{\EW{N_t}} - \frac{(1 - \EW{W_i}) Y_i(0)}{\EW{N_c}}\Biggr) \vs
&= \sum_{i=1}^{N_{sp}} R_i \Biggl(\frac{q Y_i(1)}{Nq} - \frac{(1 - q) Y_i(0)}{N(1-q)}\Biggr) \vs
&= \sum_{i=1}^{N_{sp}} R_i \Biggl(\frac{Y_i(1)}{N} - \frac{Y_i(0)}{N}\Biggr) \vs
&= \frac{1}{N}\sum_{i=1}^{N_{sp}} R_i \bigl(Y_i(1) - Y_i(0)\bigr) \vs
&= \tau_{fs}
\end{align}
$$

- The second step gives us:

$$
\begin{align}
\E{\hat{\tau}} 
&= \Esp{\EW{\hat{\tau}|R}} \\
&= \Esp{\tau_{fs}} \\
&= \Esp{\frac{1}{N}\sum_{i=1}^{N_{sp}} R_i \bigl(Y_i(1) - Y_i(0)\bigr)} \\
&= \frac{1}{\Esp{N}}\sum_{i=1}^{N_{sp}} \Esp{R_i} \bigl(Y_i(1) - Y_i(0)\bigr) \\
&= \frac{1}{N_{sp}p}\sum_{i=1}^{N_{sp}} p \bigl(Y_i(1) - Y_i(0)\bigr) \\
&= \frac{1}{N_{sp}}\sum_{i=1}^{N_{sp}}\bigl(Y_i(1) - Y_i(0)\bigr) \\
&= \tau_{sp}
\end{align}
$$


**Variance of $\hat{\tau}$**

- Using the law of total variance, we can write $\V{\hat{\tau}}$ as

$$
\begin{align}
\V{\hat{\tau}}
&= \Esp{\VW{\hat{\tau} | R}} + \Vsp{\EW{\hat{\tau} | R}}
\end{align}
$$

::: {.callout-note collapse=true}

## Law of total variance

- In general, the [Law of total variance](https://en.wikipedia.org/wiki/Law_of_total_variance) states that:

$$
\begin{align}
\V{Y} = \E{\V{Y|X}} + \V{\E{Y|X}}
\end{align}
$$

- In our case here, conditioning on $R$ means that we take the expectation or variance over the randomisation distribution, which I make explicit with the subscript $W$. The unconditional expectation or variance is taken over the randomisation distribution, which I make explicit using the subscript $sp$.

- As in the unbiasedness proof above, we are also implicitly conditioning on potential outcomes and I omit making this explicit to keep the notation lighter. Making the conditioning explicit would mean we apply the law to a conditional variance, for which the logic would still hold, and we'd write:

$$
\begin{align}
\V{\hat{\tau} | Y_{sp}(0), Y_{sp}(1)}
&= \Esp{\VW{\hat{\tau} | R, Y_{sp}(0), Y_{sp}(1)} | Y_{sp}(0), Y_{sp}(1)} \\
&+ \Vsp{\EW{\hat{\tau} | R, Y_{sp}(0), Y_{sp}(1)} | Y_{sp}(0), Y_{sp}(1)}
\end{align}
$$
:::



