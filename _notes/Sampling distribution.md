[[_Experimentation]]

- A sampling distribution is the distribution of a statistic (e.g. the mean) over many repeated samples. Classical statistics is much concerned with making inferences from samples about the population based on such statistics.  

- When we measure an attribute of the population based on a sample using a statistic, the result will vary over repeated samples. To capture by how much it varies, we are concerned with the sampling variability.

- Key distinctions:

	- The data distribution is the distribution of the data in the sample, and its spread is measured by the variance or its square root, the standard deviation.

	- The sampling distribution is the distribution of the sample statistic, and its spread is measured by the sampling variance or its square root, the standard error.


### Example code

```python

rng = np.random.default_rng(2312)

def means(data, sample_size, num_means=1000):
	return rng.choice(data, (sample_size, num_means)).mean(0)

  
# Create dataset with population and sample data

data = pd.DataFrame({"Population": rng.normal(size=1_000_000)})

for n in [10, 100, 1000]:
	data = data.join(
		pd.Series(means(data.Population, n),
		name=f"Means of samples of {n}")
	)

data = data.melt()

g = sns.FacetGrid(data, col="variable")
g.map(sns.histplot, "value", bins=40, stat="percent")
g.set_axis_labels("Value", "Count")
g.set_titles("{col_name}");
```

Figure shows that:

- The spread of sampling distributions decreases with increasing sample size

- Data distribution has larger spread than sampling distributions (each data point is a special case of a sample with n = 1)