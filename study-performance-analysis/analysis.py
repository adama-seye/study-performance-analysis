import csv

scores = []

with open("data.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)  # skip header
    for row in reader:
        scores.append(int(row[1]))

average = sum(scores) / len(scores)
print("Average score:", average)
highest = max(scores)
lowest = min(scores)

print("Average score:", average)
print("Highest score:", highest)
print("Lowest score:", lowest)
if average >= 85:
    level = "Excellent"
elif average >= 70:
    level = "Satisfactory"
else:
    level = "Needs Improvement"

print("Overall performance:", level)
