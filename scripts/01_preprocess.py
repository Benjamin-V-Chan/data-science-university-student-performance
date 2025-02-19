import pandas as pd

# Load dataset
df = pd.read_csv("data/academic_performance_dataset_V2.csv")

# Drop duplicates
df = df.drop_duplicates()

# Standardize column names
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

# Convert categorical variables if needed
df["gender"] = df["gender"].map({"Male": 0, "Female": 1})  # Encode gender

# Save cleaned dataset
df.to_csv("outputs/cleaned_data.csv", index=False)
print("Preprocessing complete. Cleaned data saved to outputs/cleaned_data.csv.")
