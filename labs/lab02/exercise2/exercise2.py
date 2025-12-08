# Lab 02 Exercise 2: Camping Logistics
# Write your code below:

import math

def calculate_event_cost(participants, tent_capacity, tent_price, meal_price):
    # TODO: Implement this function
    # Calculate total cost for tents and meals
    no_tents = participants / tent_capacity
    total_tent_price = no_tents * tent_price
    total_meal_price = meal_price * participants
    total_price = total_tent_price + total_meal_price
    return total_price

# Test your code here
print("Testing Camping Logistics...")
