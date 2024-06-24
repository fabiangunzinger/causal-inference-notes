# Long-term treatment effects

- Definition of long-term effect: conceptually, the effect towards which the estimate asymptotes once product is fully launched and users have changed their behaviour. In practice, specified as a duration (e.g. 3 months) or amount of exposure (e.g. 10 times).

- Measuring an ATE during an experimental period masks possibly dynamics. Stylistically, it can come about in three ways:

  1. Constant treatment effect

  2. Average of increasing effect (effect takes time to fully materialise)

  3. Average of decreading effect (novelty effect)


## Why care?

- We want to make decisions for the long-run, not just for the experimentation window. Given the above, we might under or overestimate the actual effect of the treatment

- Provides an understanding of how users interact with product

- Might reveal bugs in experimental setup or implementation (i.e. if we see unusual spikes)


## Drivers of dynamic effects

- Primacy effects (take a while to materialise)

- Novelty effects (overshoot in the short-run)

- Network effects (users influenced by what their connections do, but change takes time to propagate through network)

- Delayed experience or measurement (might take time till user is exposed to change. e.g. FB new feature for Bday congratulation)

- Ecosystem changes

    - New products introduced (e.g. better cameras make photo-sharing more valuable)

    - Seasonality

    - Competitor behaviour (e.g. introduction of Signal may affect WhatsApp)

    - Government policy (e.g. GDPR introduction may reduce value of feature)


## Challenges 

