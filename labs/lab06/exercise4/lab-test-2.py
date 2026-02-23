#   Name: Blessley Dylan Beldin  | Class: C02
#   Problem Description:
''' This is a program that accepts 5 integer input values from the user and is stored in a list. 
    It will also print all the numbers that has been entered in ascending order,
    Calculate and find the sum of all the entered numbers,
    and find and print the largest number.
'''


# Declare Function "calculate_sum_min_max_5_numbers"
def calculate_sum_min_max_5_numbers():
    
    # Create Empty List Called "numbers"
    numbers = []

    # Loops 5 Times to get 5 Numbers in a List
    for item in range(1, 6):
        num = int(input(f"Enter number {item}: "))
        numbers.append(num)

    # Find Sum, Min, Max of Numbers in the List
    ascending_numbers = sorted(numbers)
    total_sum = sum(numbers)
    largest_number = max(numbers)

    # Print Sum, Min, Max Of Numbers in the List
    print("Numbers in ascending order:", ascending_numbers)
    print("Sum of all numbers:", total_sum)
    print("Largest number:", largest_number)

calculate_sum_min_max_5_numbers()
