"""
Deep-ML Problem #6
Title: Calculate Eigenvalues of a Matrix
Category: Linear Algebra
Difficulty: Medium
"""

def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:
        
	a, b = matrix[0]
	c, d = matrix[1]

	tr = a + d 
	det = (a*d) - (b*c)

	eigenvalues = []
	eigenvalues.append((tr + (tr**2 - 4*det)**0.5 )/2)
	eigenvalues.append((tr - (tr**2 - 4*det)**0.5 )/2)
	
	return eigenvalues
