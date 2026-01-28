import time
import functools

# 1. Basic Decorator
def my_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"--- Starting execution of {func.__name__} ---")
        result = func(*args, **kwargs)
        print(f"--- Finished execution of {func.__name__} ---")
        return result
    return wrapper

# 2. Performance Monitoring Decorator
def timer_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        print(f"Function {func.__name__} took {end_time - start_time:.4f} seconds")
        return result
    return wrapper

@my_decorator
@timer_decorator
def say_hello(name):
    time.sleep(0.5)
    print(f"Hello, {name}!")

# 3. Generators
def fibonacci_generator(n):
    """Generates the first n Fibonacci numbers."""
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

def square_generator(numbers):
    """Lazy evaluation example."""
    for n in numbers:
        yield n * n

if __name__ == "__main__":
    print("--- Decorator Demo ---")
    say_hello("Amol")
    
    print("\n--- Fibonacci Generator Demo ---")
    for num in fibonacci_generator(8):
        print(num, end=" ")
    print()
    
    print("\n--- Square Generator Demo ---")
    my_nums = [1, 2, 3, 4, 5]
    squares = square_generator(my_nums)
    print(f"Generator object: {squares}")
    print(f"First square: {next(squares)}")
    print(f"Second square: {next(squares)}")
