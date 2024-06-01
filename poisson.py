import math

def poisson_distribution(x, lambd):
    return (math.exp(-lambd) * (lambd ** x)) / math.factorial(x)

lambd = 12  # Average arrival rate

print("Poisson Distribution for x = 0, 1, 2, ..., 15")
print("-----------------------------------------")
print("x\tP(X = x)")
print("-----------------------------------------")

for x in range(16):
    probability = poisson_distribution(x, lambd)
    print(f"{x}\t{probability:.4f}")