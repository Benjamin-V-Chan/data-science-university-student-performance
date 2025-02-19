import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score

# Load cleaned dataset
df = pd.read_csv("outputs/cleaned_data.csv")

# Define features and target variable
X = df[["sgpa", "cgpa100", "cgpa200", "cgpa300", "cgpa400"]]
y = df["cgpa"]

# Split data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate model
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

# Save predictions
predictions = pd.DataFrame({"Actual": y_test, "Predicted": y_pred})
predictions.to_csv("outputs/predictions.csv", index=False)

print(f"Modeling complete. MAE: {mae:.3f}, R²: {r2:.3f}. Predictions saved to outputs/predictions.csv.")
