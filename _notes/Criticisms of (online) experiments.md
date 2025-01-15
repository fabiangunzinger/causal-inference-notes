[[_Experimentation]]

There are a number of issues here that I want to collect and develop further.

## RCT critique of Deaton and co.

- Read and understand critique of Deaton and coauthors, read also Imbens' response and overall understand debate here and develop my own thoughts.
- How does this relate to tech?

- Summary from @stevenson2024cause (see paper for more details and comprehensive list of sources)
	1) They cannot be used to study the past.
	2) They can only estimate the effect of treatments that can be manipulated ("no causation without manipulation" Rubin).
	3) Guidance for policy limited by compliance issues, environmental dependence, and equilibrium effects.
	4) There are ethical concerns.

## Using "big data" to manipulate consumers

- The main concern here is that large amounts of data about individuals is used to specifically target those individuals in ways that might be harmful to them or not align with their best interest.
- I think experiments that are part of the product development process -- the way experiments are generally used in tech -- are not part of this, since they don't usually use any information about individuals (i.e. no covariates), focus on average outcomes and determine the experience of all users, rather than creating experiences for individual users.
- Having said that, the degree to which the above is true depends on what metrics are being optimised for. The alignment problem seems more pronounced for social media platforms that aim to increase "time spent on site" than for e-commerce sites that aim to increase conversion (there are a few assumptions baked in here, such as that time on social media might not be beneficial and that conversion on e-commerce signifies a customer having found what they were looking for. But they both seem defensible)


## Running ethical online experiments

Some useful principles to consider, based on reading chapter 9 in @kohavi2020trustworthy

- Only test changes that Company policy would allow you to roll out to 100 percent of users i.e. for Meta, deliberately showing them negative content wouldn't qualify. Personally I'm not sure I agree. I think in the Meta example, it would be useful to understand the effect of exposure to negative content. I'm not gonna think about this deeply now, but I think adapting the rule to not showing levels of content users couldn't organically be exposed to on the platform might be more useful. In the Meta example, this would allow for studying the effect of negative content in a systematic way without making the experience worse for treatment users than it actually is for some users (and could well be for treatment users, too). The reason for my willingness to entertain to go further is that there is a potentially large benefit to understanding harm. Yes, there might be some cost in the very short term (and you'd obviously want ot bound that cost somehow, as I proposed above, in order to guard against slippery slopes), but if the insights gained allow you to prevent large harm indefinitely later, then that's worth considering. Two other thoughts: motivation clearly matters here. And: the possibility of a slippery slope is not generally an argument to not do something -- often, as here -- there are quite natural and objective ways to draw a line on how far one would be willing to go.

- Aim for equipoise: this is a situation where, ex-ante, there is no grounds to favour one variant over another. This is the normal case. (The term is borrowed from clinical trial, where clinical equipoise is the assumption in an RCT that no drug is ex-ante better than another).

- Some worthwhile experiments violate equipoise: increasing latency, disabling feature, showing more adds, all aim to help us collect data which can be useful to make tradeoffs later on, which, ultimately, can benefit users.

- Beware of behavioural experiments and deception.

- Presumptive consent: ask a small subset of users whether they would be okay participating and if they do, assume that the sentiment would generalise.

- Different from clinical trials, subjects in online trials usually have the opportunity to switch service (for sth like FB, this might be difficult).

##  Salganik (2018)'s three principles of ethical design?

- Replace: use quasi-experiments whenever possible.

- Refine: make interventions as harmless as possible.

- Reduce: use the minimum necessary number of participants (use power analysis to make sure you're not over-powered).



- Why all this? Because we can never know whether an intervention is not harmful to at least some participants.