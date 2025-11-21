# APStatsSims
This is where I am storing all the simulations I use for AP Statistics.

## Rolling a Pair of Dice
For this simulation, I wanted to demonstrate how --- after a sufficiently large number of rolls --- the relative frequency of an event converges to its probability.

I used the example of rolling a pair of fair dice and getting a 7. The behavior after 10M rolls is displayed below:

![Dice Simulation](https://github.com/KCervantesSJND/APStatsSims/blob/main/dice7.png)

The blue line is the relative frequency and the orange line is the probability. We can see that after a while, the lines converge.

## Fleet of 7 Cars
In the textbook, there is a problem where 16% of cars fail a smog check. We want to simulate 7 cars moving through and use that to estimate the probability that all 7 pass.

10M simulations were run and the relative frequencies were plotted below.

![Car Simulation](https://github.com/KCervantesSJND/APStatsSims/blob/main/car.png)

### Actual Probability
Assuming each car failing is independent,

$$
\begin{aligned}
P \left( \text{all 7 pass} right) &= \left[ P \left( \text{pass} \right) \right]^7 \\
&= \left[ 1 - P \left( \text{fail} \right) \right]^7 \\
&= \left( 1 - 0.16) \right)^7 \\
&= 0.84^7 \\
\approx 30%
\end{aligned}
$$
