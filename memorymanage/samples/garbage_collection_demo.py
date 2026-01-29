import gc

def demo_garbage_collection():
    print("--- 2. Garbage Collection Demo ---")
    
    # Check if GC is enabled
    print(f"Is GC enabled? {gc.isenabled()}")
    
    # Get thresholds
    thresholds = gc.get_threshold()
    print(f"GC thresholds (gen0, gen1, gen2): {thresholds}")
    
    # Get count of objects tracked by GC in each generation
    print(f"Current GC counts: {gc.get_count()}")
    
    print("\n--- Manually triggering collection ---")
    collected = gc.collect()
    print(f"Objects collected manually: {collected}")
    print(f"GC counts after manual collect: {gc.get_count()}")

if __name__ == "__main__":
    demo_garbage_collection()
