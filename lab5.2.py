P_C_NT_given_P_T = 0.2  # Probability of purchasing Coke next time given Pepsi today
P_P_NT_given_P_T = 0.8  # Probability of purchasing Pepsi next time given Pepsi today
P_C_TN_given_C_NT = 0.9  # Probability of purchasing Coke the time after next given Coke next time
P_C_TN_given_P_NT = 0.2  # Probability of purchasing Coke the time after next given Pepsi next time

P_C_TN_given_P_T = (P_C_TN_given_C_NT * P_C_NT_given_P_T +
                    P_C_TN_given_P_NT * P_P_NT_given_P_T)

print(f"The probability that a person currently purchasing Pepsi will purchase Coke after two purchases is {P_C_TN_given_P_T:.2f}")
