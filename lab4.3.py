def mm1_queue_measures(arrival_rate, service_rate):
    # Calculate utilization (rho)
    rho = arrival_rate / service_rate
    
    # Probability of 0 customers in the system (P0)
    P0 = 1 - rho
    
    # Expected number of customers in the system (L)
    L = arrival_rate / (service_rate - arrival_rate)
    
    # Expected number of customers in the queue (Lq)
    Lq = rho * L
    
    # Expected time a customer spends in the system (W)
    W = 1 / (service_rate - arrival_rate)
    
    # Expected time a customer spends in the queue (Wq)
    Wq = W - (1 / service_rate)
    
    return {
        "Utilization (rho)": rho,
        "P0 (Probability of 0 customers in system)": P0,
        "L (Expected number of customers in system)": L,
        "Lq (Expected number of customers in queue)": Lq,
        "W (Expected time in system)": W,
        "Wq (Expected time in queue)": Wq
    }

# Example usage
arrival_rate = 1  # customers per minute
service_rate = 3  # customers per minute

measures = mm1_queue_measures(arrival_rate, service_rate)
for measure, value in measures.items():
    print(f"{measure}: {value:.2f}")
