[[_Experimentation]]

- [ ] Have a look at Eppo docs (also check statsig) when writing this section:  [here](https://docs.geteppo.com/data-management/metrics/).

- Problem arises if unit of analysis is different from unit of randomisation. For instance, if we measure conversion rate (at the variant level) after randomising at a unit level as below. In this case, orders and sessions within units may not be independent.

$$
y_t = \frac{\sum_{n_t} orders}{\sum_{n_t} sessions}
$$

- However, if we first calculate unit-level conversion rates, then I believe this issue goes away, doesn't it? By using the unit-level metric, you ensure that each data point in your analysis corresponds directly to a randomized unit. This approach reduces the risk of inflating variance, unequal weights given to units, and ensures the independence assumptions underlying many statistical tests are more likely to hold.

$$
y_t = \frac{\sum_{n_t} \frac{orders_i}{sessions_i}}{n_t}
$$
