import csv

# Lists to store data
study_hours = []
attendance = []
scores = []

# 1. Load data from CSV
with open("data.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        study_hours.append(float(row["study_hours"]))
        attendance.append(float(row["attendance"]))
        scores.append(float(row["score"]))

# 2. Calculate basic statistics
average_score = sum(scores) / len(scores)
highest_score = max(scores)
lowest_score = min(scores)

average_study_hours = sum(study_hours) / len(study_hours)
average_attendance = sum(attendance) / len(attendance)

# 3. Simple pattern analysis
high_study_scores = [
    scores[i] for i in range(len(scores)) if study_hours[i] >= average_study_hours
]

if high_study_scores:
    average_high_study_score = sum(high_study_scores) / len(high_study_scores)
else:
    average_high_study_score = 0

# 4. Performance interpretation
if average_score >= 85:
    performance_level = "Excellent"
elif average_score >= 70:
    performance_level = "Satisfactory"
else:
    performance_level = "Needs Improvement"

# 5. Output results
print("STUDY PERFORMANCE ANALYSIS")
print("---------------------------")
print(f"Average score: {average_score:.1f}")
print(f"Highest score: {highest_score}")
print(f"Lowest score: {lowest_score}")
print(f"Average study hours: {average_study_hours:.1f}")
print(f"Average attendance: {average_attendance:.1f}%")
print(f"Average score of students studying above average hours: {average_high_study_score:.1f}")
print(f"Overall performance level: {performance_level}")