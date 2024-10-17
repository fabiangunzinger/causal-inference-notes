# The stats of online experiments


## Setup

- Online experiments typically go through a ramp-up phase: they include only a small fraction of users at the start and all users at the end.

- Statistically, this means we have to consider two different cases. In the first case, during the early stages of an experiment, we use a sample of the entire user population to learn something about that population as a whole; in this case, the sample we work with and the sample we want to learn something about are different. In the second case, when the entire user population is part of the experiment, the sample we work with and the sample we want to learn something about are the same. Following @imbens2015causal, I refer to the first approach as the super-population perspective and the second case the finite sample perspective. 

- We have a (super) population of $N$ users. In the example I'm going to use throughout, these are all of our iOS-app users in the UK.

- From this super population, we sample $n$ users to be part of the experiment, and then allocate $n_t$ users to treatment and $n_c$ users to control.

- The way we sample users into the experiment and allocate them to treatment has implications for our statistical analysis, so let's have a look at the details.

- Online experiments usually use the following **sampling** approach to determine whether a user is part of an experiment:

  1. Create a hash string unique to each user such as `<user_id><experiment_id><market>`.

  2. Feed the hash string into a hash algorithm (often MD5) and receive a hash value.

  3. Use the hash value to determine whether a user is part of the experiment. Say we allocate 10% of traffic to the experiment. We then include the user only if their hash value falls within the bottom (or top) 10% of possible hash values.

- With this approach, the probability that a user is sampled into the experiment is independent of the sampling decisions of all other users. Each of our $N$ users is part of the experiment experiment with probability $n/N$ and we write $R_i = 1$ if user $i$ is part of the experiment sample and $R_i = 0$ if they aren't.[^conditioning_on_n]


