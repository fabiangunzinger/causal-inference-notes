[[_Experimentation]]

In statistics, degrees of freedom generally refers to the number of values in a calculation that can vary freely.

Examples:

- Variance calculation: given that we have a mean, once we know all but one value, we also know final value, since sum of mean deviations has to be zero.

  

- Covariance calculation: given the two means, once we know the values for all but one x and y pair, we also know the values of the final pair. Hence, we loose one df (not clear to me why not two, given that both x and y are determined -- because we treat their product as a single value? but that seems arbitrary)

  

- Also, why no correction when we have popultion means? See wikipedia article on variance for section on bias correction

  

- There is lots of confusion out there when it comes to df. For instance, you sometimes hear people say that df is the number of parameters you had to calculate on route. But this is wrong. It happens to come to the same when calculating variance, but not if you calcualte covariance (where you calculate two means beforehand, but only loose one df).