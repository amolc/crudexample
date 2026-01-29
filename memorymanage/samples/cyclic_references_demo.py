import gc
import sys

class Node:
    def __init__(self, name):
        self.name = name
        self.other = None
    def __del__(self):
        print(f"DEBUG: Deleting {self.name}")

def demo_cyclic_references():
    print("--- 3. Cyclic References Demo ---")
    
    # Disable auto GC to see the effect clearly
    gc.disable()
    print("GC disabled.")
    
    print("\nCreating cyclic reference...")
    a = Node("Node A")
    b = Node("Node B")
    
    a.other = b
    b.other = a
    
    print(f"Ref count of a: {sys.getrefcount(a)}")
    print(f"Ref count of b: {sys.getrefcount(b)}")
    
    print("\nDeleting local names 'a' and 'b'...")
    del a
    del b
    
    # Objects still exist in memory because they point to each other!
    # __del__ has NOT been called yet.
    print("Local names deleted, but __del__ was NOT called (check output above).")
    
    print("\nManually triggering GC to clean up cycles...")
    gc.collect()
    print("GC collect finished. __del__ should have been called now.")
    
    gc.enable()
    print("GC re-enabled.")

if __name__ == "__main__":
    demo_cyclic_references()
