# student Name :Olorode Feyisayo
import time
import functools
# Timing Decorator
# Write a decorator to measure and print function execution time
def timing_decorator(func):
    @functools.wraps(func)
    def wrapper(*args,**kwargs):
        start_time = time.time()
        result = func(*args,**kwargs)
        end_time = time.time()
        print(f"Execution time: {end_time - start_time:.3f} seconds") 
        return result
    return wrapper

# Validation Decorator
# Write a decorator to validate function 
def inputvalidation_decorator(validator):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if not validator(*args, **kwargs):
                raise ValueError("Invalid input!")
            return func(*args,**kwargs)
        return wrapper
    return decorator
        

# Logging Decorator
# Write a decorator to log function calls

# Example Function
# Define a simple function to demonstrate decorators

if __name__ == "__main__":
    """
    Test your decorators here by applying them to your functions and calling them.
    """
    pass  # Replace with your test code