# QuasiCalssicalMagnet
We simulate the magnetic order of some quasi-classical magnets on an 1D chain.
## Long range order in low dimensional systems
When we first learned phase transition of liquids and magnetism in statistical mechanics we understood symmetry breaking phases establish more easily in higher spatial dimensions. The intuitive reasoning is that in low dimensions orders are vulnerable against (quantum/thermal) fluctuations.

A very well known related fact in statistical physics is the Mermin-Wagner theorem, which states there can't be spontaneous symmetry breaking in dimension smaller than 3. I first knew about this statement some when I was in college, but have been overlooking one important condition -- the range of interaction most be "short enough." 
Because of this condition, there is no contradiction between this theorem and the spontaneously generated mass of photon in (1+1)D (as far as I understand it).

In fact we don't even have to worry about continuous symmetries yet. The 1D dimensional nearest-neighbor coupled Ising model, which was the thesis of Ising himself, does not possess ferromagnetic phase at finite temperature. In the standard statistical mechanics course, the very first toy model that demonstrates a ferromagnetic phase would be the 2 dimensional Ising model. Recently it came across me that 1 dimensional Ising type model can actually possess ferromagnetic phase for some long range interaction between spins. In this project, I am going to study some simple examples that demonstrate this phenomenon.
## Long-ranged Ising model

In the following plot I show finite magnetization at finite temperature can also be obtained if the interaction between spins _i_ and _j_ is long-range, in this case |i-j|^(-alpha) with alpha = 1.5. Explicitly, the Hamiltonian (the model) is 


![Hamiltonian](https://github.com/whhsiao/QuasiClassicalMagnet/blob/master/HIsing.png)

### Result of the magnetization 
The definition of the order parameter is given by

![orderparameter of simulation](https://github.com/whhsiao/QuasiClassicalMagnet/blob/master/OrderParameter.png)

We perform the Monte Carlo simulation to obtain this quantity as a function of inverse temperature.

![Monte Carlo simulation of magnetization](https://github.com/whhsiao/QuasiClassicalMagnet/blob/master/phaseTransition.png)

### Specific Heat

### Magnetic susceptibility 

![Monte Carlo simulation of magnetization](https://github.com/whhsiao/QuasiClassicalMagnet/blob/master/sus.png)
