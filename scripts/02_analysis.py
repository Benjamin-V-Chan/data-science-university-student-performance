import pandas as pd

# Load cleaned dataset
df = pd.read_csv("outputs/cleaned_data.csv")

# Generate summary statistics
summary = df.describe(include="all")

# Compute correlations
correlations = df.corr()

# Grouped analysis
grouped_gender = df.groupby("gender")["cgpa"].mean()
grouped_program = df.groupby("prog_code")["cgpa"].mean()

# Save analysis results
with open("outputs/eda_summary.txt", "w") as f:
    f.write("Summary Statistics:\n")
    f.write(summary.to_string())
    f.write("\n\nCorrelation Matrix:\n")
    f.write(correlations.to_string())
    f.write("\n\nAverage CGPA by Gender:\n")
    f.write(grouped_gender.to_string())
    f.write("\n\nAverage CGPA by Program Code:\n")
    f.write(grouped_program.to_string())

print("Analysis complete. Results saved to outputs/eda_summary.txt.")
