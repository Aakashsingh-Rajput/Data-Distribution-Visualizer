import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("student_performance.csv")

# Numeric columns
numeric_cols = ['Hours_Studied', 'Attendance (%)', 'Assignments_Submitted', 'Test_Score']

# Set seaborn style
sns.set(style="whitegrid")

# ---------------- Histogram Page ----------------
plt.figure(figsize=(12, 5))
plt.suptitle("Histograms of Student Performance Metrics", fontsize=14)

for i, col in enumerate(numeric_cols):
    plt.subplot(1, 4, i+1)
    sns.histplot(df[col], bins=5, kde=True, color="skyblue")
    plt.title(col, fontsize=9)
    plt.xlabel(col)
    plt.ylabel("Frequency")

plt.tight_layout(rect=[0, 0, 1, 0.93])
plt.show()

# ---------------- Boxplot Page ----------------
plt.figure(figsize=(12, 5))
plt.suptitle("Boxplots of Student Performance Metrics", fontsize=14)

for i, col in enumerate(numeric_cols):
    plt.subplot(1, 4, i+1)
    sns.boxplot(y=df[col], color="lightcoral")
    plt.title(col, fontsize=9)
    plt.xlabel("Metric")
    plt.ylabel(col)

plt.tight_layout(rect=[0, 0, 1, 0.93])
plt.show()
