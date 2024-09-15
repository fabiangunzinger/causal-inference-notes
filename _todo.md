# todo

- [ ] Complete rest of the outline (i.e. testing, power, analysis)

- [ ] Work out derivation for unbiasedness and variance of diff in means estimator for simple randomised experiment

	- [ ] Follow derivations for completely randomised experiment in Imbens and Rubin
		- [x] Complete derivation
		- [ ] Move causal inference notes content to Obsidian so I can develop each topic in depth without having to worry about putting it in coherent shape just yet
			- [ ] Move setup
			- [ ] Move Outcomes
			- [ ] ...
		- [ ] Move derivations from Moleskin to Obsidian
	- [ ] Adapt derivations for simple randomised experiment
	- [ ] Finite sample vs super-population perspectives
		- [ ] Understand difference
		- [ ] Write out above derivations for both and discuss differences
		- [ ] Decide which one to use for book (at the moment, my instinct is that because they lead to the same result, I'll not make the distinction in the main text, but just present a single case and refer interested readers to more detailed appendices where derivations for both cases are presented)
- [x] Start moving content to Obsidian
- [x] Complete single-page outline for book


- [ ] Stats of online experiments
    - [x] Clean assignment
    - [x] Outcomes
    - [x] Standard error
    - [ ] Use super population perspective throughout
        - [x] Read ding2017bridging to see whether it helps resolve my fs vs sp questions -- it does.
        - [ ] Work through ding2017bridging
        - [ ] One I understand difference between fs and sp, decide how to frame
          issue in my notes: if they lead to the same variance, then I could
        just ignore the difference in the main text and discuss it in a
        footnotes. If they have different implications, I might want to
        introduce them early -- as I currently do in the setup section -- and
        discuss them separately. If I can, I want to do the first: just discuss
        fs case (the relevant one for rull ramp) and mention that during ramp
        up, we strictly speaking use sp approach but that results are the same.

        - [ ] Completely derive and understand fs approach in chapter 6
        - [ ] Completely derive and understand sp approach in chapter 6



    - [ ] Superpopulation e2e — book page, but also paper (check with Max for outlet)
    - [ ] Unbalanced sample — refer to my notes
    - [ ] Incorporate all metrics types to power calculation
    - [ ] Build power calculator (check statsic one — but add unbalanced samples option), build beautiful visualisations

    - [ ] Testing and CI
    - [ ] Power
        - [ ] Differentiate between relative and abs MDES (default is abs)
        - [ ] Derive power formula
            - [x] From first princples
            - [ ] Starting from alpha and beta
            - [ ] Visual Bloom approach
        - Derive shortcut formulas
            - [ ] Section on 16 vs 32 confusion
        - [ ] Clean up rest of chapter
        - [ ] Power for different metric types (define continuous, proportion, ratio, etc. metrics -- how do they affect calculations?)

- [ ] Produce clean up version on master and publish before continuing

Later:

- [ ] Regression
- [ ] Regression approach to experiments
    - [ ] Friedman critique
    - [ ] Lin response
    - [ ] Imbens and Rubin approach
- [ ] CUPED
    - [ ] Connection to DiD


- [ ] Power of random experiments (post 2)

- [ ] Variance reduction notes from JET project
- [ ] CUPED vs regression adjustment discussion 
    - [ ] Friedman critique of OLS and Lin response (and Imbens and Rubin take)
    - [ ] My notes on regression adjustment ignore demeaning (y tilde is alpha hat plut betahat times x, so not exactly the same as cuped, but has no effect because alpha is demeaning only and has no effect on cov and var. Write down)
    - [ ] Individual-level adjustment vs group adjustment (-x_i vs -\bar{x}) See Bookings post on this.
    - [ ] CUPED in practice: all the important decisions you have to make nobody talks about.


- [ ] FDR vs family-wise-false-positive rate
- [ ] Always-valid p-values

- [ ] Add visualisations
    - [ ] Find suitable library (tikz? 3b1b?)


## Stuff I'd like to incorporate

- [ ] Why is qe power lower than experiment power? must be due to higher sampling variance. how come?

- [ ] Incorporate relevant stuff from Spotify posts: https://engineering.atspotify.com/tag/experimentation/

- [ ] incorporate athey2017econometrics (of randomised experiments)
- [ ] Read Imbens and Athey papers

- imbens2020potential - up to section 2.4
- athey2019machine
- Marton Trencseni posts on a/b testing (https://bytepawn.com/tag/ab-testing.html)
- Lukas Vermeer posts (https://www.lukasvermeer.nl/publications/)
- [ ] Gelman et al chapters
- [ ] Quasi-experimental methods - Angrist and Pischke book
- [ ] Cox and Reid book (https://www.amazon.co.uk/Experiments-Chapman-Monographs-Statistics-Probability-ebook/dp/B00UVA67EC/ref=tmm_kin_swatch_0?_encoding=UTF8&qid=1673947989&sr=8-1)
- [ ] Business data science (https://www.lukasvermeer.nl/publications/)
Stuff to consider
- ML and causal inference Mixtape course
- Machine learning and econometrics (Athey and Imbens lectures - https://www.aeaweb.org/conference/cont-ed/2018-webcasts)
- Trustworthy Online Controlled Experiments book
- [ ] bojinov2023design section 5 for cool approach to experiment simulation that I might want to add to rosalie.

## Done

- [x] CI notes on effect of below on experiments (for meta interview prep)
    - [x] Seasonality
    - [x] Network effects
    - [x] Cannibalisation
- [x] Set up provisional book structure
- [x] Move existing material from other places
- [x] Push to Github
- [x] Publish book on website -- gonna wait with that until I have some content
- [x] Projection
    - [x] Create outline on paper
    - [x] Solve Quarto preview in vscode (workaround using localhost in simple browser inside vscode, but need to refresh manually)
    - [x] Solve math limitations -- rmd works (10 theorems, so quarto should, too) -- use quarto book
    - [x] Run cells in quarto book
    - [x] Projection in general

