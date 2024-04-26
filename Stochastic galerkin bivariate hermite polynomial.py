# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 19:19:24 2024

@author: thanh
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.special import hermite
from scipy.linalg import lstsq
from mpl_toolkits.mplot3d import Axes3D

# Define the parameters for the true function (a(theta)u(theta)+b(theta)u(theta)**3=f(theta))
a_coefficient = 1.0
b_coefficient = 0.5

# Define the degree of the polynomial chaos expansion
degree = 4

# Define the mean and standard deviation for the Gaussian random variables
mean_theta1 = 0.0
std_dev_theta1 = 1.0

mean_theta2 = 0.0
std_dev_theta2 = 1.0

# Define the bivariate Hermite basis functions
def bivariate_hermite_basis(x1, x2, n1, n2):
    return hermite(n1)(x1 / np.sqrt(2)) * hermite(n2)(x2 / np.sqrt(2))

# Generate samples for independent Gaussian random variables
num_samples = 1000000
theta1_samples = np.random.normal(loc=mean_theta1, scale=std_dev_theta1, size=num_samples)
theta2_samples = np.random.normal(loc=mean_theta2, scale=std_dev_theta2, size=num_samples)

# Normalize basis functions
normalized_bivariate_hermite_basis = lambda x1, x2, n1, n2: (
    bivariate_hermite_basis(x1, x2, n1, n2) / np.sqrt(np.math.factorial(n1) * 2**n1 * np.sqrt(np.pi) * np.math.factorial(n2) * 2**n2 * np.sqrt(np.pi))
)

# Construct basis matrix using normalized basis functions (u(theta)~sum(ci.phi(theta)))
basis_matrix = np.column_stack(
    [
        normalized_bivariate_hermite_basis(theta1_samples, theta2_samples, i, j)
        for i in range(degree + 1)
        for j in range(degree + 1)
    ]
)

# Evaluate the true function at the sample points
def true_function(theta1, theta2):
    u_theta = theta1**2 + 2 * theta2**2 #theta1*theta2  # Replace with the actual u(theta) function
    return a_coefficient * u_theta + b_coefficient * u_theta**3

f_samples = np.array([true_function(theta1, theta2) for theta1, theta2 in zip(theta1_samples, theta2_samples)])

# Solve the system using the Stochastic Galerkin method to find ci 
coefficients, _, _, _ = lstsq(basis_matrix, f_samples)

# Evaluate the solution at new points
num_evaluation_points = 50
theta1_evaluation = np.linspace(-5, 5, num_evaluation_points)
theta2_evaluation = np.linspace(-5, 5, num_evaluation_points)
theta1_mesh_evaluation, theta2_mesh_evaluation = np.meshgrid(theta1_evaluation, theta2_evaluation, indexing='ij')

# Evaluate normalized basis functions at evaluation points
basis_matrix_evaluation = np.column_stack(
    [
        normalized_bivariate_hermite_basis(theta1_mesh_evaluation.flatten(), theta2_mesh_evaluation.flatten(), i, j)
        for i in range(degree + 1)
        for j in range(degree + 1)
    ]
)

# Evaluate the solution using the coefficients
solution_evaluation = np.dot(basis_matrix_evaluation, coefficients)

# Reshape the solution for plotting
solution_evaluation = solution_evaluation.reshape(theta1_mesh_evaluation.shape)

# Plotting the results side by side
fig = plt.figure(figsize=(18, 6))

# Stochastic Galerkin Solution
ax1 = fig.add_subplot(121, projection='3d')
ax1.plot_surface(theta1_mesh_evaluation, theta2_mesh_evaluation, solution_evaluation, cmap='viridis')
ax1.set_title(f'Stochastic Galerkin Solution (Approximate) with {num_samples} samples')
ax1.set_xlabel('Theta 1')
ax1.set_ylabel('Theta 2')
ax1.set_zlabel('Solution')

# True Response Surface
ax2 = fig.add_subplot(122, projection='3d')
true_values_evaluation = np.array([true_function(theta1, theta2) for theta1, theta2 in zip(theta1_mesh_evaluation.flatten(), theta2_mesh_evaluation.flatten())])
true_values_evaluation = true_values_evaluation.reshape(theta1_mesh_evaluation.shape)
ax2.plot_surface(theta1_mesh_evaluation, theta2_mesh_evaluation, true_values_evaluation, cmap='viridis')
ax2.set_title('Exact Response Surface')
ax2.set_xlabel('Theta 1')
ax2.set_ylabel('Theta 2')
ax2.set_zlabel('Response')

plt.tight_layout()
plt.show()
