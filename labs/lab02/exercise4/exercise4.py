# Lab 02 Exercise 4: Dynamic Parking Rate
# Write your code below:

def get_hourly_rate(vehicle_type, hour_24):
    # TODO: Implement this function
    # Return hourly rate based on vehicle and time
    if (vehicle_type == "Electric"):
        total_price = 2.00
    elif (vehicle_type == "Hybrid") and ((hour_24 <= 6) or (hour_24 >= 22)):
        total_price = 2.00
    elif (vehicle_type == "Hybrid") and ((hour_24 > 6) or (hour_24 < 22)):
        total_price = 5.00
    else:
        total_price = 5.00
    return total_price
        
# Test your code here
print("Testing Dynamic Parking Rate...")