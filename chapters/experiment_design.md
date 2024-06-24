# Experiment design

- Have separate page for how to think about design -- how to approach it -- a checklist for good design (based on Meta interview prep)


## Designs

- Check cox2000theory book. It's the bible.
- See BIT blue book section 5
- athey2017econometrics for rigorous discussion of basic designs

### Assignment mechanisms

Notes from @imbens2015causal:

A *randomised experiment* is an assignment mechanism that

1. is probabilistic (each unit has positive probability of being assigned to treatment and control), and
2. has a known functional form that is controlled by the researcher (e.g. p(treatment) = 1/2).

A *classical randomised experiment* is a randomised experiment with an assignment mechanism that is    

1. Individualistic (assignment probabilities for each unit is independent of information on 

2. Unconfounded (assignment probabilities are independent of potential outcomes)



### Bernoulli randomised experiments

- Assigning each unit to treatment using coin-flip


### Completely randomised experiments

- Ensuring exactly $N_t$ units are in treatment and rest in control


### Stratified randomised experiments

- Compared to completely randomised experiment, improve efficiency of ATE estimator by disallowing uninformative treatment allocations

Stratification is a treatment allocation method in which the pool of eligible units is first divided into strata (or groups or blocks) so as to ensure balance along certain variables. Random assignment is then performed within each group.

Effect: Random allocation of treatment ensures that control and treatment group will be similar in expectation, stratification ensures that along certain dimensions they will be in practice. If we stratify by gender and language, for instance, we make sure that both control and treatment group have the same proportion of women who speak a given language.

Advantages:  1.) It can increase efficiency of the estimator by lowering residual variance (intuitively, it has the opposite effect of clustering: it makes samples more representative of the overall population, which means that repeated samples will be more similar, which means that the standard error of the estimator is smaller). 2.) It allows analysis by subgroups.

Disadvantages: it can lead to very different sample sizes in different strata.

When to stratify?
- We should stratify if we want to:
- increase power
- achieve balance
- analyse data by subgroups

...and what variables to use? Use variables that
- are highly correlated with the outcome variable
- are discrete (can be discretised)
- are the subgroups of interest

How to adjust analysis? 

- Calculate treatment effect and variance separately for each subgroup using Neyman approach
- Then calculate overall TE and Var using stratum-weighted averages


### Matching

How to adjust analysis? Matching is an extreme form of stratifying, and so the approach is the same: we include a dummy for each (but one) matched pair. (If we have matched on test scores, we include a dummy for all but one possible test scores).


### Paired randomised experiments

Paired randomisation is an extreme form of stratification where the size of each stratum equals the number of treatment cells.

If we have three cells (two treatments and one control) and we pair based on test scores, we pick groups of three students, starting with the three highest scoring ones, and randomly assign one of them to each cell.

The aim is to increase power and achieve balance, and it's particularly useful if we have small samples.

The danger is that if we have attrition and one of the three students drops out, we lose all three observations (OLS will drop all observations with the relevant dummy because there is a missing value). One remedy is to have strata of size double or triple the cell number.


### Clustered randomised experiments

- Clustered randomised experiments are not designed to improve efficiency over CRE, but instead to address concerns with interactions at the unit level.

- Like in stratified design, we start by partitioning of covariate space (e.g. partition by city name). We call the resulting groups clusters instead of strata. But unlike a stratification design where units within a strata are then randomly assigned to treatment and control, we randomise at the level of the cluster, assigning all units within a cluster to the same variant.

- So, we have a CRE/BRE at the level of the clusters

Analysis:

- Choice of estimand:

    - Overall population ATE
    - Unweighted average of cluster-level ATEs

### Switchback designs

- Also called time-series experiments.


Notes on bojinov2020design

- AB tests have two main challenges in practice: dealing with interaction effects, and estimating heterogeneous treatment effects.

- Switchback experiments sequentially assign units to a random treatment, measure the response, and repeat the proceedure for a fixed period of time.

