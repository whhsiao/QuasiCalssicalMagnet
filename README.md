# QuasiCalssicalMagnet
We simulate the magnetic order of some quasi-classical magnets on an 1D chain.
## Long range order in low dimensional systems
A very well known result in statistical physics is the Mermin-Wagner theorem, which states there can't be spontaneous symmetry breaking in dimension smaller than 3. I first knew about this statement some when I was in college, but have been overlooking one important condition -- the range of interaction most be "short enough." 
Because of this condition, there is no contradiction between this theorem and the spontaneously generated mass of photon in (1+1)D (as far as I understand it).
In this project, I am going to study some simple examples that demonstrate this phenomenon.
## Classical XY model
## Long-ranged Ising model
Ising model is an even more simplified model for magnets. Seriously speaking, it doesn't fullfil the assumption of Mermin-Wagner theorem. I brought it in here since it's quite easy to simulate and also it's known that the short-range Ising model in 1D (the one solved by Ising himself) doesn't have finite magnetization except temperature = 0.

In the following plot I show finite magnetization at finite temperature can also be obtained if the interaction is long-range, in this case x^(-alpha) with alpha = 1.5.

![Monte Carlo simulation of magnetization](https://github.com/whhsiao/QuasiClassicalMagnet/blob/master/phaseTransition.png)
