[[_Experimentation]]

## Commonly used distributions

from [here](https://en.wikipedia.org/wiki/Variance)

### Commonly used probability distributions

  

The following table lists the variance for some commonly used probability distributions.

  

| Name of the probability distribution | Probability distribution function | Mean | Variance |

|--------------------------------------|-----------------------------------|------|----------|

| Binomial distribution | $\Pr\,(X=k) = \binom{n}{k}p^k(1 - p)^{n-k}$ | $np$ | $np(1 - p)$ |

| Geometric distribution | $\Pr\,(X=k) = (1 - p)^{k-1}p$ | $\frac{1}{p}$ | $\frac{1 - p}{p^2}$ |

| Normal distribution | $f(x \mid \mu, \sigma^2) = \frac{1}{\sqrt{2\pi\sigma^2}} e^{-\frac{(x - \mu)^2}{2\sigma^2}}$ | $\mu$ | $\sigma^2$ |

| Uniform distribution (continuous) | $f(x \mid a, b) = \begin{cases} \frac{1}{b - a} & \text{for } a \le x \le b, \\[3pt] 0 & \text{for } x < a \text{ or } x > b \end{cases}$ | $\frac{a + b}{2}$ | $\frac{(b - a)^2}{12}$ |

| Exponential distribution | $f(x \mid \lambda) = \lambda e^{-\lambda x}$ | $\frac{1}{\lambda}$ | $\frac{1}{\lambda^2}$ |

| Poisson distribution | $f(k \mid \lambda) = \frac{e^{-\lambda}\lambda^{k}}{k!}$ | $\lambda$ | $\lambda$ |