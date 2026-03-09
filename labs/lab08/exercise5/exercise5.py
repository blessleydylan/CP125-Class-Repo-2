# Lab 08 Exercise 5: Sales Summary
# Write your code below:
import csv

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
    outfile.write("Total Revenue: $" + str(round(total_revenue, 2)) + "\n")
    outfile.write("Average Revenue: $" + str(round(average_revenue, 2)) + "\n")
    outfile.write("Highest Revenue: $" + str(round(highest_revenue, 2)) + "\n")
    outfile.write("Lowest Revenue: $" + str(round(lowest_revenue, 2)) + "\n")
    outfile.close()  # close output file

    # Return all values as a tuple
    return total_revenue, average_revenue, highest_revenue, lowest_revenue




# Test your code here
result = summarize_sales("data/sales.csv", "data/summary.txt")
print(f"Total: ${result[0]:.2f}, Avg: ${result[1]:.2f}, High: ${result[2]:.2f}, Low: ${result[3]:.2f}")
