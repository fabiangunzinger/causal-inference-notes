# Statistics {#sec-statistics}

The goal of this part of the book is to collect all the statistical theory that
underlies online experiments.

Most online experiments are very simple; we split traffic into groups with
different experiences and compare outcomes between groups---how much
statistical theory could we possibly need?

Well, to experiment effectively, you want, at a minimum, the following:

1. A coherent definition of the causal effect you want to measure, a
   reliable way of estimating it, and a way to quantify the uncertainty around
   your estimate.

2. A way to differentiate between estimates that signal the existence of a true
   effect and those that are the results of random noise in the data.

3. A way to ensure your experiment has a good chance of picking up signals if
   there are any.

First two are covered here. The third, which relates to the power of your
experiment, is covered in @sec-power.