Coverage:

  - Restaurants and customers and possibly riders are all long tailed: most engage frequently, some very frequently. This affects composition of experiment population. 

  - As a result, the shorter the experiment, the more we oversample from frequent users in session-based experiments (the same is not true in order-based ones, there it's constant).

  - Implication: for session-level exp: the longer the experiment, the more representative the sample, for order-level, equally representative for all durations.

  - Recommendations: be aware that short experiments may not generalise, check for sample representativeness, estimate heterogeneous treatment effects by user type.

  - Fundamentally: need think about what relevant population is.


## Approaches

### Run longer experiments

Limitations:

- Cost
- Time
- Cookie churn
- Users start using multiple devices and may be exposed to both treatment groups
- Family members start using account and distort effect


### Somewhat longer experiments

- Run experiment for, say, 4 weeks instead of 2, and use only latter 2 weeks for analysis @gupta2019top


### Modeling of long-term effect

- Number of approaches, see @larsen2023statistical

- hohnhold2015focusing: they predict long-term metric of interest (long-term revenue) based on short-term metrics (learned click-through rate, short-term revenue)


### Surrogacy

- See SM2 in Appendix of @larsen2023statistical for good basic primer and literature review

Motivation

- There are many contexts where we run experiments for a relatively short period of time (a couple weeks or even months, say), but really care about an effect that only materialises in the long-run (customer re-order rate or long-term revenue in OCEs, or quality-of-life-adjusted survival rate in a drug trial)


Basic setup:

- We have an experiment sample $N_E$ and an observational sample $N_O$. 

- In $N_E$ we observe, for each $i$, a tuple $(W_i, S_i, X_i)$, where $W_i$ is the treatment assignment, $S_i$ is the (vector-valued) short-term outcome and $X_i$ is a set of pre-treatment covariates.

- In $N_O$, we observe $(Y_i, S_i, X_i)$, where $Y_i$ is the long-term outcome of interest.

- We are interested in the effect of $W_i$ on $Y_i$.

- The key assumption is the surrogacy criterion, which specifies the relationship between $Y_i$ and $W_i$ given $S_i$.


@athey2024surrogate:

Critical assumptions:


1. Unconfounded treatment assignment

$$
Wi \ind Yi(0), Yi(1), Si(0), Si(1) \>|\> Xi, Pi = E,
$$


2. Surrogacy

- Surrogacy (Prentice) criterion:

(i)
$$
W_i \ind Y_i \>|\> S_i, X_i, P_i = 1
$$

(ii) ...

- Surrogacy index

$$
μ(s,x,p) ≡ E[Yi|Si = s,Xi = x,Pi = p]
$$


- Surrogacy score

$$
ρ(s,x) ≡ pr(Wi = 1|Si = s,Xi = x,Pi = E).
$$

- How this is being used? The simplest case is the following:

  1. Estimate the surrogacy index based on data from the observational sample, i.e. estimate

$$
Y_i = β_0 + β_S^T S_{it} + β_X^T X_i + ε_i
$$

2. Predict the surrogacy index for all units in the experimental sample

3. Estimate the treatment effect surrogate index as

$$
\tau^O = \frac{1}{N_{E, T}}\sum_{i=1}^{N^E}\hat{Y_i}W_i - \frac{1}{N_{E, C}}\sum_{i=1}^{N^E}\hat{Y_i} (1 - W_i)
$$



@hohnhold2015focusing

- hohnhold2015focusing quantify the trade-off between showing more adds, which increases revenue in the short-term, and those adds leading to add-blindness, which reduces click-through rate and, hence, revenue in the long-run. They first ran a long-term experiment where they did the following: AA test period to ensure comparability, AB test period with treatment seeing more adds, another AA test period with both groups seeing normal amount of adds to observe long-term effects. They found that click-through rate for treatment did go down in follow-up AA test, indicating learned behaviour that led to lower long-term revenue. With that data in hand, they then used a version of the surrogate approach, except that they only had one sample that contained $(W_i, Y_i, S_i, X_i)$, so they could directly predict $Y_i$ based on $S_i$, and then use that model to create primary metrics in future experiments. This is quite neat indeed! (Useful summary of approach in [this](https://towardsdatascience.com/what-we-can-learn-from-googles-long-term-ab-test-64e45b649cc4) article)

Notes from paper directly:

- User learning based on idea of Thorndike's Law: positive outcomes reinforce the behaviour that caused them, negative outcomes diminish the behaviour that caused them.

- In OCEs: mainly novely (decreasing engagement after initial spike) and primacy effects (slowly increasing engagement after initial reservation)




- Limitations of long-term experiments:

  - Survivorship bias (either due to non-random cookie churn or deliberate switching away from service due to poor user experience)

  - Side effects left-over from experiment in post period (e.g. users in treatment are prompted to add their home address, which they have still access to post experiment and which might improve their experience)


- @larsen2023statistical point out that hohnhold2015focusing effectively uses a surrogate approach as described above, with $S_i$ being learned click-through rate and short-term revenue, and $Y_i$ being long-term revenue. While not explicitly stated, the surrogacy assumption is implicit in their approach.



Related articles to look into:
- @imbens2024longterm
- @vangoffrier2023estimating

Application to OCEs:

- @athey2024surrogate suggest building a library of possible $S_i$s and then find smallest set of surrogates that successfully matches the long-term outcome of interest.




### Combining experimental and observational data

@athey2020combining

- Relies on having $W_i$ in observational data. We don't generally have that in OCEs, because treatment is either rolled out to everyone or no one.








### Simple panel approach

- A simple approach to estimate whether there are dynamic effects is to use panel data with a time dummy and test whether the time coefficients are decreasing or increasing

- This only works if everyone enters at the same time, which is not the case in practice. Hence, need to account for the below


### Dynamic treatment effects (relatively short-term)

- Reweighing (Blundell, Deliveroo [approach]([this](https://drive.google.com/file/d/1h9WZFmf5moHc4XV_MwvT94_RG3CAhOTv/view)))

  - Re-weight sample so as to keep relative proportion of types constant across time and treatment cell

  - Estimating dynamic average treatment effects if everyone enters at the same time is straightforward: treat each week as mini experiment and plot ATE over time.

  - Estimating dynamic average treatment effects if people enter at different times more complex, as in each week we observe people at different time of treatment path.

      - Changing time measure to weeks since entry to experiment

      - Because we have a fixed endpoint, this means we observe fewer users at later points since entering experiment (since some, who join late, we only observe for a few weeks till the experiment ends).

      - Also, because of coverage issue above, we proportionally observe more frequent users in later points since experiment entry (since their share is about constant as they engage weekly, while infrequent users engage more infrequently)

      - Hence, if we just compare outcomes across Treatment and Control for each week since experiment entry, composition of samples over time is different (again, frequent users have more weight in later periods)
      
      - Affects metrics at any level: user, order, session
      
      - Problem exists whenever:

        1. Users enter at different times

        2. We cut off time since experiments for later joiners (i.e. observe users for different lengths of time)

        3. Treatment entry is correlated with treatment effect (e.g. effect on top users is different)








