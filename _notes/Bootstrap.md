[[_Experimentation]]

- In practice, we often use the bootstrap to calculate standard errors of model parameters or statistics.

- Conceptually, the bootstrap works as follows:

  

1) we draw an original sample and calculate our statistic

2) we then create a blown-up version of that sample by duplicating it many times

3) we then draw repeated samples from the large sample, recalculate our statistic, and calculate the standard deviation of these statistics to get the standard error.

  

- To achieve this easily, we can skip step 2) by simply sampling with replacement from the original distribution in step 3).

  

- The full procedure makes clear what the bootstrap results tell us, however: they tell us how lots of additional samples would behave if they were drawn from a population like our original sample.

  

- Hence, if the original sample is not representative of the population of interest, then bootstrap results are not informative about that population either.

  

- The bootstrap can also be used to improve the performance of classification or regression trees by fitting multiple trees on bootstrapped sample and then averaging their predictions. This is called "bagging", short for "bootstrap aggregating".

  

- We can use to boostrap also to calculate CIs following this algorithm:

1) Draw a large number of bootstrap samples and calculate the statistic of interest

2) Trim [(100-x)/2] percent of the bootstrap results on either end of the distribution

3) The trim points are the end point of the CI.

  
  

<!--

```{python}

from sklearn.utils import resample

  

rng = np.random.default_rng(2312)

  

population = rng.normal(3, 5, 1_000_000)

sample = rng.choice(population, 1000)

resample_means = pd.Series(resample(sample).mean() for _ in range(1000))

  

print(f"{'Population mean:':20} {np.mean(population):.3f}")

print(f"{'Sample mean:':20} {np.mean(sample):.3f}")

print(f"{'Bootstrap mean:':20} {np.mean(resample_means.mean()):.3f}")

print(f"{'Bootstrap se:':20} {np.mean(resample_means.std()):.3f}")

``` -->