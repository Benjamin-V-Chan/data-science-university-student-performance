# data-science-university-student-performance

# Project Overview
This project analyzes academic performance data to identify patterns, trends, and predictive insights. It includes preprocessing, exploratory data analysis (EDA), visualizations, and a predictive model for CGPA.

# Folder Structure
```
project-root/
├── data/            # Contains the dataset
├── scripts/         # Contains all Python scripts
├── outputs/         # Stores generated results (cleaned data, reports, visualizations, predictions)
├── requirements.txt # Lists dependencies
├── README.md        # Project documentation
```

# Usage
### 1. Setup the Project:
Clone the repository.
Ensure you have Python installed.
Install required dependencies using the requirements.txt file.
```sh
pip install -r requirements.txt
```

### 2. Run the Preprocessing Script:
Cleans the dataset and saves it as `outputs/cleaned_data.csv`.
```sh
python scripts/01_preprocess.py
```

### 3. Run the Analysis Script:
Generates summary statistics and insights, saving results to `outputs/eda_summary.txt`.
```sh
python scripts/02_analysis.py
```

### 4. Run the Visualization Script:
Generates key visualizations and saves them in `outputs/`.
```sh
python scripts/03_visualizations.py
```

### 5. Run the Modeling Script:
Trains a regression model to predict CGPA and saves predictions in `outputs/predictions.csv`.
```sh
python scripts/04_modeling.py
```

# Requirements
- Python 3.x
- pandas
- matplotlib
- seaborn
- scikit-learn

# Acknowledgments
**Dataset Name:** Academic Performance of University Student Dataset  
**Dataset Author:** Krishnansh Verma  
**Dataset Source:** [Kaggle](https://www.kaggle.com/datasets/krishnanshverma/academic-performance-of-university-student-dataset)
