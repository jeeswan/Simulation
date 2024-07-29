def calculate_sample_mean(sample_data):
    return sum(sample_data) / len(sample_data)

def calculate_bias(sample_mean, population_mean):
    return sample_mean - population_mean

def main():
    # Sample data (example)
    sample_data = [5.5, 6.1, 5.7, 6.6, 5.2, 6.0, 5.6, 6.3, 5.9, 5.8]
    
    # Known population mean
    population_mean = 6.1 
    
    # Calculate sample mean
    sample_mean = calculate_sample_mean(sample_data)
    
    # Calculate bias
    bias = calculate_bias(sample_mean, population_mean)
    
    # Output the results
    print(f"Sample Data: {sample_data}")
    print(f"Sample Mean (Point Estimation): {sample_mean}")
    print(f"Population Mean: {population_mean}")
    print(f"Bias: {bias:.2f}")

if __name__ == "__main__":
    main()
