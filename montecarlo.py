import random

def estimate_pi(num_points):
    inside_circle = 0

    for _ in range(num_points):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)
        distance = x**2 + y**2
        if distance <= 1:
            inside_circle += 1

    pi_estimate = (inside_circle / num_points) * 4
    return pi_estimate

num_points = 1000
pi_estimate = estimate_pi(num_points)
print(f"Estimated value of PI: {pi_estimate}")