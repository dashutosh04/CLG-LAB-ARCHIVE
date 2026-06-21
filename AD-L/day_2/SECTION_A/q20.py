principle = 1000
rate = 5
time = 3

compound_amount = principle * (1 + rate / 100) ** time
compound_interest = compound_amount - principle

print(f"CI: {compound_interest}")