[^conditioning_on_n]: For each user in the super population, being part of the experiment sample is a [Bernoulli trial](https://en.wikipedia.org/wiki/Bernoulli_trial) with $R_i \sim \text{Bernoulli}(n/N)$ and, hence, $\E{R_i} = n/N$ and $\V{R_i} = n/N(1-n/N)$. I assume here that we know $n$. The reason for doing so is twofold. First, it makes the math easier as it spares us from modeling $n$ as a Binomial random variable. Second, by the time we analyse the data, we do know $n$.


[^dependent_sampling]: This is easiest to see in contrast to experiments where neither of these
decisions are independent, as is often the case in lab and field experiments in
social science, but also medical experiments. There, we typically recruit a
pre-determined number of units into our experiment, so that the inclusion of any
given unit lowers the probability of inclusion for all others. Similarly, for
treatment assignment, we would often use a completely randomised assignment, whereby we ensure that exactly $N_t$ units end up in the treatment group. This, again means that assigning any given unit to treatment lowers the probability of receiving the treatment for all other units.





- The total number of users in the sample is $n = \sum_{i = 1}^{N}R_i$.

- Each of the $n$ users in our sample is allocated to the treatment condition with probability $q$, and we write $W_i = 1$ if user $i$ is in the treatment group and $W_i = 0$ if they are in the control group.

- The total number of users in the treatment group is $n_t = \sum_{i = 1}^{N} W_i$, and the total number of users in the control group is $n_c = \sum_{i = 1}^{N} (1 - W_i)$.

- Given this setup, we have:
$$
\begin{align}
\E{R_i} &= p \\
\E{W_i} &= q \\
\E{n} &= Np \\
\E{n_t} &= nq \\
\E{n_c} &= n(1 - q) \\
\end{align}
$$

  (we will use this in the unbiasedness proof below)

::: {.callout-note collapse=true}
## Details

- For each user in the super population, being part of the experiment sample is a [Bernoulli trial](https://en.wikipedia.org/wiki/Bernoulli_trial), as is being part of the treatment group for each user in the experiment sample.

$$
\begin{align}
R_i \sim \text{Bernoulli}(p) \quad &\text{with} \quad \E{R_i} = p \\
W_i \sim \text{Bernoulli}(q) \quad &\text{with} \quad \E{W_i} = q
\end{align}
$$

:::

**Potential outcomes**

- ...

$$
Y_i = W_iY_i(1) + (1 - W_i)Y_i(0)
$$ {#eq-yi}

- Individual causal effects ... 


**Estimand**

- We are generally interested in the effect of a universal policy -- a comparison between a state of the world where everyone is exposed to the treatment and one where nobody is. Also, while we can capture the difference between these two states of the world in many different ways, we typically focus on the difference in average outcomes.

- Hence, the estimand of interest (the theoretical quantity we try to estimate) is:

$$
\tau = \bar{Y}(1) - \bar{Y}(0),
$$

  where ...



**Identification**

- See Wagner notes for 4 assumptions: https://web.stanford.edu/~swager/stats361.pdf 

- ... Randomisation solves selection bias problem and allows us to identify treatment effect

- Use content from outcomes (expectations and show how randomisation eliminates selection bias)

- Randomisation

- SUTVA
  - No interference
  - Consistency
  - See deng2023first for reference to Rubin 1980 original article on precise assumption and other great Rubin references

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

- A natural estimator is ...

- We can write our treatment effect estimator, $\hat{\tau}$ in terms of the super-population as

$$
\hat{\tau} = \frac{1}{n_t}\sum_{i=1}^{N} R_i W_i Y_i - \frac{1}{n_c}\sum_{i=1}^{N} R_i (1 - W_i) Y_i
$$


**Unbiasedness of $\hat{\tau}$**

- First, note that using @eq-yi we can write:

$$
\begin{align}
\frac{1}{n_t}\sum_{i=1}^{N} R_i W_i Y_i &= \frac{1}{n_t}\sum_{i=1}^{N} R_i W_i Y_i(1) \\
\frac{1}{n_c}\sum_{i=1}^{N} R_i (1 - W_i) Y_i &= \frac{1}{n_t}\sum_{i=1}^{N} R_i(1 - W_i) Y_i(0)
\end{align}
$$


::: {.callout-note collapse=true}

## Derivation

$$
\begin{align}
\frac{1}{n_t}\sum_{i=1}^{N} R_i W_i Y_i
&= \frac{1}{n_t}\sum_{i=1}^{N} R_i W_i \Bigl(W_i Y_i(1) + (1 - W_i) Y_i(0)\Bigr) \\
&= \frac{1}{n_t}\sum_{i=1}^{N} \Bigl(R_i W_i W_i Y_i(1) + R_i W_i (1 - W_i) Y_i(0)\Bigr) \\ 
&= \frac{1}{n_t}\sum_{i=1}^{N} R_i W_i W_i Y_i(1) \\ 
&= \frac{1}{n_t}\sum_{i=1}^{N} R_i W_i Y_i(1) \\ 
\frac{1}{n_c}\sum_{i=1}^{N} R_i (1 - W_i) Y_i
&= \frac{1}{n_t}\sum_{i=1}^{N} R_i (1 - W_i) \Bigl(W_i Y_i(1) + (1 - W_i) Y_i(0)\Bigr) \\
&= \frac{1}{n_t}\sum_{i=1}^{N} \Bigl(R_i(1 - W_i) W_i Y_i(1) + R_i(1 - W_i) (1 - W_i) Y_i(0)\Bigr) \\
&= \frac{1}{n_t}\sum_{i=1}^{N} R_i(1 - W_i) (1 - W_i) Y_i(0) \\
&= \frac{1}{n_t}\sum_{i=1}^{N} R_i(1 - W_i) Y_i(0)
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

- In both of these steps, we implicitly also condition on the vectors of potential outcomes in the super population, $Y_{sp}(0), Y_{sp}(1)$, which we consider fixed and take as given. I don't condition on these explicitly to keep the notation light.[^condition_on_pot_outcomes]

- TODO: condition on $Y$, as a shorthand. Adapt notation below. Also, consider using bf for vectors and matrices for clarity. Probably do it!

- The inner expectation is equal to:

$$
\begin{align}
\EW{\hat{\tau} | R}
&= \EW{\frac{1}{n_t}\sum_{i=1}^{N} R_i W_i Y_i - \frac{1}{n_c}\sum_{i=1}^{N} R_i (1 - W_i) Y_i \>\Bigg|\> R} \vs
&= \EW{\frac{1}{n_t}\sum_{i=1}^{N} R_i W_i Y_i(1) - \frac{1}{n_c}\sum_{i=1}^{N} R_i (1 - W_i) Y_i(0) \>\Bigg|\> R} \vs
&= \EW{\sum_{i=1}^{N} R_i \Biggl(\frac{W_i Y_i(1)}{n_t} - \frac{(1 - W_i) Y_i(0)}{n_c}\Biggr)\>\Bigg|\> R} \vs
&= \sum_{i=1}^{N} R_i \EW{\frac{W_i Y_i(1)}{n_t} - \frac{(1 - W_i) Y_i(0)}{n_c}} \vs
&= \sum_{i=1}^{N} R_i \Biggl(\frac{\EW{W_i} Y_i(1)}{\EW{n_t}} - \frac{(1 - \EW{W_i}) Y_i(0)}{\EW{n_c}}\Biggr) \vs
&= \sum_{i=1}^{N} R_i \Biggl(\frac{q Y_i(1)}{Nq} - \frac{(1 - q) Y_i(0)}{N(1-q)}\Biggr) \vs
&= \sum_{i=1}^{N} R_i \Biggl(\frac{Y_i(1)}{N} - \frac{Y_i(0)}{N}\Biggr) \vs
&= \frac{1}{N}\sum_{i=1}^{N} R_i \bigl(Y_i(1) - Y_i(0)\bigr) \vs
&= \tau_{fs}
\end{align}
$$

- The outer expectation is equal to:

$$
\begin{align}
\E{\hat{\tau}} 
&= \Esp{\EW{\hat{\tau}|R}} \\
&= \Esp{\tau_{fs}} \\
&= \Esp{\frac{1}{N}\sum_{i=1}^{N} R_i \bigl(Y_i(1) - Y_i(0)\bigr)} \\
&= \frac{1}{\Esp{N}}\sum_{i=1}^{N} \Esp{R_i} \bigl(Y_i(1) - Y_i(0)\bigr) \\
&= \frac{1}{Np}\sum_{i=1}^{N} p \bigl(Y_i(1) - Y_i(0)\bigr) \\
&= \frac{1}{N}\sum_{i=1}^{N}\bigl(Y_i(1) - Y_i(0)\bigr) \\
&= \tau
\end{align}
$$


**Variance of $\hat{\tau}$**

- Using the law of total variance[^law_of_total_variance], we can write $\V{\hat{\tau}}$ as

$$
\begin{align}
\V{\hat{\tau}}
&= \Esp{\VW{\hat{\tau} | R}} + \Vsp{\EW{\hat{\tau} | R}}
\end{align}
$$




[^condition_on_pot_outcomes]: If we were to explicitly condition on potential outcomes, we'd get:
  $$
  \begin{align}
  \E{\hat{\tau}}
  &=\Esp{\EW{\hat{\tau}|R, Y_{sp}(0), Y_{sp}(1)} | Y_{sp}(0), Y_{sp}(1)}
  \end{align}
  $$


[^law_of_total_variance]: In general, the [Law of total variance](https://en.wikipedia.org/wiki/Law_of_total_variance) states that:
  $$
  \begin{align}
  \V{Y} = \E{\V{Y|X}} + \V{\E{Y|X}}
  \end{align}
  $$
  In our case here, conditioning on $R$ means that we take the expectation or variance over the randomisation distribution, which I make explicit with the subscript $W$. The unconditional expectation or variance is taken over the randomisation distribution, which I make explicit using the subscript $sp$. As in the unbiasedness proof above, we are also implicitly conditioning on potential outcomes and I omit making this explicit to keep the notation lighter. Making the conditioning explicit would mean we apply the law to a conditional variance, for which the logic would still hold, and we'd write:
  $$
  \begin{align}
  \V{\hat{\tau} | Y_{sp}(0), Y_{sp}(1)}
  &= \Esp{\VW{\hat{\tau} | R, Y_{sp}(0), Y_{sp}(1)} | Y_{sp}(0), Y_{sp}(1)} \\
  &+ \Vsp{\EW{\hat{\tau} | R, Y_{sp}(0), Y_{sp}(1)} | Y_{sp}(0), Y_{sp}(1)}
  \end{align}
  $$
