from django.http import JsonResponse
import sys
import gc
import time

# Helper classes for demos
class Node:
    def __init__(self, name):
        self.name = name
        self.other = None

class SlottedUser:
    __slots__ = ("id", "name")
    def __init__(self, id, name):
        self.id = id
        self.name = name

def ref_count_demo(request):
    """Demonstrates how reference counts change."""
    obj = [1, 2, 3]
    initial_count = sys.getrefcount(obj)
    
    # Create extra refs
    ref1 = obj
    ref2 = obj
    count_after_refs = sys.getrefcount(obj)
    
    return JsonResponse({
        "concept": "Reference Counting",
        "object": str(obj),
        "initial_ref_count": initial_count,
        "count_after_2_extra_refs": count_after_refs,
        "explanation": "Reference counts increase when an object is assigned to a new name."
    })

def gc_status_demo(request):
    """Shows current GC status and thresholds."""
    return JsonResponse({
        "concept": "Garbage Collection Status",
        "is_enabled": gc.isenabled(),
        "thresholds": gc.get_threshold(),
        "current_counts": gc.get_count(),
        "explanation": "Generational GC tracks objects in 3 generations (0, 1, 2)."
    })

def memory_optimization_demo(request):
    """Compares List vs Generator memory usage."""
    n = 100000
    my_list = [i for i in range(n)]
    my_gen = (i for i in range(n))
    
    return JsonResponse({
        "concept": "Memory Optimization",
        "items_count": n,
        "list_size_bytes": sys.getsizeof(my_list),
        "generator_size_bytes": sys.getsizeof(my_gen),
        "slots_instance_size_bytes": sys.getsizeof(SlottedUser(1, "Demo")),
        "explanation": "Generators and __slots__ significantly reduce memory footprint."
    })

def cyclic_reference_demo(request):
    """Triggers a manual GC collect to show hidden cleanup."""
    # Create cycles
    for i in range(100):
        a = Node(f"A{i}")
        b = Node(f"B{i}")
        a.other = b
        b.other = a
    
    before_count = gc.get_count()
    collected = gc.collect()
    after_count = gc.get_count()
    
    return JsonResponse({
        "concept": "Cyclic References",
        "action": "Created 100 cyclic pairs and ran gc.collect()",
        "objects_collected": collected,
        "gc_counts_before": before_count,
        "gc_counts_after": after_count,
        "explanation": "GC handles objects that point to each other even if they are unreachable from the root."
    })
