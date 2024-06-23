def mixed_congruential_method(X0, m, a, c, n):
    # Initialize the seed value
    X = X0
    # List to store the random numbers
    random_numbers = []
    
    # Generate n random numbers
    for _ in range(n):
        X = (a * X + c) % m
        random_numbers.append(X)
    
    return random_numbers

# Parameters
X0 = 11
m = 100
a = 5
c = 13
n = 50

# Generate 50 random numbers
random_numbers = mixed_congruential_method(X0, m, a, c, n)

# Print the random numbers
for i, num in enumerate(random_numbers, 1):
    print(f"Random number {i}: {num}")
