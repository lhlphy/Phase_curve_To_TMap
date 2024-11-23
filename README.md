The jupyter notebook is designed to transform phase-curve (measured by telescope) to temperature distribution map on planet surface, the notebook is well-commented and interactive. 
Anyone can run it immediately as a demo, and solve your problems after modified key parameters. The reference only gives 1D temperature distribution (along longitude).
This project assumes $T(\theta)\sim \cos^{1/4}\theta$, $\theta$ is latitude, so it can construct 2-D temperature map from 1D curve.

We use a simple Fourier series to fit the phase curve, see details in Reference.

Reference:
>Cowan, Nicolas B., and Eric Agol. “Inverting Phase Functions to Map Exoplanets.” The Astrophysical Journal 678, no. 2 (May 10, 2008): L129–32. https://doi.org/10.1086/588553.
