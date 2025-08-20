import random
import string
import pandas as pd

def generate_random_string(length=8, include_special=False, include_uppercase=True, include_digits=True):
    """Generate a random string of specified length with customizable options"""
    chars = string.ascii_lowercase
    if include_uppercase:
        chars += string.ascii_uppercase
    if include_digits:
        chars += string.digits
    if include_special:
        chars += "!@#$%^&*()_+-=[]{}|;:,.<>?"
    
    return ''.join(random.choices(chars, k=length))

def generate_random_strings(count=5, min_length=5, max_length=15):
    """Generate multiple random strings with varying lengths"""
    return [generate_random_string(random.randint(min_length, max_length)) for _ in range(count)]

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

def quick_sort(arr):
    """Quick sort implementation"""
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def merge_sort(arr):
    """Merge sort implementation"""
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)

def merge(left, right):
    """Helper function for merge sort"""
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def insertion_sort(arr):
    """Insertion sort implementation"""
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def benchmark_sorting_algorithms(arr):
    """Benchmark different sorting algorithms"""
    import time
    
    algorithms = {
        'Bubble Sort': bubble_sort,
        'Quick Sort': quick_sort,
        'Merge Sort': merge_sort,
        'Insertion Sort': insertion_sort,
        'Built-in Sort': lambda x: sorted(x)
    }
    
    results = {}
    for name, func in algorithms.items():
        arr_copy = arr.copy()
        start_time = time.time()
        func(arr_copy)
        end_time = time.time()
        results[name] = end_time - start_time
    
    return results

# Main execution
if __name__ == "__main__":
    print("Enhanced Random Python Code Examples!")
    print("=" * 50)
    
    # Generate random strings with different options
    print("\n1. Random String Generation:")
    print(f"Basic random string: {generate_random_string(10)}")
    print(f"With special chars: {generate_random_string(12, include_special=True)}")
    print(f"Only lowercase: {generate_random_string(8, include_uppercase=False, include_digits=False)}")
    
    # Generate multiple random strings
    random_strings = generate_random_strings(5, 3, 10)
    print(f"Multiple random strings: {random_strings}")
    
    # Calculate fibonacci
    print(f"\n2. Fibonacci(10): {fibonacci(10)}")
    
    # Sorting examples
    print("\n3. Sorting Algorithms:")
    numbers = [random.randint(1, 100) for _ in range(10)]
    print(f"Original numbers: {numbers}")
    
    # Test different sorting algorithms
    sorted_bubble = bubble_sort(numbers.copy())
    sorted_quick = quick_sort(numbers.copy())
    sorted_merge = merge_sort(numbers.copy())
    sorted_insertion = insertion_sort(numbers.copy())
    
    print(f"Bubble sort: {sorted_bubble}")
    print(f"Quick sort: {sorted_quick}")
    print(f"Merge sort: {sorted_merge}")
    print(f"Insertion sort: {sorted_insertion}")
    
    # Benchmark sorting algorithms
    print("\n4. Sorting Algorithm Benchmark:")
    benchmark_results = benchmark_sorting_algorithms(numbers)
    for algo, time_taken in benchmark_results.items():
        print(f"{algo}: {time_taken:.6f} seconds")
    
    # List and dictionary comprehensions
    print("\n5. Advanced Examples:")
    squares = [x**2 for x in range(1, 11)]
    print(f"Squares 1-10: {squares}")
    
    word_count = {word: len(word) for word in ["hello", "world", "python", "programming"]}
    print(f"Word lengths: {word_count}")
    
    # Generate random data for pandas
    print("\n6. Pandas Example:")
    data = {
        'name': generate_random_strings(5, 4, 8),
        'age': [random.randint(18, 65) for _ in range(5)],
        'score': [random.uniform(0, 100) for _ in range(5)]
    }
    df = pd.DataFrame(data)
    print("Random DataFrame:")
    print(df)
