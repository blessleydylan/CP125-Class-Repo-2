# Lab 08 Exercise 3: Product Price Lookup
# Write your code below:
import csv

def calculate_order_total(products_file, order_file, output_file):

    
    """
    Calculate total cost for each product in order.

    Args:
        products_file: path to products CSV (product_id,product_name,price)
        order_file: path to order CSV (product_id,quantity)
        output_file: path to output CSV file

    Returns:
        float: grand total of all orders
    """
    # TODO: Implement this function
    pass


# Test your code here
result = calculate_order_total("CP125-Class-Repo-2/labs/lab08/exercise3/data/products.csv",
                                "CP125-Class-Repo-2/labs/lab08/exercise3/data/order.csv",
                                "CP125-Class-Repo-2/labs/lab08/exercise3/data/total.csv")
print(f"Grand total: ${result:.2f}")
