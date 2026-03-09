# Lab 08 Exercise 3: Product Price Lookup
# Write your code below:
import csv

def calculate_order_total(products_file, order_file, output_file):
    # Read products and store prices
    products = {}
    infile = open(products_file, "r")
    lines = infile.readlines()
    infile.close()

    for line in lines[1:]:  # skip header
        parts = line.strip().split(",")
        product_id = parts[0]
        price = float(parts[2])
        products[product_id] = price

    # Read orders and calculate totals
    orderfile = open(order_file, "r")
    lines = orderfile.readlines()
    orderfile.close()

    outfile = open(output_file, "w")
    outfile.write("product_id,total_cost\n")

    grand_total = 0

    for line in lines[1:]:  # skip header
        parts = line.strip().split(",")
        product_id = parts[0]
        quantity = int(parts[1])

        total_cost = products[product_id] * quantity
        grand_total += total_cost

        outfile.write(product_id + "," + format(total_cost, ".2f") + "\n")

    outfile.close()

    return grand_total


# Test your code here
result = calculate_order_total("CP125-Class-Repo-2/labs/lab08/exercise3/data/products.csv",
                                "CP125-Class-Repo-2/labs/lab08/exercise3/data/order.csv",
                                "CP125-Class-Repo-2/labs/lab08/exercise3/data/total.csv")
print(f"Grand total: ${result:.2f}")
