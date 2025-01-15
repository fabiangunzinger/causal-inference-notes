[[_Experimentation]]

- In a randomised experiment with treatment indicator $W_i$, the difference in means estimator is defined as:

$$
\begin{align}
\hat{\tau}^{\text{dif}}
&= \bar{Y}_\text{t} - \bar{Y}_\text{c} \\
&= \frac{1}{n_\text{t}}\sum_{i:w_i=1}Y_i - \frac{1}{n_\text{c}}\sum_{i:w_i=0}Y_i \\
&= \frac{1}{n_\text{t}}\sum_{i=1}^{n}W_iY_i - \frac{1}{n_\text{c}}\sum_{i=1}^{n}(1-W_i)Y_i
\end{align}
$$


