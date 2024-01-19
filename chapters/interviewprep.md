# Background

## Product

How does it work?
- Panel on feed with gallery of short videos

Main purpose?
- Share fun moments with your community

How does it provide value for users?
- Can share and watch videos with/from community and feel engaged

What is success?
- Users upload frequently and consume frequently and engage positively


## Objective

- Decide whether or not to replace current with new recommendation algorithm.


# Pre-design

## Intervention

- New algo changes which videos are shown
- We've got one new algo that we compare to control

- Treatment: show videos based on new algo
- Control: show videos based on current algo


## Metrics

OEC

- AVg. time spend watching reels per week per user

Drivers
- Share: Avg. number of reel uploads per user per week per user
- Consume: Number of reels clicked per week per user
- Engagement: Avg. reactions to reels per week per user

Guardrails

- Protect business
  - Same metrics as above, but for Insta stories, FB reels and stories (to avoid cannibalisation)

- Protect user experience
  - Latency
  - Video loading
  - ...

- Protecting exp internal validity
  - SRM 


## Target audience

- Global (no reason to restrict)


## Hypothesis

H0: ... will have no effect on ...
H1: New recommendation algorithm will increase avg. time spend watching reel videos per week per user across the entire universe of users.


## Decision-making process

- Suggestion: nail down when to implement (green), not implement (red), and run experiment for longer/rerun with more data (amber)


# Design

## Exposure/roll-out

- Use 1% of global universe

## Key parameters

Sig level (alpha): 0.05
Power: 0.8
MDE: 1%


## Randomisation

Unit
- User

Ass mechanisms
- Bernoulli (hash based)

Variant allocation
- 50/50 to max power


## Sample size/exp duration

- Do power calc to get min sample size
- Adjust by shared traffic
- Adjust by ramp-up strategy
- Adjust by internal validity considerations (seasonality, dow effects, learning effects)
= Experiment duration

## Anaysis strategy

- Simple t-test (regression or t-test based)


## Limitations

- Driver metrics will suffer from interaction effects
- Ignores subgroups / segment analysis


# Implementation

## Risks

Internal validity

- REM 
- Dow effects
- Seasonality
- Non-represeantative users
- 


External validity
- Not problematic given that we use global universe

Ethics

Project mgt

# (Analysis, delivery, wrap-up)

- How to present results for max usefulness for stakeholder


#########################################################################################
#########################################################################################
#########################################################################################


## Lessons

- Think about control: what do we compare new feature to? (What do we show presently instead)

- Need metrics for which I can compare t and c (above point should fix that largely, but can only use features that are present in both, i.e. likes)

