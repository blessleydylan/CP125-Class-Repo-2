# Lab 08 Exercise 1: Simple Score Filter
# Write your code below:

def filter_passing_scores(input_file, output_file):
    infile = open(input_file, "r")
    outfile = open(output_file, "w")

    lines = infile.readlines()
    passing_count = 0

    for i in range(0, len(lines), 2):
        student_id = lines[i].strip()
        score = int(lines[i+1].strip())

        if score >= 80:
            outfile.write(student_id + " " + str(score) + "\n")
            passing_count += 1

    infile.close()
    outfile.close()
    return passing_count
    


# Test your code here
result = filter_passing_scores("CP125-Class-Repo-2/labs/lab08/exercise1/data/scores.txt", "CP125-Class-Repo-2/labs/lab08/exercise1/data/passing.txt")
print(f"Passing students: {result}")
