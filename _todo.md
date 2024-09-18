# todo

- Read relevant sections from the beginning in imbens2015causal and take notes
- Do the same for athey2017econometrics and integrate
- [ ] Full derivations of unbiasedness and variance of diff-in-means estimator
for online experiment setup (this is BRE, which is not straightforward. So I
first do CRE, and then adapt).

    - [ ] CRE finite sample case
    - [ ] CRE super-population case
    - [ ] BRE finite sample case
    - [ ] BRE super-population case

- [ ] Have a look at aronow2013class and integrate relevant material
- [ ] Write stats of online experiments drawing on relevant material from above




- [ ] Above derivations — book page, but also paper (check with Max for outlet)

- [ ] Testing and CI
- [ ] Power
    - [ ] Incorporate all metrics types to power calculation
    - [ ] Differentiate between relative and abs MDES (default is abs)
    - [ ] Derive power formula
        - [x] From first princples
        - [ ] Starting from alpha and beta
        - [ ] Visual Bloom approach
    - Derive shortcut formulas
        - [ ] Section on 16 vs 32 confusion
    - [ ] Clean up rest of chapter
    - [ ] Power for different metric types (define continuous, proportion, ratio, etc. metrics -- how do they affect calculations?)
    - [ ] Build power calculator (check Statsig one — but add unbalanced samples option), build beautiful visualisations (use uv for package mgt)

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

