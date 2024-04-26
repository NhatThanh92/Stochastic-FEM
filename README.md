This code performs a Stochastic Galerkin method to approximate a response surface defined by a function:
$f(\theta_{1}, \theta_{2}) = a(\theta)u(\theta) + b(\theta)u(\theta)^{3}, \text{ where } u(\theta) = \theta_{1}^{2} + 2\theta_{2}^{2}.$

This method is used for uncertainty quantification where the response of a system is approximated in terms of a series expansion involving orthogonal polynomials (here, Hermite polynomials) weighted by coefficients obtained by solving a system of equations. 
In this code, the solution is visualized along with an exact response surface for comparison.

![image](https://github.com/NhatThanh92/Stochastic-FEM/assets/51020597/5076f999-f649-4354-a7b2-d65f7db4639b)
![image](https://github.com/NhatThanh92/Stochastic-FEM/assets/51020597/df1d59c7-869f-412d-891c-98d2786ad4b5)
![image](https://github.com/NhatThanh92/Stochastic-FEM/assets/51020597/cfc27892-cc6d-4c8a-a3d9-57d8e220c181)
![image](https://github.com/NhatThanh92/Stochastic-FEM/assets/51020597/5e2fd61c-d52f-4984-b0c7-1db160bcede2)






...
