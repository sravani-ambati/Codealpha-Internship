def fibonacci_generator(n):
    fib_sequence = []
    a, b = 0, 1
    while len(fib_sequence) < n:
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence

# Example usage
print("Enter how many fibonacci numbers you want:")
n = int(input())  # Generate the first 10 Fibonacci numbers
print(fibonacci_generator(n))