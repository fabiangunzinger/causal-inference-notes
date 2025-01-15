todo
- Combine as needed

## Setup notes 1

- When deciding on the experiment setup we make two types of decisions.

- First, we decide whether the $n$ units in our experiment sample are the population of interest, or whether that population of interest is instead a larger super-population of size $N$ of which the $n$ units in the experiment sample are a random sample. Following @imbens2015causal, I refer to the former as the finite sample perspective and the later as the super population perspective. See more in [[Finite sample vs super-population perspectives]]

- Second, regardless of which of these two perspectives we adopt, we decide how to allocate the $n$ units in the experiment sample into a treatment and control group. The procedure for performing this allocation is called the [[Assignment mechanism]], and there are a number of different such mechanisms.

- Technically, this type of experiment is called a [[Bernoulli randomised experiment]].

- If we are treating $n$ as known, then the setting becomes equivalent to a [[Imbens and Rubin book notes to be split into separate notes]] (see discussion in [[Bernoulli randomised experiment]] for more detail)


## Setup notes 2 (online experiments)

[[_Experimentation]]

- Online experiments typically go through a ramp-up phase: they include only a small fraction of users at the start and all users at the end.  

- Statistically, this means we have to consider two different cases. In the first case, during the early stages of an experiment, we use a sample of the entire user population to learn something about that population as a whole; in this case, the sample we work with and the sample we want to learn something about are different. In the second case, when the entire user population is part of the experiment, the sample we work with and the sample we want to learn something about are the same. Following @imbens2015causal, I refer to the first approach as the super-population perspective and the second case the finite sample perspective.

- We have a (super) population of $N$ users. In the example I'm going to use throughout, these are all of our iOS-app users in the UK.

- From this super population, we sample $n$ users to be part of the experiment, and then allocate $n_t$ users to treatment and $n_c$ users to control.

- The way we sample users into the experiment and allocate them to treatment has implications for our statistical analysis, so let's have a look at the details.

- Online experiments usually use the following **sampling** approach to determine whether a user is part of an experiment:

	1. Create a hash string unique to each user such as `<user_id><experiment_id><market>`.  
	2. Feed the hash string into a hash algorithm (often MD5) and receive a hash value.
	3. Use the hash value to determine whether a user is part of the experiment. Say we allocate 10% of traffic to the experiment. We then include the user only if their hash value falls within the bottom (or top) 10% of possible hash values.

- With this approach, the probability that a user is sampled into the experiment is independent of the sampling decisions of all other users.


**Treatment assignment** for units in the experiment sample then works in the same way:

1. We again create a unique -- but different[^different_hash] -- hash string for each unit.

2. We use the hash algorithm to generate a hash value

3. If we wanted to allocate units equally to a control and treatment group, we could allocate all units with hash values within the bottom 50% of possible values to the treatment group and all others to the control group.

- Hashed sampling and treatment assignment resembles sampling without replacement in that we can only include a given user in the experiment once, and resembles sampling with replacement in that **sampling and treatment assignment are independent** across units -- sampling any one unit does not alter the chance of being sampled for any other unit.[^dependent_sampling]

[^different_hash]: Suppose we used the same hash strings instead, and that we sampled units with hash values that fall into the bottom 10% of possible hash values. What would happen if we now allocated all units with hash values in the bottom 50% of possible values to treatment and all others to control? How many units would be in the control group? (None! Since the hash values of all units in the sample would fall into the bottom 10% of possible hash values so that all units would be allocated to treatment.) A simple way to create a different hash value is to flip the first bit of the hash string. Because of the [avalanche effect](https://en.wikipedia.org/wiki/Avalanche_effect), this would result in a completely different hash value.


## Setup notes 3







  
