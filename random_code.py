import random
import string
import pandas as pd

#dsffsdv
def generate_random_string(length=8):
    """Generate a random string of specified length"""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def fibonacci(n):
    """Calculate fibonacci number"""
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

def bubble_sort(arr):
    """Simple bubble sort implementation"""
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# Main execution
if __name__ == "__main__":
    print("Random Python Code Examples!")
    
    # Generate random string
    random_str = generate_random_string(10)
    print(f"Random string: {random_str}")
    
    # Calculate fibonacci
    fib_num = fibonacci(8)
    print(f"Fibonacci(8): {fib_num}")
    
    # Sort random numbers
    numbers = [random.randint(1, 100) for _ in range(5)]
    print(f"Original numbers: {numbers}")
    sorted_numbers = bubble_sort(numbers.copy())
    print(f"Sorted numbers: {sorted_numbers}")
    
    # List comprehension example
    squares = [x**2 for x in range(1, 6)]
    print(f"Squares: {squares}")
    
    # Dictionary comprehension
    word_count = {word: len(word) for word in ["hello", "world", "python"]}
    print(f"Word lengths: {word_count}")
