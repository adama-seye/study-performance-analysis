import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("data/student-mat.csv", sep=";")

# Keep only numeric columns
numeric_df = df.select_dtypes(include=["int64", "float64"])

# Calculate the relationships (links) between variables
links = numeric_df.corr()

# Check which factors are most linked to final grade (G3)
g3_links = links["G3"].sort_values(ascending=False)
print("Top factors linked to final grade (G3):")
print(g3_links.head(10))

# Plot heatmap of links
plt.figure(figsize=(12, 8))
sns.heatmap(links, cmap="coolwarm", annot=False)
plt.title("Links Between Student Performance Variables")
plt.tight_layout()
plt.savefig("links_heatmap.png")
plt.show()

# Plot bar chart of top 10 links to G3
top_links = g3_links[1:11]  # skip G3 itself
plt.figure(figsize=(10,6))
top_links.plot(kind="bar", color="skyblue")
plt.title("Top Factors Linked to Final Grade (G3)")
plt.ylabel("Strength of Link")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("top_links.png")
plt.show()

# Simple scatter plot for absences vs final grade
plt.figure(figsize=(8,6))
plt.scatter(df["absences"], df["G3"], color="orange", alpha=0.6)

# Add a simple regression line
import numpy as np
m, b = np.polyfit(df["absences"], df["G3"], 1)  # linear fit
plt.plot(df["absences"], m*df["absences"] + b, color="blue")

plt.title("Link Between Absences and Final Grade")
plt.xlabel("Absences")
plt.ylabel("Final Grade (G3)")
plt.tight_layout()
plt.savefig("absences_vs_G3.png")
plt.show()

# Top links with final grade (G3)
top_links = g3_links[1:6]  # top 5 factors excluding G3 itself

plt.figure(figsize=(8,5))
top_links.plot(kind="bar", color="skyblue")
plt.title("Top Factors Linked to Final Grade (G3)")
plt.ylabel("Strength of Link")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("top_links.png")
plt.show()

# Scatter plot for absences vs final grade
plt.figure(figsize=(8,6))
plt.scatter(df["absences"], df["G3"], color="orange", alpha=0.6)

# Add a simple regression line
import numpy as np
m, b = np.polyfit(df["absences"], df["G3"], 1)
plt.plot(df["absences"], m*df["absences"] + b, color="blue")

plt.title("Link Between Absences and Final Grade")
plt.xlabel("Absences")
plt.ylabel("Final Grade (G3)")
plt.tight_layout()
plt.savefig("absences_vs_G3.png")
plt.show()

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Features and target
X = df[["G1", "G2", "studytime"]]
y = df["G3"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Model
model = LinearRegression()
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Evaluation
print("R² Score:", r2_score(y_test, y_pred))
print("RMSE:", mean_squared_error(y_test, y_pred, squared=False))
