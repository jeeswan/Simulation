import random

def monte_carlo_simulation(f, a, b, n):
    total = 0
    for _ in range(n):
        x = random.uniform(a, b)
        y = random.uniform(0, 1)
        if y <= f(x):
            total += 1
    return total / n * (b - a)

def f(x):
    return x**2

a = 0
b = 1
n = 100000

area = monte_carlo_simulation(f, a, b, n)
print(f"The estimated area under the curve y = x^2 from {a} to {b} is {area:.6f}.")