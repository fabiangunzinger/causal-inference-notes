[[_Experimentation]]

Common types of selection bias in data science:

- The vast search effect (using the data to answer many questions will eventually reveal something interesting by mere chance -- if 20,000 people flip a coin 10 times, some will have 10 straight heads)

- Nonrandom sampling

- Cherry-picking data

- Selecting specific time-intervals

- Stopping experiments prematurely

- Regression to the mean (occurs in settings where we measure outcomes repeatedly over time and where luck and skill combine to determine outcomes, since winners of one period will be less lucky next period and perform closer to the mean performer)

  

Ways to guard against selection bias:

- have one or many holdout datasets to confirm your results.