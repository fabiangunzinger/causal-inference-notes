[[_Experimentation]], [[Experiment statistics]]

Online experiments usually use the following **sampling** approach to determine whether a user is part of an experiment:

1. Create a hash string unique to each user. For example: `<user_id><experiment_id>`.

2. Feed the hash string into a hash algorithm (often MD5) and receive a hash value.

3. Use the hash value to determine whether a user is part of the experiment. Say we allocate 10% of traffic to the experiment. We then include the user only if their hash value falls within the bottom (or top) 10% of possible hash values.

With this approach, the probability that a user is sampled into the experiment is independent of the sampling decisions of all other users. 

We write $R_i = 1$ if user $i$ is part of the experiment sample and $R_i = 0$ if they aren't.

If we sample $n$ users into the experiment, then each of our $N$ users is part of the experiment experiment with probability $n/N$. [^conditioning_on_n]
  

[^conditioning_on_n]: For each user in the super population, being part of the experiment sample is a [Bernoulli trial](https://en.wikipedia.org/wiki/Bernoulli_trial) with $R_i \sim \text{Bernoulli}(n/N)$ and, hence, $\E{R_i} = n/N$ and $\V{R_i} = n/N(1-n/N)$. I assume here that we know $n$. The reason for doing so is twofold. First, it makes the math easier as it spares us from modeling $n$ as a Binomial random variable. Second, by the time we analyse the data, we do know $n$.