# Sampling and assignment {#sec-treatment-assignment}

In this section, we discuss how online experiments sample units into experiments
and assign them to treatment conditions. This matters because different
approaches have different implications for the independence among units, which,
in turn, has implications for the variability of our treatment estiamte (it's
standard error).

In an online experiment, we typically allocate units to the experiment sample
and a treatment condition using simple random assignment. We do this using a hash function as follows:

1. To determine whether a unit is part of the experiment sample, we create a hash
string by concatenating the unique unit id with additional experiment
information such as the experiment id, the market the experiment is being run
in, and a random seed.

2. We then feed that hash string into a hash algorithm (often MD5 is chosen) to
   receive a hash value and check where in the range of possible hash values our
particular hash value falls. If it's below a certain threshold, the unit is part
of the sample. If, for instance, we want to allocate 10% of traffic to the
experiment, we'd include all users whose hash value lies within the lowest (or
highest) 10% of possible hash values.

4. For units that are part of the sample, we then determine treatment allocation
  in the same way. We create a new hash string and hash value (by, for instance,
changing the random seed added to the string), and assign the
unit to a treatment condition based on where in the range of possible hash
values their hash value lies. If, for instance, we split the sample equally
between one treatment and one control group, units whose hash value falls into
the lower (or upper) half of possible hash values would be allocated to treatment.

Hashed sampling and treatment assignment resembles sampling without replacement
in that we can only include a given user in the experiment once, but it
resembles sampling with replacement in that sampling and treatment assignment are
independent across units.

The important implication of this hash sampling approach for experiment analysis
is that both sampling and treatment assignment for each unit are completely
independent of that of other units.

This is easiest to see in contrast to experiments where neither of these
decisions are independent, as is often the case in lab and field experiments in
social science, but also medical experiments. There, we typically recruit a
pre-determined number of units into our experiment, so that the inclusion of any
given unit lowers the probability of inclusion for all others. Similarly, for
treatment assignment, we would often use what is called "complete
randomisation", whereby we ensure that exactly $\Nt$ or of all $N$ units end up
in the treatment group. This, again means that assigning any given unit to
treatment lowers the probability of receiving the treatment for all other units.
In both of those cases, we sample without replacement.

In contrast, relying on hashes mimics the independence from sampling with
replacement. The entire point of hash values is that they are deterministic
given a hash string. Our decision to include a user into the sample or a
particular variant based on whether their unique hash value falls above or below
a pre-determined threshold is thus independent of how many other users have
already met that condition. This is because the decision we made for these users
alters neither our user's hash value nor the thresholds we compare it against.
