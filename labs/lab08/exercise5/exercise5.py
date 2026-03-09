# Lab 08 Exercise 5: Sales Summary
# Write your code below:
import csv

import csv
import shutil
import tempfile

def summarize_sales(input_file, output_file):
    revenues = []

    # Open input file
    infile = open(input_file, "r", newline="")
    reader = csv.reader(infile)
    next(reader)  # skip header

    for row in reader:
        quantity = float(row[1])
        price = float(row[2])
        revenues.append(quantity * price)

    infile.close()  # close input file

    total_revenue = sum(revenues)
    average_revenue = total_revenue / len(revenues)
    highest_revenue = max(revenues)
    lowest_revenue = min(revenues)

    # Open output file
    outfile = open(output_file, "w")
    outfile.write("Total Revenue: ${:.2f}\n".format(total_revenue))
    outfile.write("Average Revenue: ${:.2f}\n".format(average_revenue))
    outfile.write("Highest Revenue: ${:.2f}\n".format(highest_revenue))
    outfile.write("Lowest Revenue: ${:.2f}\n".format(lowest_revenue))
    outfile.close()  # close output file

    # Return all values as a tuple
    return total_revenue, average_revenue, highest_revenue, lowest_revenue



# Test your code here
result = summarize_sales("CP125-Class-Repo-2/labs/lab08/exercise5/data/sales.csv", "CP125-Class-Repo-2/labs/lab08/exercise5/data/summary.txt")
print(f"Total: ${result[0]:.2f}, Avg: ${result[1]:.2f}, High: ${result[2]:.2f}, Low: ${result[3]:.2f}")
