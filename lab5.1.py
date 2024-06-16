P_Nt_plus_1_given_Nt = 0.8  # No rain tomorrow given no rain today
P_Rt_plus_1_given_Nt = 0.2  # Rain tomorrow given no rain today
P_Nt_plus_2_given_Nt_plus_1 = 0.8  # No rain the day after tomorrow given no rain tomorrow
P_Nt_plus_2_given_Rt_plus_1 = 0.6  # No rain the day after tomorrow given rain tomorrow

P_Nt_plus_2_given_Nt = (P_Nt_plus_2_given_Nt_plus_1 * P_Nt_plus_1_given_Nt +
                        P_Nt_plus_2_given_Rt_plus_1 * P_Rt_plus_1_given_Nt)

print(f"The probability that it will not rain the day after tomorrow given that it is not raining today is {P_Nt_plus_2_given_Nt:.2f}")
