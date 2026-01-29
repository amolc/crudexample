import sys

def demo_reference_counting():
    print("--- 1. Reference Counting Demo ---")
    
    # Create an object
    a = [1, 2, 3]
    print(f"Initial list created: a = {a}")
    print(f"Reference count of 'a': {sys.getrefcount(a)} (includes the call to getrefcount)")
    
    # Create a new reference
    b = a
    print(f"\nNew reference created: b = a")
    print(f"Reference count of 'a': {sys.getrefcount(a)}")
    
    # Reference in a list
    c = [a]
    print(f"\nReference added to a list: c = [a]")
    print(f"Reference count of 'a': {sys.getrefcount(a)}")
    
    # Remove references
    print("\nRemoving references...")
    del b
    print(f"After 'del b', reference count of 'a': {sys.getrefcount(a)}")
    
    c.pop()
    print(f"After 'c.pop()', reference count of 'a': {sys.getrefcount(a)}")
    
    print("\nNote: When ref count drops to 0 (excluding internal temporary refs), the memory is deallocated.")

if __name__ == "__main__":
    demo_reference_counting()
