#Student Name: Olorode Feyisayomi
import random

# Generate a dictionary of random names and scores
data = {
    "names": ["Alice", "Bob", "Charlie", "Alice", "Bob"],
    "scores": [random.randint(50, 101) for i in range(5)]
}


# Find the top scorer from the data
max_score = max(data["scores"])  #removed .pop because it wasn't necessary
index = data["scores"].index(max_score)
print(data["names"][index])


# Remove duplicates from names (if any) using a set comprehension
data["names"] = list({name for name in data["names"]})

# Sort the names in reverse alphabetical order
data["names"] = sorted(data["names"],reverse=True)  #changed .sort to sorted()
print("Cleaned and Sorted Names:", data["names"])

# Create a summary report for all names
report = {}
for name, score in zip(data["names"], data["scores"]):
    grade = "Pass" if score > 60 else "Fail"
    report[name] = grade.upper() if score > 60 else grade #added () to upper to covert grade to uppercase
print(report)

