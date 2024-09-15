---
title: "Top Challenges from the first Practical Online Controlled Experiment Summit"
author: "Fabian Gunzinger"
date: 5 June 2024
date-format: D MMM YYYY
slide-number: true
format: html
#   revealjs:
#     smaller: true  
bibliography: /Users/fabian.gunzinger/.dotfiles/latex/fabib.bib
---

## Intro

- This 2019 conference invited representatives from experimentation leaders to discuss common challenges and solutions.

- Outcomes are discussed in @gupta2019top

- This deck summarises the findings

## Estimating long-term effects

**Problem**

- Experiments run for 1-2 weeks, but we care about long-term effects.

- Measuring long-term effects directly is hard because:
  - Development cycles are short
  - Tracking based on cookies that suffer from churn over time


**Solutions and challenges**

- Long-term experiments
  - Impractical due to short dev cycles and need for agility

- Holdout groups
  - Significant engineering effort
  - Mixes cumulative and long-term effect
  - Doesn't address non-persistent tracking and network effects

- Slightly longer experiments (e.g. 4 wks) 
  - Use last two weeks for estimation of long-term effect
  - May of may not be long enough, but better than nothing

- Proxies
  - Estimating proxy metrics (e.g. find metrics that predict long-term outcome), then use these as experiment outcomes
  - Can be misleading and suffer from correlation $\neq$ causation

- Model user learning based on long-term effects
  - See @hohnhold2015focusing

- Surrogates
  - See Athey et al. work


## Overall evaluation criterion metric

**Problem**

- Without having a single metric to guide decision making, shipping decisions will be ad-hoc and based on HiPPO.

**Solutions and challenges**

- Defining a single metric is challenging because defining success of a session is not always trivial (search vs discovery in search engine)

- Product goals aren't always clear and uniform across subteams

- Even if they are clear, there is often more than one goal or key metric and they might be in conflict at times (e.g. revenue and user happiness)

- One approach is to weigh different metrics to create a single OEC

- Defining and changing OECs is challenging. Possible (complementary) approaches: expert input, corpus of historical experiments with clearly established effects, degradation experiments

- and sometimes contradictory (revenue and user happiness)

- One approach is to weigh different 

## Heterogeneous treatment effects

**Problem**

- We commonly estimate ATE, but sometimes we want to learn about the effect of different subgroups

**Solutions and challenges**

- Common segments:
  - Market/country
  - User activity level
  - Device/platform
  - Time and day of week
  - Product specific segment (normal user vs recruiters on LinkedIn)

- Computation
  - Most companies focus on categorical segments
  - Effects are commonly estimated using linear regression with an interaction term

- Challenges
  - Computation is expensive (for all metrics of all experiments)
  - Lower power
  - Multiple testing problem
  - Less interpretable and memorable results (esp. for non-specialists)
  - Absolute vs relative treatment effects (relative usually recommended to normalise across segments)
  - HTEs give correlation not causal effect (there can/will be omitted variable bias -- e.g. different users use different devices)

- Common solutions:
  - Separate on-demand vs scheduled analysis (former looks into HTEs and can take longer)
  - Sparse modeling
  - Combine results to make more memorable (e.g. effect on Asia rather than each single market)

## Developing experimentation culture

**Problem**


**Solutions and challenges**

- Experimentation platform and tools
- Practices, policies, and capabilities
  - High touch
  - Top down buy in
  - Negative and positive case studies
  - Safe rollout
  - Report cards and gamification
  - Education and support

## Training others in the organisation to scale experimentation

**Problem**
- A central experimentation team cannot handle all the demand
- Have experimentation experts across the business who can help

**Solutions and challenges**

- Experimentation ambassadors (Booking.com)
- Peer-review program (Booking.com)
- Center of excellence (Microsoft)
- Just-in-time education model (Google)



## Computation of experiment analysis and metrics

**Problem**

**Solutions and challenges**

- Data management and schema 
- Timely and trustworthy analysis
- Metric ownership
- Supporting exploratory and advanced experimentation pipelines


## Dealing with client bloat

**Problem**

- As more experiments are being run, the configuration downloaded to the client device gets bloated and starts to affect performance

**Solutions and challenges**


## Network interactions

**Problem**

**Solutions and challenges**
- Producer and consumer model
- Known influence network model
- One-to-one communication
- Market effects
- Multiple identities for the same person


## Interactions between multiple experiments

**Problem**

**Solutions and challenges**


## References