- The approach can thus deal with both limitations above: it limits interference, and it can estimate individual-level causal effects, thus providing the ability to estimate heterogeneous treatment effects.

- Instead of making assumptions on the outcome model under interference, switchback experiments require assumptions on the duration of carryover effects, the duration for which the effects of one treatment during a particular period affects outcomes in subsequent periods (the authors call this carryover duration the "order of carryover effects").

- Thus far, most switchback approaches have assumed away carryover effects

- Paper provides solution to optimal switchback design in the presence of carryover effects.

- Carryover effects create bias, leading to a different treatment control comparison if switch happens hourly vs weekly

- Tradeoff: fewer switching points (lower bias) vs more switching points (lower variance). 

- Authors provide computational approach to optimal design

- There are two main areas of application: to deal with interference in a network (either in the context of [network or marketplace interference](network_experiments.qmd## Types of interferance)) and to deal with situations where we have a limited number of units in the experiment and where we expect heterogeneous treatment effects.

- There are three main challenges when running switchback experiments:

    1. ATE estimators from switchback experiments have high variance because the precision is a function of the total number of assignments.

    2. One has to deal with the existence of carryover effects.

    3. Super-population inference requires unrealistic assumptions.

- The paper provides solutions for all of them:

    1. It provides an optimal design approach that reduces variance

    2. It assumes carryover effects and shows that estimation and inference is valid both when they are correctly and incorrectly specified, though in the latter case estimation variance is higher. The authors also provide a method for practitioners to measure the duration of carryover effects.

    3. It takes a purely design-based perspective on inference by assuming that outcomes are unknown but fixed, which means that findings are wholly non-parametric and robust to model misspecification (akin to the approach of [Fisher's exact P-value approach](fisher.qmd))

- Assumptions:

**Assumption 1 (Non-anticipating Potential Outcomes).** 

For any $t \in [T]$, $w_{1:t} \in \{0,1\}^t$, and for any $w', w'' \in \{0,1\}^{T-t}$,
$$ Y_t(w_{1:t}, w'_{t+1:T}) = Y_t(w_{1:t}, w''_{t+1:T})$$

- This says that potential outcomes don't depend on future assignments. Given that we control the assignment mechanisms, this holds by design (i.e. units can't adapt their behaviour in a given period based on future assignments because these assignments are random).

**Assumption 2 (m-Carryover Effects).** 

There exists a fixed and given m, such that for any $t \in \{m+1, m+2, \ldots, T\}$, $w \in \{0,1\}^{T-t+m+1}$, and for any $w', w'' \in \{0,1\}^{t-m-1}$,
$$ Y_t(w'_{1:t-m-1}, w_{t-m:T}) = Y_t(w''_{1:t-m-1}, w{t-m:T})$$

- This says that outcomes at time $t$ are independent of assignenments more than $m$ periods in the past.

- Together, the two assumption imply that for any $t \in \{m + 1, \ldots, T\}$ and any two assignment paths $w, w' \in \{0, 1\}^{m+1}$, whenever $w = w'$ this leads to:

$$
Y_t(w_{1:T})=Y_t(w'_{1:T})
$$

- Which is a rigorous way of waying that all that matters do determine potential outcomes at time $t$ is the assignment history of the previous $m$ periods.



- @bojinov2023design

- @bojinov2019time

- [Experiment Rigor for Switchback Experiment Analysis](https://doordash.engineering/2019/02/20/experiment-rigor-for-switchback-experiment-analysis/)

- [Analyzing Switchback Experiments by Cluster Robust Standard Error to Prevent False Positive Results](https://doordash.engineering/2019/09/11/cluster-robust-standard-error-in-switchback-experiments/)



### Step-wedge / phase-in randomised experiments

- Similar to switchback, but can only switch from control to treatment (see bajari2023experimental)

- Might allow us to estimate long-term effects. If we focus on a specific age-group or cohort. Because then certain people will never receive the treatment and can thus act as a long-run control group. (Example: if we focus on kids in their last year of school and phase-in periods are a year, then once we get to the third school, two cohorts will have graduated and will never receive the program.)

### Split-plot design

- See bajari2023experimental



### Interleaving

- Netflix users interleaving in first stage to quickly filter out most promising recommendation algorithms that can then be tested in classic A/B test.

- Interleaving works as follows:

  - We have two algorithms, A and B, each with a ranked list of recommendations
  - Instead of showing some users the list from A and others that of B, we create interleaved lists using team-drafting algorithm:
  - We randomly select from which algo we take the first item, for subsequent items, each algo alternates in contributing its highest ranked item that isn't yet in the interleaved list
  - Each user is then shown such a list at each visit
  - Advantage: we massively increase effective sample size, and we get a direct within-unit comparison between A and B each time

- Results for Netflix
  - Find that interleaving in first stage reduces required sample size by >100x
  - Preference from interleaving correlates strongly (R .95) with A/B test results


Sources:

- [Innovating Faster on Personalization Algorithms at Netflix Using Interleaving](https://netflixtechblog.com/interleaving-in-online-experiments-at-netflix-a04ee392ec55)

- [Interleaving at Airbnb](https://medium.com/airbnb-engineering/beyond-a-b-test-speeding-up-airbnb-search-ranking-experimentation-through-interleaving-7087afa09c8e)

- [Large-scale validation and analysis of interleaved search evaluation](https://dl.acm.org/doi/10.1145/2094072.2094078)


### Multiple randomisation design

### Pigeonhole design

- Design to improve covariance balance in sequentially randomised units in online experiments

- Up to 10% variance reduction over completely randomised design in simulations based on Yahoo! data

- zhao2024pigeonhole


### Multi-arm bandits





### Wait-list design

### Factorial design 

### Encouragement design

- It measures the effect of those who took up the program because of the encouragement but would not have otherwise (LATE). So it's particularly helpful if we are interested in the effect of encouragement on marginal participants. 

- The encouragement must not encourage some and discourage others (monotonicity assumption).


## General considerations

### Between vs within designs

What's the difference between a "between-subjects design" and a "within-subjects design" and what are their advantages? What is a "mixed-design"?

- A between design compares the treatment group to a control group, a within design compares the treatment group to itself before the treatment, so that each participant acts as their own control group.
- The strength of a between design is that it protects against confounding factors, that of a within design that it improves precision (because we have baseline data).
- A mixed design is where we have a control group and baseline data. If we use that baseline, the estimator is then a difference-in-difference estimator, which is statistically more efficient.


### Choosing unit of randomisation 

Factors to consider: 
- Spillovers
- The level of treatment administration
- The level of measurement (randomisation level needs to be the same or higher)
- Power
- Attrition and compliance (within-group randomisation may lead to resentment among participants and staff)
- Feasibility (what is easiest, cheapest, politically possible, ...)

Question:
- You randomise at customer level. For analysis, you do the following: you calculate metrics at a restaurant level, then calculate variant level averages from the restaurant-level averages. Is there a problem? What is it? What assumptions are being violated? 


### Dimensions along which we can vary randomisation 

Aspect: 
- access
- access around cutoff
- timing
- encouragement

Level: 
- individual 
- group

### Choosing number of units per arm

- Show that equal split maximises power if N is fixed (use power formula and show that power is max for p = 1-p )

- If we have many treatment groups, then more units should be allocated to control to estimate its effect more precisely (add formula)

- if sample variances differ, the ratio of the sample sizes should equal the ratio of the standard deviations.



## Q & A

### Questions

**1.**

A food delivery company randomises at the customer level, then calculates outcomes at the restaurant level for both treatment and control group (i.e. avg food price at restaurant for treatment group units is 25, for control group units it's 22), then calculates the variant-level average based on the restaurant averages, and then calculates the ATE as the difference between the two variant-level averages. Is this a problem? What assumptions does it relate to? Does it violate any?

### Answers