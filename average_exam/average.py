import pandas as pd

# Load the Excel file
file_path = "m2.xlsx"  # Replace this with the correct path to your Excel file
data = pd.read_excel(file_path)

# Clean and prepare the data
# Skip the first row and rename columns for clarity
data_cleaned = data.iloc[1:]  # Skip the first row (header)
data_cleaned.rename(columns={'Unnamed: 2': 'Scores'}, inplace=True)  # Rename "Unnamed: 2" to "Scores"

# Convert the Scores column to numeric
data_cleaned['Scores'] = pd.to_numeric(data_cleaned['Scores'], errors='coerce')

# Calculate the average score
average_score = data_cleaned['Scores'].mean()

# Display the result
print(f"The average score is: {average_score}")
