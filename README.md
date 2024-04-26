This code performs a Stochastic Galerkin method to approximate a response surface defined by a function
(θ₁, θ₂) = a(θ)u(θ) + b(θ)u(θ)³, where u(θ) = θ₁² + 2θ₂².
The Stochastic Galerkin method is used for uncertainty quantification where the response of a system is approximated in terms of a series expansion involving orthogonal polynomials (here, Hermite polynomials) weighted by coefficients obtained by solving a system of equations. 
In this code, the solution is visualized alongside the exact response surface for comparison.
## Description

\ (\theta_{1}, \theta_{2}) = a(\theta)u(\theta) + b(\theta)u(\theta)^{3}, \text{ where } u(\theta) = \theta_{1}^{2} + 2\theta_{2}^{2}.



...
