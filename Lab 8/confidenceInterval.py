import scipy.stats as stats
import numpy as np

# Given data
sample_mean = 5.8
sample_std = 1.6
sample_size = 120
confidence_level = 0.95

# Calculate the degrees of freedom
df = sample_size - 1

# Calculate the critical value from the t-distribution
alpha = 1 - confidence_level
t_critical = stats.t.ppf(1 - alpha/2, df)

# Calculate the margin of error
margin_of_error = t_critical * (sample_std / np.sqrt(sample_size))

# Calculate the confidence interval
lower_bound = sample_mean - margin_of_error
upper_bound = sample_mean + margin_of_error

print(f"{confidence_level*100}% Confidence Interval: ({lower_bound:.2f}, {upper_bound:.2f})")
