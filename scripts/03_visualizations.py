import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load cleaned dataset
df = pd.read_csv("outputs/cleaned_data.csv")

# Histograms
plt.figure(figsize=(8, 5))
sns.histplot(df["cgpa"], bins=20, kde=True)
plt.title("CGPA Distribution")
plt.savefig("outputs/cgpa_distribution.png")

# Boxplot of CGPA by Program Code
plt.figure(figsize=(12, 5))
sns.boxplot(x="prog_code", y="cgpa", data=df)
plt.xticks(rotation=90)
plt.title("CGPA by Program Code")
plt.savefig("outputs/cgpa_by_program.png")

# Correlation heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(df.corr(), annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Feature Correlation Heatmap")
plt.savefig("outputs/correlation_heatmap.png")

print("Visualizations saved in outputs/")
