# Lab 08 Exercise 4: Student Grade Calculator
# Write your code below:
import csv

import csv

def calculate_final_grades(input_file, output_file):
    infile = open(input_file, "r", newline="")
    reader = csv.reader(infile)

    outfile = open(output_file, "w", newline="")
    writer = csv.writer(outfile)

    next(reader)  # skip header

    writer.writerow(["student_id", "final_grade"])

    total = 0
    count = 0

    for row in reader:
        student_id = row[0]
        midterm = float(row[1])
        final = float(row[2])

        final_grade = (midterm * 0.4) + (final * 0.6)

        writer.writerow([student_id, f"{final_grade:.2f}"])

        total += final_grade
        count += 1

    infile.close()
    outfile.close()

    return total / count
    
    


# Test your code here
result = calculate_final_grades("CP125-Class-Repo-2/labs/lab08/exercise4/data/scores.csv", "CP125-Class-Repo-2/labs/lab08/exercise4/data/grades.csv")
print(f"Average final grade: {result:.2f}")
