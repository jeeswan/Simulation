def multiplicative_congruential_method(X0, m, a, n):
    # Initialize the seed value
    X = X0
    # List to store the random numbers
    random_numbers = []
    
    # Generate n random numbers
    for _ in range(n):
        X = (a * X) % m
        random_numbers.append(X)
    
    return random_numbers

# Parameters
X0 = 13
m = 1000
a = 15
n = 50

# Generate 50 random numbers
random_numbers = multiplicative_congruential_method(X0, m, a, n)

# Print the random numbers
for i, num in enumerate(random_numbers, 1):
    print(f"Random number {i}: {num}")
