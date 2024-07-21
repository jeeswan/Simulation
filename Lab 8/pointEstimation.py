import numpy as np

def calculate_point_estimation_and_bias(sample, population_mean):
    # Calculate the sample mean
    sample_mean = np.mean(sample)
    
    # Calculate the bias (difference between sample mean and population mean)
    bias = sample_mean - population_mean
    
    return sample_mean, bias

sample_data = [5.5, 6.1, 5.7, 6.6, 5.2, 6.0, 5.6, 6.3, 5.9, 5.8] 
population_mean = 6.1  

sample_mean, bias = calculate_point_estimation_and_bias(sample_data, population_mean)

print(f"Sample Mean (Point Estimation): {sample_mean:.2f}")
print(f"Bias: {bias:.2f}")
