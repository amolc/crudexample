import numpy as np
import time

def demo_numpy_performance():
    print("--- NumPy vs Python Lists Performance ---")
    size = 1_000_000
    
    # Python List
    l1 = list(range(size))
    l2 = list(range(size))
    start = time.time()
    result_list = [x + y for x, y in zip(l1, l2)]
    print(f"Python List Addition: {time.time() - start:.4f} seconds")
    
    # NumPy Array
    a1 = np.arange(size)
    a2 = np.arange(size)
    start = time.time()
    result_np = a1 + a2
    print(f"NumPy Array Addition: {time.time() - start:.4f} seconds")
    print("-" * 40)

def demo_numpy_basics():
    print("--- NumPy Array Basics ---")
    # 1D Array
    arr1d = np.array([1, 2, 3, 4, 5])
    print(f"1D Array: {arr1d}")
    
    # 2D Array
    arr2d = np.array([[1, 2, 3], [4, 5, 6]])
    print(f"2D Array:\n{arr2d}")
    print(f"Shape: {arr2d.shape}, Dimensions: {arr2d.ndim}, Dtype: {arr2d.dtype}")
    
    # Special Arrays
    print(f"Zeros:\n{np.zeros((2, 3))}")
    print(f"Ones:\n{np.ones((2, 2))}")
    print(f"Range (arange): {np.arange(0, 10, 2)}")
    print(f"Linspace: {np.linspace(0, 1, 5)}")
    print("-" * 40)

def demo_broadcasting():
    print("--- NumPy Broadcasting ---")
    a = np.array([[1, 2, 3], [4, 5, 6]])
    b = np.array([10, 20, 30])
    
    print(f"Array A:\n{a}")
    print(f"Array B (broadcasted):\n{b}")
    print(f"Result (A + B):\n{a + b}")
    print("-" * 40)

if __name__ == "__main__":
    demo_numpy_performance()
    demo_numpy_basics()
    demo_broadcasting()
