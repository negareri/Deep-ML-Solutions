"""
Deep-ML Problem #8
Title: Calculate 2x2 Matrix Inverse
Category: Linear Algebra
Difficulty: Easy
"""

def inverse_2x2(matrix: list[list[float]]) -> list[list[float]] | None:
    """
    Calculate the inverse of a 2x2 matrix.
    
    Args:
        matrix: A 2x2 matrix represented as [[a, b], [c, d]]
    
    Returns:
        The inverse matrix as a 2x2 list, or None if the matrix is singular
        (i.e., determinant equals zero)
    """
    
    def det(f):
        return(f[0][0]*f[1][1] - f[0][1]*f[1][0])
    
    determinant = det(matrix)

    if determinant == 0:
        return None
    
    def helper(m):
        a, b = m[0]
        c, d = m[1]
        return [[d, b*-1], [c*-1, a]]
    
    inverse_base = helper(matrix)

    a_inv = []
    for i in range(2):
        row = []
        for j in range(2):
            row.append((1/determinant) * inverse_base[i][j])
        a_inv.append(row)
    
    return a_inv
