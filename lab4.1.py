
lambda_rate = 1 / 10  # Arrival rate (customers per minute)
mu_rate = 1 / 5       # Service rate (customers per minute)

# a. Probability that a customer will not have to wait at the counter (P0)
P0 = 1 - (lambda_rate / mu_rate)

# b. Expected number of customers in the bank (L)
L = lambda_rate / (mu_rate - lambda_rate)

# c. Time a customer expects to spend in the bank (W)
W = 1 / (mu_rate - lambda_rate)

print(f"Probability that a customer will not have to wait at the counter: {P0:.2f}")
print(f"Expected number of customers in the bank: {L:.2f}")
print(f"Time a customer expects to spend in the bank: {W:.2f} minutes")
