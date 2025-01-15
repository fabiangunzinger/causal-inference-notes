[[_Experimentation]]

- The standard error is a measure for the variability of the sampling distribution.

- It is related to the standard deviation of the observations, $\sigma$ and the sample size $n$ in the following way:
$$

se = \frac{\sigma}{\sqrt{n}}

$$
- The relationship between sample size and se is sometimes called the "Square-root of n rule", since reducing the $se$ by a factor of 2 requires an increase in the sample size by a factor of 4.

Derivation:

The sum of a sequence of independent random variables is:
$$

T = (x_1 + x_2 + ... + x_n)

$$
Which has variance
$$

Var(T) = Var(x_1) + Var(x_2) + ... + Var(x_n) = n\sigma^2$$
and mean
$$

\bar{x} = T/n.

$$
The variance of $\bar{x}$ is then given by:
$$
Var(\bar{x}) = Var\left(\frac{T}{n}\right) = \frac{1}{n^2}Var(T) = \frac{1}{n^2}n\sigma^2 = \frac{\sigma^2}{n}.
$$
The standard error is defined as the standard deviation of $\bar{x}$, and is thus
$$
se(\bar{x}) = \sqrt{Var(\bar{x})} = \frac{\sigma}{\sqrt{n}}.
$$

### Standard deviation vs standard error

- Standard deviation is the spread of the distribution of the values in the population of interest

- Standard error is the spread of the distribution of a sample statistic (such as the mean) based on a random sample of population values.