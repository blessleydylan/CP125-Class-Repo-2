# Lab 08 Exercise 2: Text File Merger
# Write your code below:

def merge_lists(file1, file2, output_file):
    list1 = open(file1, "r")
    list2 = open(file2, "r")
    output = open(output_file, "w")

    content1 = set(list1.readlines())
    content2 = set(list2.readlines())

    merged = sorted(content1 | content2)

    for name in merged:
        output.write(name)

    list1.close()
    list2.close()
    output.close()

    return len(merged)


# Test your code here
result = merge_lists(
    "CP125-Class-Repo-2/labs/lab08/exercise2/data/list1.txt",
    "CP125-Class-Repo-2/labs/lab08/exercise2/data/list2.txt",
    "CP125-Class-Repo-2/labs/lab08/exercise2/data/merged.txt"
)

print(f"Unique names: {result}")