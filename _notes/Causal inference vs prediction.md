[[_Experimentation]]

- Descriptive analysis describes the data. We simply turn data into meaningfull summary measures presented in tables or -- better, usually! -- figures. The aim here is to simply describe the data as it is, highlighting aspects that are particularly interesting or relevant to the task at hand.

- Predictive analysis predicts unobserved metric values based on observed ones. We build a model that captures the data generating process of the metric we aim to predict based on training data we observe, so that we can then predict metric values we don't observe.

- Causal inference makes statements about what would happen to outcomes if we changed the world in a particular way.

Causal inference vs prediction

- Prediction is about finding the most likely outcome based on a set of (existing) covariates. Causal inference is about finding the effect of a change in a covariate on the outcome.

- The difference is profound: when predicting, you take the features as given and predict outcomes based on them -- you're asking: "given existing features, what outcome can I expect?". When you perform causal inference, you want to know what would happen if you were to change one of the covariates -- you're asking "if I were to change one covariate in a certain way, what outcome could I expect?". (In prediction, different units have different covariate values. In causal inference, we ask what would happen if we changed covariate values for some or all units.)

- Causal inference is about manipulating covariates -- to paraphrase Donald Rubin: there is no causality without manipulation.

- Technically, what this really comes down to is that in prediction, you don't care about selection bias, whereas in causal inference that's the main thing you care about.

- This also means that the role of goodness of fit is very different: for prediction, it's obviously very important -- if your model explains only a very small part of the variation in the outcome, it won't be very good at predicting outcomes. In causal inference, goodness of fit doesn't matter because your aim is not to predict, but to know how the outcome changes if you change a covariate. So, you can have very low goodness of fit (lots of things outside the model predicting outcomes), but if you can precisely estimate your treatment effect, that's very valuable (you learn that regardless of all the many other factors that determine the outcome, changing a covariate in a certain way tends to change outcomes in a certain way.)


- In a business context, they capture two sets of problems:
	- Prediction is about making statements in domains where the future is expected to be similar to the past (i.e. revenue given sales)
	- Causal inference is about answering "what if" questions (what happens to sales if we change X)