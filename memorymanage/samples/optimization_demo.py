import sys
import time

# 1. __slots__ optimization
class RegularUser:
    def __init__(self, id, name):
        self.id = id
        self.name = name

class SlottedUser:
    __slots__ = ("id", "name")
    def __init__(self, id, name):
        self.id = id
        self.name = name

def demo_optimization():
    print("--- 4. Memory Optimization Demo ---")
    
    # --- Slots Demo ---
    print("\n--- __slots__ vs Regular Classes ---")
    reg = RegularUser(1, "Amol")
    slot = SlottedUser(1, "Amol")
    
    # Regular classes have a __dict__ for dynamic attributes
    print(f"Regular instance has __dict__: {hasattr(reg, '__dict__')}")
    # Slotted classes do NOT have a __dict__
    print(f"Slotted instance has __dict__: {hasattr(slot, '__dict__')}")
    
    # Note: sys.getsizeof doesn't deep-traverse, but we can see the presence of __dict__
    print(f"Size of regular instance: {sys.getsizeof(reg)} bytes")
    print(f"Size of slotted instance: {sys.getsizeof(slot)} bytes")

    # --- Generators Demo ---
    print("\n--- Generators vs Lists ---")
    n = 1_000_000
    
    start = time.perf_counter()
    my_list = [i for i in range(n)]
    end = time.perf_counter()
    print(f"List of {n} elements created in {end-start:.4f}s")
    print(f"Memory size of list: {sys.getsizeof(my_list) / (1024*1024):.2f} MB")
    
    start = time.perf_counter()
    my_gen = (i for i in range(n))
    end = time.perf_counter()
    print(f"Generator for {n} elements created in {end-start:.4f}s")
    print(f"Memory size of generator: {sys.getsizeof(my_gen)} bytes")
    
    print("\nConclusion: Generators use constant memory regardless of size!")

if __name__ == "__main__":
    demo_optimization()
