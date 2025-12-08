# Lab 02 Exercise 1: Road Trip Budgeter
# Write your code below:

def is_budget_sufficient(one_way_km, km_per_liter, price_per_liter, budget):
    # TODO: Implement this function
    # Calculate round trip cost and checks if within budget
    total_distance = one_way_km * km_per_liter
    needed_budget = total_distance / price_per_liter
    round_trip_budget = needed_budget * 2
    
    # Check if budget is enough for a round trip
    if round_trip_budget < budget:
        round_trip = True
        return round_trip


# Test your code here
print("Testing Road Trip Budgeter...")
