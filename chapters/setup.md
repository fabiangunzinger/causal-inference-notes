# Setup {#setup}



- Whether sampling and treatment assignment are independent across units impacts the standard error ouf our treatment effect estimator.



- **Treatment assignment** for units in the experiment sample then works in the same way:

  1. We again create a unique -- but different[^different_hash] -- hash string for each unit.

  2. We use the hash algorithm to generate a hash value

  3. If we wanted to allocate units equally to a control and treatment group, we could allocate all units with hash values within the bottom 50% of possible values to the treatment group and all others to the control group.

- Hashed sampling and treatment assignment resembles sampling without replacement in that we can only include a given user in the experiment once, and resembles sampling with replacement in that **sampling and treatment assignment are independent** across units -- sampling any one unit does not alter the chance of being sampled for any other unit.[^dependent_sampling]


[^different_hash]: Suppose we used the same hash strings instead, and that we sampled units with hash values that fall into the bottom 10% of possible hash values. What would happen if we now allocated all units with hash values in the bottom 50% of possible values to treatment and all others to control? How many units would be in the control group? (None! Since the hash values of all units in the sample would fall into the bottom 10% of possible hash values so that all units would be allocated to treatment.) A simple way to create a different hash value is to flip the first bit of the hash string. Because of the [avalanche effect](https://en.wikipedia.org/wiki/Avalanche_effect), this would result in a completely different hash value.

