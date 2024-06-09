# Constants
lambda_rate = 1 / 1  # Arrival rate (customers per minute)
mu_rate = 1 / (20 / 60)  # Service rate (customers per minute)
time_to_seat = 1.5  # Time to reach the correct seat (minutes)
time_before_game = 2  # Time before the game starts (minutes)

Wq = lambda_rate / (mu_rate * (mu_rate - lambda_rate))

Ws = 1 / mu_rate

W = Wq + Ws

T_total = W + time_to_seat

can_be_seated = T_total <= time_before_game

print(f"Total time spent by a sports fan to be seated: {T_total:.2f} minutes")
print(f"Can the sports fan be seated before the kick-off? {'Yes' if can_be_seated else 'No'}")
