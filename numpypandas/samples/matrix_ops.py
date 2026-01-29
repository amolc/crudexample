import numpy as np

def demo_matrix_ops():
    print("--- Matrix Operations & Linear Algebra ---")
    
    # Define matrices
    A = np.array([[1, 2], [3, 4]])
    B = np.array([[5, 6], [7, 8]])
    
    print(f"Matrix A:\n{A}")
    print(f"Matrix B:\n{B}")
    
    # Matrix Multiplication
    # Method 1: np.dot
    # Method 2: @ operator (Python 3.5+)
    C = A @ B
    print(f"\nMatrix Multiplication (A @ B):\n{C}")
    
    # Transpose
    print(f"\nTranspose of A:\n{A.T}")
    
    # Determinant
    det_A = np.linalg.det(A)
    print(f"\nDeterminant of A: {det_A:.2f}")
    
    # Inverse
    inv_A = np.linalg.inv(A)
    print(f"\nInverse of A:\n{inv_A}")
    
    # Identity Matrix check: A @ inv_A
    print(f"\nA @ Inverse(A) (Should be Identity):\n{np.round(A @ inv_A)}")
    print("-" * 40)

if __name__ == "__main__":
    demo_matrix_ops()
