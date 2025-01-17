[[_Experimentation]]

- A Bernoulli randomised experiment (BRE) is an experiment where, for each unit $i$, the probability of being assigned to treatment is decided by a mechanism that is equivalent to a coin toss.

- We write $R_i = 1$ if user $i$ is part of the experiment sample and $R_i = 0$ if they aren't.

- For each user on $N$ users in the super population, being part of the experiment sample is a [Bernoulli trial](https://en.wikipedia.org/wiki/Bernoulli_trial) with $R_i \sim \text{Bernoulli}(q)$. Hence, $\mathbb{E}[{R_i}] = q$ and $\mathbb{V}({R_i}) = q(1-q)$.

- Sometimes, people assume that $n$ is known, in which case $q = n/N$. This turns the setup into a CRE ([[Neyman's ATE estimator]]). Why do that?
	- It makes the math easier as it spares us from modelling $n$ as a Binomial random variable -- it seems that in the Bernoulli case, the variance isn't finite, while in the CRE case, it is (that's the case everyone works with).
	- Second, by the time we analyse the data, we do know $n$, so the assumption isn't completely arbitrary.
